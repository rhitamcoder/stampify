from PIL import Image, ImageDraw, ImageFont

def apply_watermark(image_path, text):
    img = Image.open(image_path).convert("RGBA")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 40)
    except OSError:
        font = ImageFont.load_default()

    img_width, img_height = img.size
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    margin = 20
    x = img_width - text_width - margin
    y = img_height - text_height - margin

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 200))
    return img

# result_img = apply_watermark("", "Test Watermark")
# result_img.show()
