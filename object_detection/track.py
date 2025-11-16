import cv2
import numpy as np

def compute_hsv_bounds(
    roi_bgr,
    s_thresh=40,
    v_thresh=40,
    lower_perc=5,
    upper_perc=95,
    h_margin=5,
    s_margin=15,
    v_margin=15
):
    """
    Given a BGR ROI, compute HSV lower/upper bounds robustly:
    - Convert ROI to HSV
    - Ignore very dark / low-saturation pixels (black text, shadows)
    - Use percentiles instead of raw min/max
    - Add small margins and clamp to valid ranges
    """
    hsv_roi = cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2HSV)
    hsv_flat = hsv_roi.reshape(-1, 3)

    H = hsv_flat[:, 0].astype(np.float32)
    S = hsv_flat[:, 1].astype(np.float32)
    V = hsv_flat[:, 2].astype(np.float32)

    # Keep only reasonably "colored" pixels (ignore black text etc.)
    valid_mask = (S > s_thresh) & (V > v_thresh)
    if np.count_nonzero(valid_mask) < 50:
        # Fallback: if filter is too aggressive, use all pixels
        valid_mask = np.ones_like(H, dtype=bool)

    H = H[valid_mask]
    S = S[valid_mask]
    V = V[valid_mask]

    # Use percentiles for robustness
    h_min = np.percentile(H, lower_perc)
    h_max = np.percentile(H, upper_perc)
    s_min = np.percentile(S, lower_perc)
    s_max = np.percentile(S, upper_perc)
    v_min = np.percentile(V, lower_perc)
    v_max = np.percentile(V, upper_perc)

    lower = np.array([
        max(0,   h_min - h_margin),
        max(0,   s_min - s_margin),
        max(0,   v_min - v_margin)
    ], dtype=np.uint8)

    upper = np.array([
        min(179, h_max + h_margin),
        min(255, s_max + s_margin),
        min(255, v_max + v_margin)
    ], dtype=np.uint8)

    return lower, upper

def calibrate_object_from_camera(cap):
    """
    Show live feed, let the user capture a frame with 'c',
    then select ROI with the mouse. Return (lower_hsv, upper_hsv, frame_shape).
    """
    print("Calibration mode:")
    print("  - A window will show the camera feed.")
    print("  - Press 'c' to capture a frame for calibration.")
    print("  - Press 'q' to quit without calibrating.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read from camera during calibration.")
            return None, None, None

        # Optional: flip for mirror-style view
        frame = cv2.flip(frame, 1)

        cv2.putText(frame, "Press 'c' to capture frame, 'q' to quit",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Calibration - Live Feed", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            captured_frame = frame.copy()
            break
        elif key == ord('q'):
            return None, None, None

    cv2.destroyWindow("Calibration - Live Feed")

    # Let user select ROI
    print("Select the object to track by dragging a box. Press ENTER or SPACE to confirm, or ESC to cancel.")
    roi = cv2.selectROI("Select Object", captured_frame, showCrosshair=True, fromCenter=False)
    cv2.destroyWindow("Select Object")

    x, y, w, h = roi
    if w == 0 or h == 0:
        print("No ROI selected. Calibration cancelled.")
        return None, None, None

    roi_bgr = captured_frame[y:y+h, x:x+w]

    lower_hsv, upper_hsv = compute_hsv_bounds(roi_bgr)
    print("Calibration complete.")
    print("Lower HSV:", lower_hsv)
    print("Upper HSV:", upper_hsv)

    return lower_hsv, upper_hsv, captured_frame.shape

def track_objects(cap, lower_hsv, upper_hsv, max_objects=10, min_area=500):
    """
    Track objects that fall within the HSV bounds.
    Draw bounding boxes around up to max_objects largest matches.
    """
    print("\nTracking started.")
    print("  - Press 'q' to quit.")
    print(f"  - Tracking up to {max_objects} objects matching calibrated color.\n")

    kernel = np.ones((5, 5), np.uint8)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from camera.")
            break

        # Flip for mirror-style view (optional)
        frame = cv2.flip(frame, 1)

        blurred = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

        # Clean mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter by area
        valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) >= min_area]

        # Sort contours by area (largest first)
        valid_contours = sorted(valid_contours, key=cv2.contourArea, reverse=True)

        # Limit number of contours based on max_objects
        valid_contours = valid_contours[:max_objects]

        for cnt in valid_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Tracked Object", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Tracking", frame)
        cv2.imshow("Mask", mask)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

def main():
    # Ask user how many objects to track
    try:
        max_objects = int(input("Enter max number of objects to track (e.g. 5): ").strip())
    except ValueError:
        max_objects = 5
        print("Invalid input. Defaulting to max_objects =", max_objects)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Step 1: calibration (capture + ROI selection + HSV bounds)
    lower_hsv, upper_hsv, frame_shape = calibrate_object_from_camera(cap)
    if lower_hsv is None or upper_hsv is None:
        print("Calibration failed or cancelled. Exiting.")
        cap.release()
        cv2.destroyAllWindows()
        return

    # Step 2: tracking
    track_objects(cap, lower_hsv, upper_hsv, max_objects=max_objects)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

