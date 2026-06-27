"""
🕷️ pdf_generator.py
Generates a Spider-Man themed Hero ID Card PDF using ReportLab.
"""

import os
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ── Spidey Colour Palette ──
RED       = HexColor("#C0392B")
DARK_RED  = HexColor("#922B21")
BLUE      = HexColor("#1A3A6B")
DARK_BLUE = HexColor("#0D2137")
WEB_GOLD  = HexColor("#F39C12")
WHITE     = HexColor("#FFFFFF")
LIGHT_GRAY= HexColor("#ECF0F1")
DARK_GRAY = HexColor("#2C3E50")
BLACK     = HexColor("#0A0A0A")

OUTPUT_DIR = "generated_pdfs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ────────────────────────────────────────────────
#  DRAWING HELPERS
# ────────────────────────────────────────────────

def draw_web_lines(c, cx, cy, radius, num_spokes=12, num_rings=5):
    """Draw a decorative spider-web pattern."""
    c.saveState()
    c.setStrokeColor(HexColor("#FFFFFF"))
    c.setLineWidth(0.4)
    c.setStrokeAlpha(0.15)

    # Spokes
    for i in range(num_spokes):
        angle = math.radians(i * 360 / num_spokes)
        x_end = cx + radius * math.cos(angle)
        y_end = cy + radius * math.sin(angle)
        c.line(cx, cy, x_end, y_end)

    # Rings
    for r in range(1, num_rings + 1):
        ring_r = radius * r / num_spokes
        points = []
        for i in range(num_spokes):
            angle = math.radians(i * 360 / num_spokes)
            points.append((
                cx + ring_r * math.cos(angle),
                cy + ring_r * math.sin(angle)
            ))
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            c.line(x1, y1, x2, y2)

    c.restoreState()


def draw_spider_silhouette(c, x, y, size):
    """Draw a simple spider icon using circles and lines."""
    c.saveState()
    c.setStrokeColor(WHITE)
    c.setFillColor(WHITE)
    c.setStrokeAlpha(0.6)
    c.setFillAlpha(0.6)

    # Body
    c.circle(x, y, size * 0.35, fill=1)
    c.circle(x, y + size * 0.6, size * 0.25, fill=1)

    # Legs (4 per side)
    c.setLineWidth(size * 0.07)
    leg_angles = [40, 70, 110, 140]
    for angle in leg_angles:
        rad = math.radians(angle)
        # Left legs
        lx1 = x - size * 0.35 * math.cos(math.radians(180 - angle))
        ly1 = y + size * 0.35 * math.sin(math.radians(180 - angle))
        lx2 = lx1 - size * 0.7 * math.cos(rad)
        ly2 = ly1 - size * 0.7 * math.sin(rad)
        c.line(lx1, ly1, lx2, ly2)
        # Right legs
        rx1 = x + size * 0.35 * math.cos(math.radians(180 - angle))
        ry1 = y + size * 0.35 * math.sin(math.radians(180 - angle))
        rx2 = rx1 + size * 0.7 * math.cos(rad)
        ry2 = ry1 - size * 0.7 * math.sin(rad)
        c.line(rx1, ry1, rx2, ry2)

    c.restoreState()


def draw_stat_bar(c, x, y, width, height, value, label, fill_color):
    """Draw a labeled stat progress bar."""
    pct = max(0, min(100, int(value))) / 100.0

    # Background bar
    c.setFillColor(HexColor("#1A1A2E"))
    c.roundRect(x, y, width, height, height / 2, fill=1, stroke=0)

    # Fill bar
    c.setFillColor(fill_color)
    if pct > 0:
        c.roundRect(x, y, width * pct, height, height / 2, fill=1, stroke=0)

    # Label
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(x, y + height + 3, label.upper())

    # Percentage text
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(WHITE)
    c.drawRightString(x + width, y + height + 3, f"{int(pct * 100)}%")


def draw_web_divider(c, x, y, width):
    """Draw a decorative web-thread divider line."""
    c.setStrokeColor(WEB_GOLD)
    c.setLineWidth(0.8)
    # Main line
    c.line(x, y, x + width, y)
    # Small web drops
    for i in range(5):
        drop_x = x + width * (i + 1) / 6
        c.setFillColor(WEB_GOLD)
        c.circle(drop_x, y - 3, 1.5, fill=1, stroke=0)


# ────────────────────────────────────────────────
#  MAIN PDF GENERATOR
# ────────────────────────────────────────────────

def generate_hero_card(data: dict) -> str:
    """Generate a full Spider-Man Hero ID Card PDF and return the file path."""

    name    = data.get("name", "Peter Parker")
    alias   = data.get("alias", "Your Friendly Neighbourhood Hero")
    city    = data.get("city", "New York")
    power   = data.get("power", "Spider-Sense")
    quote   = data.get("quote", "With great power comes great responsibility.")
    str_val = data.get("strength", "85")
    agi_val = data.get("agility", "95")
    int_val = data.get("intelligence", "90")

    safe_name = name.replace(" ", "_").replace("/", "_")
    output_path = os.path.join(OUTPUT_DIR, f"hero_card_{safe_name}.pdf")

    W, H = A4   # 595 x 842 pts
    c = canvas.Canvas(output_path, pagesize=A4)

    # ── PAGE BACKGROUND ──
    c.setFillColor(DARK_BLUE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── HEADER BAND ──
    c.setFillColor(RED)
    c.rect(0, H - 160, W, 160, fill=1, stroke=0)

    # ── DARK RED ACCENT STRIPE ──
    c.setFillColor(DARK_RED)
    c.rect(0, H - 168, W, 8, fill=1, stroke=0)

    # ── WEB DECORATION (background) ──
    draw_web_lines(c, W * 0.85, H - 80, 200)
    draw_web_lines(c, W * 0.1, H * 0.3, 160)
    draw_web_lines(c, W * 0.9, H * 0.55, 130)

    # ── SPIDER SILHOUETTE ──
    draw_spider_silhouette(c, W - 70, H - 70, 28)

    # ── HEADER TITLE ──
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(30, H - 55, "SPIDER-MAN")
    c.setFont("Helvetica", 11)
    c.setFillColor(LIGHT_GRAY)
    c.drawString(30, H - 75, "OFFICIAL HERO IDENTIFICATION CARD")

    # ── SHIELD BADGE SHAPE ──
    c.setFillColor(WEB_GOLD)
    c.setStrokeColor(WHITE)
    c.setLineWidth(1.5)
    badge_x, badge_y = 30, H - 155
    for i in range(0, 360, 45):
        rad = math.radians(i)
        px = badge_x + 18 + 14 * math.cos(rad)
        py = badge_y + 18 + 14 * math.sin(rad)
    c.circle(badge_x + 18, badge_y + 18, 18, fill=1, stroke=1)
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(badge_x + 18, badge_y + 14, "HERO")
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(badge_x + 18, badge_y + 5, "ID")

    # ── CARD NUMBER ──
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 8)
    c.drawRightString(W - 30, H - 148, f"CARD #SP-{abs(hash(name)) % 99999:05d}")

    # ── HERO NAME SECTION ──
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(30, H - 220, name.upper())

    c.setFillColor(WEB_GOLD)
    c.setFont("Helvetica-BoldOblique", 12)
    c.drawString(30, H - 240, f'"{alias}"')

    draw_web_divider(c, 30, H - 255, W - 60)

    # ── INFO GRID ──
    info_y = H - 295
    fields = [
        ("🏙  CITY / BASE",    city),
        ("⚡  PRIMARY POWER",  power),
        ("🕷  AFFILIATION",   "The Avengers · S.H.I.E.L.D"),
        ("📋  STATUS",         "Active · Field Agent"),
    ]

    for i, (label, value) in enumerate(fields):
        col = i % 2
        row = i // 2
        fx = 30 + col * (W / 2 - 10)
        fy = info_y - row * 60

        # Field box
        c.setFillColor(HexColor("#0D1B2A"))
        c.setStrokeColor(HexColor("#C0392B"))
        c.setLineWidth(0.8)
        c.roundRect(fx, fy - 32, W / 2 - 40, 44, 4, fill=1, stroke=1)

        c.setFillColor(WEB_GOLD)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(fx + 8, fy + 5, label)

        c.setFillColor(WHITE)
        c.setFont("Helvetica", 10)
        c.drawString(fx + 8, fy - 14, value)

    # ── STATS SECTION ──
    stats_y = H - 430
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(30, stats_y, "HERO STATS")

    draw_web_divider(c, 30, stats_y - 10, W - 60)

    bar_w = W - 80
    draw_stat_bar(c, 40, stats_y - 45, bar_w, 14, str_val, "Strength",     RED)
    draw_stat_bar(c, 40, stats_y - 80, bar_w, 14, agi_val, "Agility",      WEB_GOLD)
    draw_stat_bar(c, 40, stats_y - 115, bar_w, 14, int_val, "Intelligence", BLUE)

    # ── QUOTE SECTION ──
    quote_y = H - 590
    c.setFillColor(HexColor("#0D1B2A"))
    c.setStrokeColor(WEB_GOLD)
    c.setLineWidth(1)
    c.roundRect(30, quote_y - 50, W - 60, 70, 6, fill=1, stroke=1)

    # Left red accent bar
    c.setFillColor(RED)
    c.rect(30, quote_y - 50, 5, 70, fill=1, stroke=0)

    c.setFillColor(WEB_GOLD)
    c.setFont("Helvetica-BoldOblique", 30)
    c.drawString(44, quote_y + 5, "\u201c")

    # Draw quote text with wrapping
    style = ParagraphStyle(
        "quote",
        fontName="Helvetica-Oblique",
        fontSize=10,
        textColor=LIGHT_GRAY,
        leading=14,
        leftIndent=20,
        rightIndent=10,
    )
    p = Paragraph(quote, style)
    p.wrapOn(c, W - 100, 60)
    p.drawOn(c, 50, quote_y - 38)

    # ── FINGERPRINT / DNA PATTERN DECORATION ──
    c.setStrokeColor(HexColor("#C0392B"))
    c.setStrokeAlpha(0.2)
    c.setLineWidth(0.5)
    for r in range(5, 55, 8):
        c.circle(W - 75, H - 680, r, fill=0, stroke=1)
    c.setStrokeAlpha(1)

    # ── BOTTOM FOOTER BAND ──
    c.setFillColor(RED)
    c.rect(0, 0, W, 60, fill=1, stroke=0)
    c.setFillColor(DARK_RED)
    c.rect(0, 60, W, 6, fill=1, stroke=0)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(W / 2, 38, "MARVEL · AUTHORIZED DOCUMENT · FOR HERO USE ONLY")
    c.setFont("Helvetica", 7)
    c.setFillColor(LIGHT_GRAY)
    c.drawCentredString(W / 2, 22, "Spider-Man PDF Generator  ·  Powered by ReportLab & Flask")

    # ── CORNER WEB DETAILS ──
    c.setStrokeColor(WHITE)
    c.setStrokeAlpha(0.2)
    c.setLineWidth(0.5)
    # Bottom left corner web
    for i in range(4):
        c.arc(0, 0, 40 + i * 15, 40 + i * 15, 0, 90)
    c.setStrokeAlpha(1)

    # ── PAGE 2: WEB SHOOTER MANUAL ──
    c.showPage()

    # BG
    c.setFillColor(DARK_BLUE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Header
    c.setFillColor(RED)
    c.rect(0, H - 80, W, 80, fill=1, stroke=0)
    c.setFillColor(DARK_RED)
    c.rect(0, H - 88, W, 8, fill=1, stroke=0)
    draw_web_lines(c, W * 0.85, H - 40, 150)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, H - 45, f"HERO PROFILE: {name.upper()}")
    c.setFont("Helvetica", 9)
    c.setFillColor(LIGHT_GRAY)
    c.drawString(30, H - 65, "CONFIDENTIAL — S.H.I.E.L.D. DATABASE EXTRACT")

    # Mission Brief
    section_y = H - 130
    sections = [
        ("MISSION BRIEF",
         f"{name} operates primarily out of {city}, defending civilians from "
         f"threats both ordinary and extraordinary. Known for the unique ability "
         f"of {power}, this hero represents the best of what humanity can aspire to."),
        ("PSYCHOLOGICAL PROFILE",
         f"Subject demonstrates exceptional moral fortitude and a deep sense of "
         f"personal responsibility. Despite immense personal sacrifice, {name} "
         f"consistently prioritises the welfare of others above personal gain. "
         f"Risk tolerance: HIGH. Compassion index: MAXIMUM."),
        ("FIELD NOTES",
         f"Operates most effectively in urban environments. Signature style involves "
         f"acrobatic evasion and close-quarters engagement. Web-based utility tools "
         f"allow for rapid traversal and target immobilisation. City of operation: {city}."),
    ]

    for title, body in sections:
        # Section title
        c.setFillColor(WEB_GOLD)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(30, section_y, title)
        draw_web_divider(c, 30, section_y - 8, W - 60)

        # Body text
        body_style = ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=10,
            textColor=colors.HexColor("#ECF0F1"),
            leading=16,
            leftIndent=0,
        )
        bp = Paragraph(body, body_style)
        bp.wrapOn(c, W - 60, 200)
        bp_h = bp.wrap(W - 60, 200)[1]
        bp.drawOn(c, 30, section_y - 20 - bp_h)
        section_y -= bp_h + 55

    # Web pattern decoration page 2
    draw_web_lines(c, 60, 120, 110)
    draw_spider_silhouette(c, W / 2, 110, 40)

    # Footer
    c.setFillColor(RED)
    c.rect(0, 0, W, 50, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W / 2, 30, "MARVEL · AUTHORIZED DOCUMENT · PAGE 2 OF 2")
    c.setFont("Helvetica", 7)
    c.setFillColor(LIGHT_GRAY)
    c.drawCentredString(W / 2, 15, "Generated on-the-fly with Python + ReportLab")

    c.save()
    return output_path
