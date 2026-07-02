#!/usr/bin/env python3
"""
Génère les visuels de DÉMONSTRATION (placeholders SVG) du site.
L'artiste remplacera ces fichiers par ses vraies photos (mêmes noms de fichiers,
ou change les chemins dans index.html). Voir GUIDE-PERSONNALISATION.md.

Lancer :  python3 scripts/generate-placeholders.py
"""
import os, math

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
os.makedirs(OUT, exist_ok=True)

# Palettes douces, cohérentes avec la charte (crème / nude / rose / prune / or)
PALETTES = [
    ("#F3E3DA", "#C98A8A"),  # crème -> rose poudré
    ("#E9D8CE", "#6E4555"),  # nude -> prune
    ("#F1E7DF", "#B8933F"),  # sable -> or
    ("#EAD9D3", "#8A5B6B"),  # rosé -> mauve
    ("#E7DAD0", "#A9776B"),  # taupe -> terracotta doux
    ("#F4E9E2", "#C9AE9E"),  # crème -> nude
    ("#E6DBD6", "#734B5E"),  # gris rosé -> prune
    ("#F0E1D6", "#C08552"),  # sable chaud -> caramel
]

def nail_hand(cx, cy, base, accent, style):
    """Dessine un motif abstrait d'ongles/nail-art (5 'ongles' stylisés)."""
    els = []
    # arc de 5 ongles en éventail
    for i in range(5):
        ang = math.radians(-58 + i * 29)
        r = 78 + (0 if i in (0,4) else (10 if i in (1,3) else 16))
        x = cx + math.cos(ang) * 120
        y = cy + math.sin(ang) * 120
        rot = math.degrees(ang) + 90
        deco = ""
        if style == 0:   # French : pointe claire
            deco = f'<rect x="-13" y="-{r}" width="26" height="12" rx="6" fill="#ffffff" opacity="0.9"/>'
        elif style == 1: # points dorés
            deco = f'<circle cx="0" cy="-{r-14}" r="4.5" fill="#B8933F"/><circle cx="0" cy="-{r-30}" r="3" fill="#ffffff" opacity=".85"/>'
        elif style == 2: # dégradé accent
            deco = f'<rect x="-13" y="-{r}" width="26" height="{r*0.5:.0f}" rx="13" fill="{accent}" opacity="0.55"/>'
        else:            # ligne fine
            deco = f'<line x1="0" y1="-{r-6}" x2="0" y2="-18" stroke="#ffffff" stroke-width="2" opacity=".7"/>'
        els.append(
            f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})">'
            f'<rect x="-13" y="-{r}" width="26" height="{r+16}" rx="13" '
            f'fill="url(#nailgrad)" stroke="#ffffff" stroke-opacity=".5" stroke-width="1"/>'
            f'{deco}</g>'
        )
    return "".join(els)

def make_svg(w, h, base, accent, style, label=""):
    cx, cy = w/2, h/2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Photo de nail art (démonstration)">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{base}"/>
      <stop offset="1" stop-color="{accent}"/>
    </linearGradient>
    <linearGradient id="nailgrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/>
      <stop offset="1" stop-color="{base}"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="38%" r="70%">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#glow)"/>
  <g opacity="0.96">{nail_hand(cx, cy, base, accent, style)}</g>
  <circle cx="{w*0.16:.0f}" cy="{h*0.2:.0f}" r="5" fill="#ffffff" opacity=".5"/>
  <circle cx="{w*0.82:.0f}" cy="{h*0.78:.0f}" r="7" fill="#B8933F" opacity=".55"/>
  <text x="{w-16}" y="{h-14}" text-anchor="end" font-family="Georgia, serif" font-size="{max(11,w//34)}" fill="#2B2422" opacity="0.32">{label}</text>
</svg>'''

def blob(color, size=340):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 340 340">
  <path fill="{color}" d="M282,190Q262,240,214,268Q166,296,116,272Q66,248,48,196Q30,144,62,100Q94,56,148,44Q202,32,246,66Q290,100,290,145Q290,190,282,190Z"/>
</svg>'''

def portrait(w, h, base, accent, label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Portrait (démonstration)">
  <defs>
    <linearGradient id="pg" x1="0" y1="0" x2="0.7" y2="1">
      <stop offset="0" stop-color="{base}"/><stop offset="1" stop-color="{accent}"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#pg)"/>
  <g fill="#2B2422" opacity="0.18">
    <circle cx="{w/2}" cy="{h*0.4}" r="{w*0.20}"/>
    <path d="M{w*0.18},{h} Q{w*0.5},{h*0.55} {w*0.82},{h} Z"/>
  </g>
  <circle cx="{w*0.5}" cy="{h*0.4}" r="{w*0.205}" fill="none" stroke="#ffffff" stroke-opacity=".5" stroke-width="2"/>
  <text x="{w/2}" y="{h-22}" text-anchor="middle" font-family="Georgia, serif" font-size="{w//20}" fill="#ffffff" opacity="0.85">{label}</text>
</svg>'''

# ---- Galerie : 12 tuiles + catégories ----
gallery = [
    ("gel", "Pose gel"), ("nailart", "Nail art fleuri"), ("french", "French moderne"),
    ("nailart", "Chrome miroir"), ("gel", "Babyboomer"), ("entretien", "Remplissage"),
    ("nailart", "Ongles bijoux"), ("french", "French couleur"), ("gel", "Semi-permanent"),
    ("nailart", "Marbre & or"), ("entretien", "Manucure russe"), ("french", "Micro-French"),
]
for i, (cat, name) in enumerate(gallery):
    base, accent = PALETTES[i % len(PALETTES)]
    style = i % 4
    svg = make_svg(700, 700, base, accent, style, name)
    with open(os.path.join(OUT, f"galerie-{i+1:02d}.svg"), "w") as f:
        f.write(svg)

# ---- Hero + portrait à propos ----
with open(os.path.join(OUT, "hero.svg"), "w") as f:
    f.write(make_svg(800, 1000, "#EAD9D3", "#6E4555", 1, "Nail Art"))
with open(os.path.join(OUT, "portrait.svg"), "w") as f:
    f.write(portrait(700, 900, "#C9AE9E", "#6E4555", "Votre portrait"))

# ---- Blobs décoratifs du hero ----
with open(os.path.join(OUT, "blob-1.svg"), "w") as f:
    f.write(blob("#E9D0C7"))
with open(os.path.join(OUT, "blob-2.svg"), "w") as f:
    f.write(blob("#EBD8C0"))

# ---- Logo (mark) + favicon + image Open Graph ----
logo = '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80">
  <defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#6E4555"/><stop offset="1" stop-color="#C98A8A"/>
  </linearGradient></defs>
  <rect width="80" height="80" rx="20" fill="url(#lg)"/>
  <g transform="translate(40,44)">
    <rect x="-6" y="-26" width="12" height="34" rx="6" fill="#FBF7F4"/>
    <rect x="-6" y="-26" width="12" height="11" rx="6" fill="#B8933F"/>
    <ellipse cx="0" cy="14" rx="15" ry="6" fill="#FBF7F4" opacity="0.55"/>
  </g>
</svg>'''
with open(os.path.join(OUT, "logo.svg"), "w") as f:
    f.write(logo)
with open(os.path.join(OUT, "favicon.svg"), "w") as f:
    f.write(logo)

og = make_svg(1200, 630, "#EAD9D3", "#6E4555", 1, "")
og = og.replace('</svg>',
    '<text x="60" y="330" font-family="Georgia, serif" font-size="86" fill="#2B2422">L’Atelier Nacré</text>'
    '<text x="62" y="392" font-family="Arial, sans-serif" font-size="30" fill="#6E4555" letter-spacing="4">NAIL ART &amp; BEAUTÉ DES ONGLES</text></svg>')
with open(os.path.join(OUT, "og-image.svg"), "w") as f:
    f.write(og)

print("Placeholders générés dans assets/images :", len(os.listdir(OUT)), "fichiers")
