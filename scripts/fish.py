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
<path fill="#1e6091" opacity="0.35"
  d="M0,190 Q225,170 450,190 T900,190 V220 H0 Z">
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
<path fill="#2a9df4" opacity="0.45"
  d="M0,200 Q225,185 450,200 T900,200 V220 H0 Z">
  <animate
    attributeName="d"
    dur="4s"
    repeatCount="indefinite"
    values="
      M0,200 Q225,185 450,200 T900,200 V220 H0 Z;
      M0,200 Q225,215 450,200 T900,200 V220 H0 Z;
      M0,200 Q225,185 450,200 T900,200 V220 H0 Z"/>
</path>
 
<!-- Cá mập dữ tợn -->
<g>
<animateTransform
  attributeName="transform"
  type="translate"
  values="-180 0;950 0"
  dur="8s"
  repeatCount="indefinite"/>
 
<!-- Thân (thon dài, mũi nhọn, màu đỏ) -->
<path fill="#c62828"
  d="M0,120
     C20,92 60,76 120,76
     C172,76 208,93 228,110
     L233,120
     L228,130
     C208,147 172,164 120,164
     C60,164 20,148 0,120 Z"/>
 
<!-- Bụng sáng màu -->
<path fill="#ffe0d6"
  d="M18,130
     C55,152 110,160 150,154
     C120,163 55,159 18,138 Z"/>
 
<!-- Đuôi chẻ đôi -->
<g>
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="-12 5 120;12 5 120;-12 5 120"
    dur="0.5s"
    repeatCount="indefinite"/>
  <polygon points="5,120 -48,82 -30,118" fill="#c62828"/>
  <polygon points="5,120 -48,158 -30,122" fill="#8e1c1c"/>
</g>
 
<!-- Vây lưng -->
<polygon points="92,78 118,25 152,79" fill="#8e1c1c"/>
 
<!-- Vây ngực -->
<polygon points="145,142 170,180 190,144" fill="#8e1c1c"/>
 
<!-- Mang -->
<path d="M172,92 L169,118" stroke="#7a1414" stroke-width="2" fill="none"/>
<path d="M184,90 L181,120" stroke="#7a1414" stroke-width="2" fill="none"/>
<path d="M196,89 L193,122" stroke="#7a1414" stroke-width="2" fill="none"/>
 
<!-- Miệng mở, răng nhọn -->
<path fill="#5c0f0f"
  d="M195,120 C205,132 205,145 195,150
     C170,158 130,158 108,150
     C100,146 100,124 108,120
     C130,112 170,112 195,120 Z"/>
<!-- Răng hàm trên -->
<polygon points="118,120 124,132 130,120" fill="white"/>
<polygon points="132,120 138,133 144,120" fill="white"/>
<polygon points="146,121 152,133 158,121" fill="white"/>
<polygon points="160,121 166,132 172,121" fill="white"/>
<polygon points="174,121 179,131 184,121" fill="white"/>
<!-- Răng hàm dưới -->
<polygon points="118,150 124,138 130,150" fill="white"/>
<polygon points="132,150 138,137 144,150" fill="white"/>
<polygon points="146,150 152,138 158,150" fill="white"/>
<polygon points="160,149 166,138 172,149" fill="white"/>
<polygon points="174,148 179,138 184,148" fill="white"/>
 
<!-- Lông mày dữ tợn -->
<polygon points="188,90 216,86 210,98" fill="#5c0f0f"/>
 
<!-- Mắt (nheo lại, giận dữ) -->
<path d="M195,100 Q207,94 218,100 Q207,106 195,100 Z" fill="white"/>
<circle cx="208" cy="100" r="3.2" fill="black"/>
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
 
