#!/usr/bin/env python3
"""Build paper/phoenix-experiment-paper.pdf from paper/phoenix-experiment-paper.md.

Usage:  python3 paper/build_pdf.py
Needs:  reportlab (pip install reportlab)

Handles the Markdown subset used by the paper: YAML front matter, #/##/### headings,
paragraphs, **bold**, *italic*, `code`, pipe tables, a bold "Table N." caption line
before each table, and numbered lists.
"""
import re
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (KeepTogether, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle)

HERE = Path(__file__).resolve().parent
SRC = HERE / "phoenix-experiment-paper.md"
OUT = HERE / "phoenix-experiment-paper.pdf"

BLUE = colors.HexColor("#1f4e8c")
BASE = dict(fontName="Helvetica", fontSize=9.5, leading=13.2)
S = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=15, leading=19,
                            alignment=TA_CENTER, spaceAfter=6),
    "author": ParagraphStyle("author", **{**BASE, "fontSize": 10.5}, alignment=TA_CENTER),
    "date": ParagraphStyle("date", **BASE, alignment=TA_CENTER, textColor=BLUE, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                         spaceBefore=10, spaceAfter=5, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName="Helvetica-BoldOblique", fontSize=10.5, leading=14,
                         spaceBefore=6, spaceAfter=3, keepWithNext=1),
    "body": ParagraphStyle("body", **BASE, alignment=TA_JUSTIFY, spaceAfter=6),
    "caption": ParagraphStyle("caption", **BASE, spaceBefore=2, spaceAfter=5),
    # Long URLs cannot be hyphenated; left-align those paragraphs to avoid wide gaps.
    "body_url": ParagraphStyle("body_url", **BASE, spaceAfter=6),
    "cell": ParagraphStyle("cell", **{**BASE, "fontSize": 9, "leading": 11.5}),
    "item": ParagraphStyle("item", **BASE, alignment=TA_JUSTIFY, leftIndent=16,
                           bulletIndent=2, spaceAfter=4),
}


def inline(text: str) -> str:
    """Markdown inline markup -> ReportLab paragraph markup."""
    t = escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r'<font face="Courier">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    # Helvetica (WinAnsi) has no right arrow; take it from the Symbol font.
    t = t.replace("→", '<font face="Symbol">→</font>')
    return t


def make_table(rows, width):
    header, body = rows[0], rows[1:]
    ncol = len(header)
    if ncol == 2:
        widths = [width * 0.48, width * 0.52]
    else:
        # Each column is at least as wide as its longest word (so words never break);
        # the remaining width goes to columns in proportion to their longest cell.
        cs = S["cell"]
        def word_w(cell):
            return max(stringWidth(w, cs.fontName, cs.fontSize) for w in (cell.split() or [""]))
        minw = [max(word_w(r[i]) for r in rows) + 16 for i in range(ncol)]
        longest = [max(stringWidth(r[i], cs.fontName, cs.fontSize) for r in rows) + 16
                   for i in range(ncol)]
        extra = [max(l - m, 0) for l, m in zip(longest, minw)]
        spare = width - sum(minw)
        widths = [m + (spare * e / sum(extra) if sum(extra) else spare / ncol)
                  for m, e in zip(minw, extra)]
    data = [[Paragraph(inline(c), S["cell"]) for c in r] for r in [header] + body]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#7f7f7f")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def build():
    text = SRC.read_text(encoding="utf-8")
    meta = {}
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
        text = text[m.end():]

    doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=2.2 * cm, rightMargin=2.2 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm,
                            title=meta.get("title", ""), author=meta.get("author", ""))
    width = doc.width
    blocks = [b.strip("\n") for b in re.split(r"\n\s*\n", text) if b.strip()]
    story, pending_caption, seen_title = [], None, False
    after_title = []  # author/date lines directly after the H1

    for b in blocks:
        lines = b.splitlines()
        if b.startswith("# "):
            story.append(Paragraph(inline(b[2:].strip()), S["title"]))
            seen_title, after_title = True, ["author", "date"]
        elif after_title and not b.startswith("#"):
            story.append(Paragraph(inline(b), S[after_title.pop(0)]))
        elif b.startswith("## "):
            after_title = []
            story.append(Paragraph(inline(b[3:].strip()), S["h2"]))
        elif b.startswith("### "):
            story.append(Paragraph(inline(b[4:].strip()), S["h3"]))
        elif all(l.lstrip().startswith("|") for l in lines):
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
            rows = [r for r in rows if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
            items = [pending_caption] if pending_caption else []
            items.append(make_table(rows, width))
            story.append(KeepTogether(items))
            story.append(Spacer(1, 8))
            pending_caption = None
        elif re.match(r"\*\*Table \d+\.\*\*", b):
            pending_caption = Paragraph(inline(b), S["caption"])
        elif re.match(r"\d+\. ", b):
            num, _, rest = b.partition(" ")
            story.append(Paragraph(inline(rest), S["item"], bulletText=num))
        else:
            para = " ".join(l.strip() for l in lines)
            story.append(Paragraph(inline(para), S["body_url" if "https://" in para else "body"]))

    if not seen_title:
        raise SystemExit("no '# ' title found")
    doc.build(story)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
