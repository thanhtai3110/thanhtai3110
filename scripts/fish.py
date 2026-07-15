import os
 
os.makedirs("dist", exist_ok=True)
 
svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="220" viewBox="0 0 900 220">
<defs>
  <linearGradient id="ocean" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0d1b2a"/>
    <stop offset="55%" stop-color="#0e3a5f"/>
    <stop offset="100%" stop-color="#08243d"/>
  </linearGradient>
</defs>
 
<!-- Nền biển -->
<rect width="100%" height="100%" fill="url(#ocean)"/>
 
<!-- Lớp sóng xa (chậm, mờ) -->
<path fill="#1e6091" opacity="0.35">
  <animate
    attributeName="d"
    dur="6s"
    repeatCount="indefinite"
    values="
      M0,190 Q225,170 450,190 T900,190 V220 H0 Z;
      M0,190 Q225,210 450,190 T900,190 V220 H0 Z;
      M0,190 Q225,170 450,190 T900,190 V220 H0 Z"/>
</path>
 
<!-- Lớp sóng gần (nhanh, rõ hơn) -->
<path fill="#2a9df4" opacity="0.45">
  <animate
    attributeName="d"
    dur="4s"
    repeatCount="indefinite"
    values="
      M0,200 Q225,185 450,200 T900,200 V220 H0 Z;
      M0,200 Q225,215 450,200 T900,200 V220 H0 Z;
      M0,200 Q225,185 450,200 T900,200 V220 H0 Z"/>
</path>
 
<text x="40" y="40" fill="white" font-size="26" font-family="Arial">
GitHub Fish
</text>
 
<!-- Cá -->
<g>
<animateTransform
  attributeName="transform"
  type="translate"
  values="-120 0;950 0"
  dur="8s"
  repeatCount="indefinite"/>
<!-- Thân -->
<ellipse cx="160" cy="120" rx="55" ry="30" fill="#14b8ff"/>
<!-- Đuôi -->
<polygon points="105,120 65,95 65,145" fill="#14b8ff">
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="-15 105 120;15 105 120;-15 105 120"
    dur="0.4s"
    repeatCount="indefinite"/>
</polygon>
<!-- Mắt -->
<circle cx="190" cy="112" r="4" fill="white"/>
<circle cx="190" cy="112" r="2" fill="black"/>
<!-- Bong bóng -->
<circle cx="235" cy="100" r="5"
  fill="none"
  stroke="#9ddcff"
  stroke-width="2">
  <animate
    attributeName="cy"
    values="100;20"
    dur="2s"
    repeatCount="indefinite"/>
  <animate
    attributeName="opacity"
    values="1;0"
    dur="2s"
    repeatCount="indefinite"/>
</circle>
<circle cx="255" cy="85" r="8"
  fill="none"
  stroke="#9ddcff"
  stroke-width="2">
  <animate
    attributeName="cy"
    values="85;5"
    dur="2.5s"
    repeatCount="indefinite"/>
  <animate
    attributeName="opacity"
    values="1;0"
    dur="2.5s"
    repeatCount="indefinite"/>
</circle>
</g>
</svg>
"""
 
output_path = os.path.join("dist", "github-contribution-grid-fish.svg")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg)
 
print(f"Đã tạo file: {output_path}")
