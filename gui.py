import logic
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Watermark")
root.geometry("800x600")
root.configure(bg="#193645")

current_image_path = None

def upload_image():
    global current_image_path
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpeg *.jpg *.png")]
    )
    current_image_path = file_path
    return display_image(current_image_path)

def display_image(path):
    img = Image.open(path)
    img.thumbnail((400, 400))
    tk_img = ImageTk.PhotoImage(img)

    image_label.config(image=tk_img)
    image_label.image = tk_img

def apply_watermark_clicked():
    global current_image_path

    if current_image_path is None:
        print("No image uploaded yet.")
        return

    text = watermark_entry.get()
    if text == "":
        print("Please enter watermark text.")
        return

    watermarked_img = logic.apply_watermark(current_image_path, text)

    tk_img = ImageTk.PhotoImage(watermarked_img.resize((400, 400)))
    image_label.config(image=tk_img)
    image_label.image = tk_img

def save_image():
    global current_image_path

    if current_image_path is None:
        print("No image uploaded yet.")
        return

    text = watermark_entry.get()
    if text == "":
        print("Please enter watermark text.")
        return

    watermarked_img = logic.apply_watermark(current_image_path, text)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
    )

    if save_path:
        watermarked_img.save(save_path)
        print(f"Saved to {save_path}")

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=20)

image_label = tk.Label(root, bg="#193645")
image_label.pack(pady=10)

watermark_entry_label = tk.Label(root, text="Watermark Text:", fg="#E4E7EC", bg="#193645")
watermark_entry_label.pack(pady=5)

watermark_entry = tk.Entry(root, font=("Arial", 12))
watermark_entry.pack(pady=10)

apply_btn = tk.Button(root, text="Apply Watermark", command=apply_watermark_clicked)
apply_btn.pack(pady=10)

save_btn = tk.Button(root, text="Save Image", command=save_image)
save_btn.pack(pady=10)

root.mainloop()
