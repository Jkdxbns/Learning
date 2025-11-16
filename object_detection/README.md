# 📌 Color-Based Object Tracking with OpenCV

A real-time object tracking system built for my *robotics: vision and sensors* assignment using **OpenCV + Python** that allows the user to **calibrate any object by selecting it on the screen** and then track all occurrences of that object based on its **color cluster (HSV)**.

This project supports:

* ✔ Real-time tracking from webcam
* ✔ Automatic color calibration from user-selected ROI
* ✔ Percentile-based, robust HSV bound estimation
* ✔ Noise-resistant masking with morphology
* ✔ Tracking of **1 to many** objects
* ✔ Bounding boxes + real-time visualization

---

## 🚀 Features

### 🎯 1. Robust Color Calibration

Instead of hardcoding HSV values, the user:

* Presses **`c`** to capture a frame
* Selects an **ROI** (Region Of Interest) around the object
* The algorithm computes HSV lower/upper bounds using:

  * Percentiles (not min/max)
  * Ignoring dark + gray pixels (S/V thresholds)
  * Adjustable safety margins

This prevents issues with **text shadows, black print, or underexposed regions** inside the ROI.

---

### 🟧 2. Real-Time Color-Based Tracking

Once calibrated, the system:

* Converts each frame to HSV
* Thresholds using the calibrated range
* Cleans noise with OpenCV morphology
* Finds contours and draws bounding boxes
* Tracks up to **N objects** (user-defined)

---

### 📸 3. Mirror-Mode Live Preview

The webcam feed is automatically flipped horizontally for a natural, mirror-like experience.

---

## 🖥️ Demo (Screenshots)

> *(Replace these with your actual screenshots)*

| Calibration                            | ROI Selection                    | Tracking                         |
| -------------------------------------- | -------------------------------- | -------------------------------- |
| ![calibration](images/calibration.png) | ![roi](images/roi_selection.png) | ![tracking](images/tracking.png) |

---

## 📂 Project Structure

```
color-object-tracker/
│
├── tracker.py           # Main script (calibration + tracking)
├── README.md            # Documentation (this file)
└── images/              # Optional screenshots for README
```

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/color-object-tracker.git
cd color-object-tracker
```

### 2. Install dependencies

```bash
pip install opencv-python numpy
```

(Optional, for better performance)

```bash
pip install opencv-contrib-python
```

---

## ▶️ Usage

Run the main script:

```bash
python tracker.py
```

### Step-by-Step Workflow

#### **1️⃣ Calibration Phase**

* The webcam opens.
* Position the object in view.
* Press **`c`** to capture a frame.
* A selection window opens.
* Drag a rectangle around the object you want to track.
* Press **Enter** to confirm.

The program will:

* Detect the color cluster
* Compute HSV ranges
* Print the values
* Enter tracking mode

---

#### **2️⃣ Tracking Phase**

Now the program will:

* Highlight all pixels that match your calibrated color
* Draw bounding boxes around each object
* Track up to **N objects** (entered at start)

Press **`q`** to quit.

---

## 🧠 How the Algorithm Works

### 1. Convert ROI to HSV

HSV space separates color information more cleanly than BGR.

### 2. Ignore low-S and low-V pixels

This removes black text / darker noise from the ROI.

### 3. Use percentiles (5th–95th)

Prevents a few extreme pixels from ruining the range.

### 4. Add small margins

Makes tracking tolerant to lighting changes.

### 5. Threshold each frame

`cv2.inRange(hsv, lower_hsv, upper_hsv)` creates a binary mask.

### 6. Clean mask

Morphological ops remove noise and fill small gaps.

### 7. Find contours

Each blob corresponds to an instance of the object.

### 8. Draw bounding boxes

Contours → boundingRect → rectangle on original frame.

---

## ⚙️ Configuration

You can adjust these parameters:

| Parameter                          | Meaning                                 |
| ---------------------------------- | --------------------------------------- |
| `s_thresh`                         | Minimum saturation (ignore gray pixels) |
| `v_thresh`                         | Minimum value (ignore dark pixels)      |
| `lower_perc`                       | Lower percentile for color cluster      |
| `upper_perc`                       | Upper percentile                        |
| `h_margin`, `s_margin`, `v_margin` | Safety margins                          |
| `min_area`                         | Smallest allowed object contour         |
| `max_objects`                      | Limit on number of objects tracked      |

---

## 📌 Limitations

* Works best for **distinctive colored objects**
* Not suitable for objects defined by texture or shape only
* Lighting changes can still affect detection (minimized but not eliminated)


