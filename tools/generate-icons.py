"""Generate the Crossed Threads PWA icon set.

Run from the repository root:
    python tools/generate-icons.py

Produces:
    icons/icon-192.png, icons/icon-512.png              (purpose: any)
    icons/icon-maskable-192.png, ...-512.png            (purpose: maskable, safe zone)
    icons/apple-touch-icon.png                          (180x180, opaque)
    icons/favicon-32.png
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

MASTER = 1024
BG_TOP = (208, 139, 76)      # warm highlight
BG_BOTTOM = (138, 74, 30)    # deep leather
INK = (250, 247, 242)
SHADOW = (104, 54, 22)

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"


def gradient_canvas():
    img = Image.new("RGB", (MASTER, MASTER))
    draw = ImageDraw.Draw(img)
    for y in range(MASTER):
        t = y / (MASTER - 1)
        color = tuple(round(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOTTOM))
        draw.line([(0, y), (MASTER, y)], fill=color)

    # Soft top-left glow for depth.
    overlay = Image.new("RGBA", (MASTER, MASTER), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse(
        [-MASTER * 0.28, -MASTER * 0.38, MASTER * 0.78, MASTER * 0.66],
        fill=(255, 255, 255, 30),
    )
    overlay = overlay.filter(ImageFilter.GaussianBlur(MASTER // 10))
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def draw_crossed_needles(img, span_ratio, width_ratio):
    d = ImageDraw.Draw(img)
    c = MASTER / 2
    reach = MASTER * span_ratio / 2  # axis offset from centre
    width = max(4, round(MASTER * width_ratio))
    r = width / 2

    def stroke(p1, p2, color):
        d.line([p1, p2], fill=color, width=width)
        d.ellipse([p1[0] - r, p1[1] - r, p1[0] + r, p1[1] + r], fill=color)
        d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=color)

    # Subtle drop shadow so the mark reads on light home-screen wallpapers.
    offset = MASTER * 0.006
    shadow = (SHADOW[0], SHADOW[1], SHADOW[2])
    stroke((c - reach + offset, c - reach + offset), (c + reach + offset, c + reach + offset), shadow)
    stroke((c + reach + offset, c - reach + offset), (c - reach + offset, c + reach + offset), shadow)

    stroke((c - reach, c - reach), (c + reach, c + reach), INK)
    stroke((c + reach, c - reach), (c - reach, c + reach), INK)

    # Needle eyes: small warm dots at the two upper tips, like the in-app mark.
    eye_r = width * 0.17
    for x in (c - reach, c + reach):
        y = c - reach
        d.ellipse([x - eye_r, y - eye_r, x + eye_r, y + eye_r], fill=BG_BOTTOM)
    return img


def main():
    ICONS.mkdir(exist_ok=True)
    base = gradient_canvas()
    standard = draw_crossed_needles(base.copy(), span_ratio=0.72, width_ratio=0.072)
    maskable = draw_crossed_needles(base.copy(), span_ratio=0.56, width_ratio=0.058)

    standard.resize((192, 192), Image.LANCZOS).save(ICONS / "icon-192.png", optimize=True)
    standard.resize((512, 512), Image.LANCZOS).save(ICONS / "icon-512.png", optimize=True)
    maskable.resize((192, 192), Image.LANCZOS).save(ICONS / "icon-maskable-192.png", optimize=True)
    maskable.resize((512, 512), Image.LANCZOS).save(ICONS / "icon-maskable-512.png", optimize=True)
    standard.resize((180, 180), Image.LANCZOS).save(ICONS / "apple-touch-icon.png", optimize=True)
    standard.resize((32, 32), Image.LANCZOS).save(ICONS / "favicon-32.png", optimize=True)
    print("Icons written to", ICONS)


if __name__ == "__main__":
    main()
