# ModelIt K-12 Brand Identity System

**Version 1.0 | December 2025**

Complete brand identity assets, guidelines, and automation for ModelIt K-12 - Systems Thinking for Tomorrow's Scientists.

## 📚 Brand Documentation

### Core Documents
1. **[BRAND-GUIDELINES.md](BRAND-GUIDELINES.md)** - Complete brand guidelines
2. **[BRAND-ASSETS-REFERENCE.md](BRAND-ASSETS-REFERENCE.md)** - Quick reference for implementation

### Quick Start
- **Designers**: Start with [BRAND-GUIDELINES.md](BRAND-GUIDELINES.md)
- **Developers**: Use [BRAND-ASSETS-REFERENCE.md](BRAND-ASSETS-REFERENCE.md) for code
- **Marketers**: Reference brand voice and messaging sections

---

## 🎨 Brand System

### Colors
- **Primary Dark Blue**: `#1F4E79` - Headings, professional materials
- **Primary Light Blue**: `#0078D7` - CTAs, interactive elements
- **Secondary Navy**: `#2B2B40` - Body text, borders
- **Background Light**: `#F2F6FA` - Backgrounds, sections
- **Accent Teal**: `#009999` - Science themes, diagrams
- **Accent Gold**: `#FFC857` - Highlights, achievements

All colors meet WCAG AA/AAA accessibility standards.

### Typography
- **Headings**: Montserrat (300, 400, 500, 600, 700)
- **Body**: Open Sans (300, 400, 600, 700)
- **Code**: Roboto Mono (400)

All fonts available free via Google Fonts.

### Logo
- Primary horizontal, stacked, icon-only variations
- Monochrome versions for single-color applications
- Minimum sizes and clear space requirements specified

### Brand Voice
- Educational (not academic)
- Approachable (not casual)
- Scientific (not stuffy)
- Empowering (not prescriptive)
- Progressive (not trendy)

---

## 📁 Repository Structure

```
modelit-brand-identity/
├── BRAND-GUIDELINES.md                   # Complete brand guidelines
├── BRAND-ASSETS-REFERENCE.md             # Quick reference guide
├── assets/
│   ├── colors/
│   │   └── modelit_color_palette.pptx    # PowerPoint color palette
│   └── templates/
│       └── modelit_presentation_templates.pptx  # Slide templates
├── scripts/
│   ├── brand_constants.py                # Brand specs as Python
│   ├── generate_color_palette.py         # Generate color assets
│   ├── generate_ppt_templates.py         # Generate slide templates
│   ├── generate_visual_assets.py         # Generate branded images
│   └── generate_all_brand_assets.py      # Generate all assets
└── README.md
```

---

## 🚀 Asset Generation

### Already Generated
✅ Color palette PowerPoint (6 colors with HEX/RGB/CMYK)
✅ PowerPoint slide templates (4 templates)
✅ Brand guidelines documentation

### Available to Generate
- 20 branded visual assets (molecular structures, networks, cell imagery)
- 10 Micro Mayhem mascot variations
- TPT cover templates
- Social media graphics
- Icon library

### Generate Assets

**Prerequisites**:
```bash
pip install python-pptx requests
```

**Environment Variables**:
- `OPENROUTER_API_KEY` - For AI image generation

**Commands**:
```bash
# Generate everything (demo: 13 images, ~$0.51)
python scripts/generate_all_brand_assets.py

# Generate everything (full: 30 images, ~$1.17)
python scripts/generate_all_brand_assets.py --mode=full

# Individual generators
python scripts/generate_color_palette.py       # Free
python scripts/generate_ppt_templates.py       # Free
python scripts/generate_visual_assets.py       # 8 images, ~$0.31
python scripts/generate_visual_assets.py all   # 20 images, ~$0.78
```

---

## 🔧 Implementation Examples

### Website Header
```html
<header style="background: #FFFFFF;">
  <img src="logo.svg" alt="ModelIt K-12" width="200">
  <nav style="font-family: 'Montserrat', sans-serif;">
    <a href="#" style="color: #2B2B40;">Curriculum</a>
  </nav>
</header>
```

### CSS Variables
```css
:root {
  --primary-dark-blue: #1F4E79;
  --primary-light-blue: #0078D7;
  --secondary-navy: #2B2B40;
  --background-light: #F2F6FA;
  --accent-teal: #009999;
  --accent-gold: #FFC857;
}
```

### Primary Button
```css
.btn-primary {
  background: #0078D7;
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  padding: 14px 28px;
  border-radius: 8px;
}
```

---

## 📱 Social Media Specifications

### Profile Pictures (All Platforms)
- Size: 800×800px (2x retina)
- Format: PNG with transparent background
- Content: Icon-only logo

### Cover Photos
| Platform | Size | Safe Area |
|----------|------|-----------|
| Facebook | 820×312px | Center 640×250px |
| Twitter | 1500×500px | Center 1200×400px |
| LinkedIn | 1584×396px | Center 1200×300px |
| YouTube | 2560×1440px | Center 1546×423px |

---

## 🤖 Technology Stack

- **Documentation**: Markdown
- **PowerPoint Automation**: python-pptx
- **Image Generation**: Nano Banana (Gemini 2.5 Flash) via OpenRouter
- **Workflow Automation**: Make.com integration ready
- **Social Media**: Ayrshare (12 platforms)

---

## 💰 Cost Breakdown

| Asset Type | Quantity | Cost per | Total |
|------------|----------|----------|-------|
| Color Palette | 1 file | Free | $0.00 |
| PPT Templates | 4 slides | Free | $0.00 |
| Brand Guidelines | Documentation | Free | $0.00 |
| Visual Assets (Demo) | 8 images | $0.039 | $0.31 |
| Visual Assets (Full) | 20 images | $0.039 | $0.78 |
| Mascot (Demo) | 5 poses | $0.039 | $0.20 |
| Mascot (Full) | 10 poses | $0.039 | $0.39 |
| **Total (Demo)** | | | **$0.51** |
| **Total (Full)** | | | **$1.17** |

---

## 📊 Brand Deliverables Checklist

- [x] Color system with accessibility ratings
- [x] Typography specifications and font pairing
- [x] Logo usage guidelines
- [x] Brand voice and messaging guide
- [x] Social media templates and specs
- [x] Email signature templates
- [x] PowerPoint slide templates
- [x] Complete brand guidelines documentation
- [ ] Logo files (SVG, PNG, AI, EPS)
- [ ] 20 branded visual assets
- [ ] 10 Micro Mayhem mascot poses
- [ ] TPT cover templates
- [ ] Icon library (12 topics)

---

## 🔗 Related Projects

- **TPT Automation**: Educational resource generation
- **Teachers Pay Teachers**: ModelIt curriculum products
- **Dissemination Plan**: Marketing and outreach
- **Cell Collective**: Core technology platform

---

## 📞 Support

**Questions?** cmartin@alexandriasdesign.com

**Need files?** Request complete logo package (all formats and sizes)

**Custom needs?** Contact brand team before creating variations

---

## 📝 License

**ModelIt K-12 Brand Identity System**
© 2025 Alexandria's Design / Discovery Collective

Proprietary and confidential. For authorized ModelIt K-12 team members and partners only.

---

**Status**: ✅ Active - Brand system complete and ready for implementation

**Last Updated**: 2025-12-18

**Version**: 1.0
