# ModelIt K-12 Brand Assets - Quick Reference

## Colors (Copy-Paste Ready)

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

### Accessible Combinations
| Foreground | Background | Contrast | WCAG Level |
|------------|------------|----------|------------|
| #2B2B40 (Navy) | #FFFFFF (White) | 12.47:1 | AAA - Body text |
| #1F4E79 (Dark Blue) | #FFFFFF (White) | 9.23:1 | AAA - Headings |
| #0078D7 (Light Blue) | #FFFFFF (White) | 4.53:1 | AA - Buttons/CTAs |
| #2B2B40 (Navy) | #FFC857 (Gold) | 7.02:1 | AAA - Callouts |

---

## Typography

### Font Imports
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Open+Sans:wght@300;400;600;700&family=Roboto+Mono:wght@400&display=swap" rel="stylesheet">
```

### Heading Styles
```css
h1 { font-family: 'Montserrat', sans-serif; font-weight: 700; font-size: 48px; color: #1F4E79; }
h2 { font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 36px; color: #1F4E79; }
h3 { font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 28px; color: #2B2B40; }

p { font-family: 'Open Sans', sans-serif; font-weight: 400; font-size: 16px; color: #2B2B40; line-height: 1.6; }
```

### Button Styles
```css
.btn-primary {
  background: #0078D7;
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  font-size: 16px;
  padding: 14px 28px;
  border-radius: 8px;
  border: none;
}
```

---

## Social Media Specs

### Profile Pictures (All Platforms)
- **Size**: 800×800px (2x retina)
- **Format**: PNG with transparent background
- **Content**: Icon only logo

### Cover Photos
| Platform | Size | Safe Area |
|----------|------|-----------|
| Facebook | 820×312px | Center 640×250px |
| Twitter/X | 1500×500px | Center 1200×400px |
| LinkedIn | 1584×396px | Center 1200×300px |
| YouTube | 2560×1440px | Center 1546×423px |

### Post Images
| Platform | Recommended Size | Format |
|----------|-----------------|--------|
| Instagram Feed | 1080×1080px | JPG/PNG |
| Instagram Stories | 1080×1920px | JPG/PNG |
| Facebook Post | 1200×630px | JPG/PNG |
| Twitter/X | 1200×675px | JPG/PNG |
| LinkedIn | 1200×627px | JPG/PNG |

---

## Logo Usage

### Minimum Sizes
- **Primary Horizontal**: 200px width (digital), 2 inches (print)
- **Stacked**: 150px width (digital), 1.5 inches (print)
- **Icon Only**: 64×64px (digital), 0.5 inches (print)

### Clear Space
- Maintain space equal to height of "M" in ModelIt on all sides
- For icon: 10% of icon size on all sides

### Approved Backgrounds
✅ White (#FFFFFF)
✅ Light Background (#F2F6FA)
✅ Dark Blue (#1F4E79) - use white logo
✅ Navy (#2B2B40) - use white logo

❌ Busy patterns
❌ Low-contrast backgrounds
❌ Gradients

---

## Email Signature Template

```html
<table style="font-family: Arial, sans-serif; font-size: 14px; color: #2B2B40;">
  <tr>
    <td>
      <strong style="font-size: 16px;">[NAME]</strong><br>
      [TITLE]<br>
      <span style="color: #0078D7; font-weight: 500;">ModelIt K-12</span>
    </td>
  </tr>
  <tr>
    <td style="padding-top: 10px; border-top: 2px solid #0078D7;">
      <a href="mailto:[EMAIL]" style="color: #2B2B40; text-decoration: none;">[EMAIL]</a><br>
      <a href="tel:[PHONE]" style="color: #2B2B40; text-decoration: none;">[PHONE]</a><br>
      <a href="https://modelitk12.org" style="color: #0078D7; text-decoration: none;">modelitk12.org</a>
    </td>
  </tr>
</table>
```

---

## Brand Voice Quick Tips

### Do
✅ Use "you" and "your students"
✅ Lead with benefits, not features
✅ Include specific proof points
✅ Write in active voice
✅ Keep sentences 12-18 words average

### Don't
❌ Use jargon without explanation
❌ Make unrealistic promises
❌ Speak negatively about traditional teaching
❌ Use fear-based messaging
❌ Bury the lead with long preambles

### Example Headlines
✅ "Your Students Will Actually *Want* to Learn About Cells"
✅ "NGSS-Aligned and Ready to Use Tomorrow"
✅ "No Coding. No Complexity. Just Learning."

---

## File Naming Conventions

### Images
- `modelit-[type]-[description]-[size].[ext]`
- Examples:
  - `modelit-logo-primary-200px.png`
  - `modelit-social-quote-1080x1080.jpg`
  - `modelit-hero-classroom-1920x1080.jpg`

### Documents
- `ModelIt-[Type]-[Topic]-[Version].[ext]`
- Examples:
  - `ModelIt-Curriculum-Module1-v2.pdf`
  - `ModelIt-Presentation-Conference-2025.pptx`

---

## Support

**Questions?** cmartin@alexandriasdesign.com

**Need files?** Request logo package (SVG, PNG, AI, EPS)

**Last Updated**: 2025-12-18
