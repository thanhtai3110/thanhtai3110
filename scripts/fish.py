import os
 
os.makedirs("dist", exist_ok=True)
 
svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="220">
<rect width="100%" height="100%" fill="#0d1117"/>
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
 
# Đây là phần bị thiếu ở bản trước — ghi chuỗi svg ra file thật
output_path = os.path.join("dist", "github-contribution-grid-fish.svg")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg)
 
print(f"Đã tạo file: {output_path}")
 
