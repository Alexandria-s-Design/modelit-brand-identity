# ModelIt K12 Brand Identity - Automated Generation System

Complete brand identity automation for ModelIt K12 using Make.com, PowerPoint, and Nano Banana image generation.

## 🎨 What This System Generates

### ✅ Already Generated
1. **Color Palette** - Professional PowerPoint with all 6 brand colors (HEX/RGB/CMYK codes)
2. **PowerPoint Templates** - 4 slide templates for conferences and webinars

### 🚀 Ready to Generate
3. **Visual Assets** - 20 branded images (molecular structures, networks, cell imagery)
4. **Micro Mayhem Mascot** - 10 character poses for educational materials
5. **TPT Covers** - Branded cover templates for Teachers Pay Teachers products
6. **Graphic Library** - Header banners, icons, social media covers
7. **Style Guide PDF** - Complete brand guidelines document

## 📁 Directory Structure

```
modelit-brand-identity/
├── scripts/
│   ├── brand_constants.py              # Brand specifications
│   ├── generate_color_palette.py       # ✅ Color palette generator
│   ├── generate_ppt_templates.py       # ✅ PowerPoint templates
│   ├── generate_visual_assets.py       # Visual assets (Nano Banana)
│   ├── generate_mascot.py              # Mascot generator (Nano Banana)
│   └── generate_all_brand_assets.py    # Master automation script
├── assets/
│   ├── colors/
│   │   └── modelit_color_palette.pptx  # ✅ Generated
│   ├── templates/
│   │   └── modelit_presentation_templates.pptx  # ✅ Generated
│   ├── visuals/                        # Visual assets (to be generated)
│   ├── mascot/                         # Mascot variations (to be generated)
│   ├── tpt_covers/                     # TPT covers (to be generated)
│   └── graphics/                       # Graphic library (to be generated)
└── docs/
    └── (Style guide PDF will go here)
```

## 🚀 Quick Start

### Generate Everything (Demo Mode - 13 images, ~$0.51)
```bash
python scripts/generate_all_brand_assets.py
```

### Generate Everything (Full Mode - 30 images, ~$1.17)
```bash
python scripts/generate_all_brand_assets.py --mode=full
```

### Generate Individual Assets

**Color Palette (Free)**
```bash
python scripts/generate_color_palette.py
```

**PowerPoint Templates (Free)**
```bash
python scripts/generate_ppt_templates.py
```

**Visual Assets - Demo (8 images, ~$0.31)**
```bash
python scripts/generate_visual_assets.py
```

**Visual Assets - Full (20 images, ~$0.78)**
```bash
python scripts/generate_visual_assets.py all
```

**Mascot - Demo (5 poses, ~$0.20)**
```bash
python scripts/generate_mascot.py
```

## 🎨 Brand Colors

- **Primary Dark Blue**: `#1F4E79` - Headings, professional materials
- **Primary Light Blue**: `#0078D7` - Accents, CTAs, interactive elements
- **Secondary Navy**: `#2B2B40` - Secondary text, borders
- **Background Light**: `#F2F6FA` - Backgrounds, light sections
- **Accent Teal**: `#009999` - Science themes, molecular diagrams
- **Accent Gold**: `#FFC857` - Highlights, important notes

## 🤖 Technology Stack

- **PowerPoint Automation**: `python-pptx` library
- **Image Generation**: Nano Banana (Gemini 2.5 Flash Image) via OpenRouter
- **Workflow Automation**: Make.com (MCP integration ready)
- **Social Media**: Ayrshare (12 platforms)

## 💰 Cost Breakdown

| Asset Type | Quantity | Cost per | Total |
|------------|----------|----------|-------|
| Color Palette | 1 file | Free | $0.00 |
| PPT Templates | 4 slides | Free | $0.00 |
| Visual Assets (Demo) | 8 images | $0.039 | $0.31 |
| Visual Assets (Full) | 20 images | $0.039 | $0.78 |
| Mascot (Demo) | 5 poses | $0.039 | $0.20 |
| Mascot (Full) | 10 poses | $0.039 | $0.39 |
| **Total (Demo)** | | | **$0.51** |
| **Total (Full)** | | | **$1.17** |

## 🔧 Requirements

```bash
pip install python-pptx requests
```

**Environment Variables** (in `/workspace/.env`):
- `OPENROUTER_API_KEY` - For Nano Banana image generation

## 📦 Integration with Make.com

The system is designed to integrate with Make.com for full automation:

1. **Trigger**: Webhook or schedule
2. **Generate Assets**: Run Python scripts via HTTP module
3. **Upload to Google Drive**: Store organized by asset type
4. **Share on Social**: Post samples via Ayrshare
5. **Notify Team**: Send summary via Slack/email

See `/docs/MAKE-COM-INTEGRATION.md` for scenario setup (coming soon).

## 🎯 Next Steps

1. ✅ Test color palette and templates (completed)
2. ⏭️ Generate visual assets in demo mode
3. ⏭️ Generate mascot variations
4. ⏭️ Create Make.com automation scenario
5. ⏭️ Build style guide PDF compiler
6. ⏭️ Upload all assets to Google Drive

## 📊 Brand Identity Deliverables

- [x] Color palette with HEX/RGB/CMYK codes
- [x] 4 PowerPoint slide templates
- [ ] 20 branded visual assets
- [ ] 10 Micro Mayhem mascot poses
- [ ] TPT cover template
- [ ] Social media graphics (FB, Twitter, LinkedIn, YouTube)
- [ ] Icon library (12 topics)
- [ ] Complete brand style guide PDF

## 🔗 Related Projects

- **TPT Automation**: `/workspace/projects/tpt-automation/`
- **Teachers Pay Teachers**: `/workspace/projects/modelit-teachers-pay-teachers/`
- **Dissemination Plan**: `Alexandria-s-Design/dissemination-plan`

## 📝 License

Proprietary - Alexandria's Design / ModelIt K12

## 🎓 About ModelIt K12

**Mission**: Systems Thinking for Tomorrow's Scientists

ModelIt K12 empowers middle school students (grades 5-8) with computational modeling and systems thinking through NGSS-aligned curricula and Cell Collective integration.

---

**Generated**: 2025-11-17
**Status**: Phase 1 Complete (Color Palette + Templates Generated)
**Next**: Phase 2 - Image Generation

## Status
Active

## TODO
- [ ] Update with latest content
- [ ] Optimize asset organization
- [ ] Add metadata documentation