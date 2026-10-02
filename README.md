# 🖋️ Stampify

**A minimal desktop GUI app for adding text watermarks to your images.**

Stampify is a Tkinter-based desktop application that lets you upload an image, type in a watermark, preview it instantly, and save the watermarked result, no browser, no upload to a third-party service, everything runs locally on your machine.

---

## ✨ Features

- 📂 **Upload** JPEG or PNG images via a native file picker
- 🖼️ **Live preview** of your image right in the app window
- 🖋️ **Apply custom watermark text**, rendered in the bottom-right corner with a semi-transparent white overlay
- 💾 **Save** the watermarked result as a PNG or JPEG, with a native save dialog
- 🎨 Clean, minimal dark-themed interface

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** — GUI framework (file dialogs, buttons, image display)
- **Pillow (PIL)** — image loading, watermark drawing, resizing, and saving

---

## 📁 Project Structure

```
stampify/
├── gui.py           # Tkinter interface and event handling
├── logic.py         # Watermarking logic (Pillow image processing)
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites

```
pip install pillow
```

(Tkinter ships with most standard Python installations.)

### Running the App

```
git clone https://github.com/rhitamcoder/stampify.git
```
```
cd stampify
```
```
python gui.py
```

---

1. Click **Upload Image** and select a JPEG or PNG file
2. Type your watermark text into the input field
3. Click **Apply Watermark** to preview it on the image
4. Click **Save Image** to export the watermarked result

---

## 🧠 How It Works

- **`gui.py`** handles the Tkinter window, file dialogs, image preview, and button events
- **`logic.py`** contains `apply_watermark()`, which opens the image with Pillow, calculates text size and positioning (bottom-right corner with a margin), and draws the watermark text with partial transparency
- The watermarked image is re-rendered in the preview on **Apply**, and only written to disk when you click **Save**

---

## ⚠️ Platform Note

`logic.py` attempts to load a specific TrueType font (`DejaVuSans-Bold.ttf`) from a Linux system font path. If that path doesn't exist on your machine (e.g. Windows or macOS), it automatically falls back to Pillow's built-in default font, so the app still works, just with a different watermark font. If you'd like consistent font rendering across platforms, consider bundling a `.ttf` file with the project and loading it by relative path instead.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
