#!/usr/bin/env python3
"""Render the 19 Nov 2026 world-news front page (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont
from math import sin, cos, pi

W = H = 1024
PAPER = (246, 242, 232)
INK = (28, 32, 44)
NAVY = (23, 42, 76)
RED = (176, 40, 40)
GOLD = (198, 152, 58)
TEAL = (36, 96, 100)
GREY = (110, 114, 124)
LINE = (208, 202, 188)

B  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f_mast   = ImageFont.truetype(B, 66)
f_date   = ImageFont.truetype(B, 40)
f_head   = ImageFont.truetype(B, 25)
f_sub    = ImageFont.truetype(R, 18)
f_ed     = ImageFont.truetype(R, 16)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def ctext(x, y, s, f, fill, anchor="mm"):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor)

# ---- masthead ----
d.rectangle([0, 0, W, 26], fill=NAVY)
ctext(W/2, 13, "AGENT PRESS  ·  ONE-DAY WORLD EDITION", ImageFont.truetype(R, 14), (230, 228, 218))
ctext(W/2, 78, "THE WORLD IN ONE DAY", f_mast, INK)
ctext(W/2, 128, "THURSDAY · 19 NOVEMBER 2026", f_date, RED)
d.line([40, 158, W-40, 158], fill=INK, width=3)

# ---- panel grid ----
GX, GY, PW, PH, GAP = 40, 178, 462, 260, 16
def panel(cx, cy):
    x0, y0 = GX + cx*(PW+GAP), GY + cy*(PH+GAP)
    d.rectangle([x0, y0, x0+PW, y0+PH], outline=LINE, width=2)
    d.rectangle([x0, y0, x0+PW, y0+56], fill=NAVY)
    return x0, y0

def label(x0, y0, head, sub):
    ctext(x0+PW/2, y0+28, head, f_head, (246,242,232))
    ctext(x0+PW/2, y0+PH-20, sub, f_sub, GREY)

def silhouette(x, y, s, col):
    d.ellipse([x-s*0.28, y-s, x+s*0.28, y-s*0.35], fill=col)
    d.polygon([(x-s*0.5, y+s*0.6), (x-s*0.38, y-s*0.25), (x-s*0.1, y-s*0.4),
               (x+s*0.1, y-s*0.4), (x+s*0.38, y-s*0.25), (x+s*0.5, y+s*0.6)], fill=col)

# P1: trilateral summit
x0, y0 = panel(0, 0)
label(x0, y0, "FIRST TRUMP-PUTIN-XI SUMMIT", "Trilateral meeting · Shenzhen, China")
by = y0+126
for i, col in enumerate([(160,60,54), (60,90,160), (190,160,60)]):
    silhouette(x0+116+i*115, by, 44, col)
d.line([x0+116, by+60, x0+346, by+60], fill=GREY, width=4)

# P2: Iran strikes / oil
x0, y0 = panel(1, 0)
label(x0, y0, "US WEIGHS NEW IRAN STRIKES", "Brent crude climbs to $93")
bx, by = x0+110, y0+96
d.rounded_rectangle([bx, by, bx+110, by+96], radius=12, fill=(96,102,112), outline=INK, width=3)
for yy in (by+32, by+64):
    d.line([bx+6, yy, bx+104, yy], fill=INK, width=4)
cx, cy = bx+55, by-16
d.polygon([(cx-12,cy+22),(cx+2,cy-6),(cx-2,cy-6),(cx+12,cy+22)], fill=(226,120,40))
d.ellipse([cx-16, cy+12, cx+16, cy+36], fill=(238,150,60))
ctext(x0+370, y0+130, "$93", ImageFont.truetype(B, 44), RED)

# P3: Kerch bridge
x0, y0 = panel(0, 1)
label(x0, y0, "KERCH BRIDGE STRUCK AGAIN", "Ukraine hit the span for a second day")
by = y0+118
d.rectangle([x0+40, by+50, x0+422, by+70], fill=(74,118,138))
for k in range(4):
    px = x0+85+k*88
    d.arc([px, by-16, px+76, by+52], 180, 360, fill=GREY, width=7)
d.arc([x0+260, by-16, x0+336, by+52], 205, 320, fill=RED, width=7)
d.line([x0+268, by+2, x0+312, by+40], fill=RED, width=7)
d.ellipse([x0+150, by-56, x0+182, by-24], fill=(238,150,60))

# P4: Anthropic IPO
x0, y0 = panel(1, 1)
label(x0, y0, "ANTHROPIC'S RECORD IPO", "Priced at $83 · biggest share sale ever")
pts = [(x0+60, y0+185), (x0+130, y0+150), (x0+200, y0+162), (x0+265, y0+118), (x0+325, y0+88)]
d.line(pts, fill=TEAL, width=6)
x, y = pts[-1]
d.polygon([(x-4, y+18), (x+22, y-10), (x-14, y-12)], fill=TEAL)
for i, (px, py) in enumerate(pts[:-1]):
    d.ellipse([px-6, py-6, px+6, py+6], fill=PAPER, outline=TEAL, width=4)
ctext(x0+392, y0+72, "$81B", ImageFont.truetype(B, 32), TEAL)

# P5: ICJ
x0, y0 = panel(0, 2)
label(x0, y0, "ICJ RULES ON ROHINGYA CASE", "Genocide judgment · The Hague")
cx, cy = x0+231, y0+96
d.line([cx, cy-22, cx, cy+64], fill=INK, width=6)
d.polygon([(cx-16, cy+64), (cx+16, cy+64), (cx, cy+44)], fill=INK)
d.line([cx-120, cy-26, cx+120, cy-26], fill=INK, width=6)
d.line([cx-120, cy-26, cx-120, cy+10], fill=INK, width=5)
d.line([cx+120, cy-26, cx+120, cy+10], fill=INK, width=5)
for sx, sgn in ((cx-120, -1), (cx+120, 1)):
    d.line([sx-24*sgn*0, 0, 0, 0])  # keep simple
    d.rectangle([sx-40, cy+10, sx+40, cy+26], outline=INK, width=5)
d.rectangle([cx-52, cy-44, cx+52, cy-26], fill=GOLD)

# P6: Cyclone
x0, y0 = panel(1, 2)
label(x0, y0, "CYCLONE AKVAN HITS INDIA", "Odisha coastal districts on red alert")
cx, cy = x0+170, y0+140
for r, w, a in ((66, 12, 40), (46, 10, 60), (28, 8, 80)):
    d.arc([cx-r, cy-r, cx+r, cy+r], 180+a, 540+a, fill=TEAL, width=w)
d.arc([cx-84, cy-84, cx+84, cy+84], 250, 420, fill=(140,180,190), width=9)
d.rectangle([x0+280, cy+20, x0+425, cy+46], fill=(212,188,120))
d.rectangle([x0+280, cy-34, x0+330, cy+20], fill=(84,146,96))
ctext(x0+352, cy+66, "BAY OF BENGAL", ImageFont.truetype(R, 15), GREY)

# footer
ctext(W/2, H-24, "Selection: tri-summit Shenzhen · Iran escalation · Kerch bridge · Anthropic IPO · ICJ ruling · Cyclone Akvan",
      ImageFont.truetype(R, 16), GREY)

img.save("/tmp/entry.png", optimize=True)
print("ok", img.size)
