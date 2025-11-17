"""
ModelIt K12 Brand Constants
Complete brand identity specification for automated asset generation
"""

from pptx.dml.color import RGBColor

# ============================================================================
# BRAND COLORS
# ============================================================================

# Primary Colors
BRAND_COLORS = {
    "primary_dark_blue": {
        "name": "Primary Dark Blue",
        "hex": "#1F4E79",
        "rgb": (31, 78, 121),
        "cmyk": (74, 36, 0, 53),
        "usage": "Headings, primary text, professional materials"
    },
    "primary_light_blue": {
        "name": "Primary Light Blue",
        "hex": "#0078D7",
        "rgb": (0, 120, 215),
        "cmyk": (100, 44, 0, 16),
        "usage": "Accents, CTAs, interactive elements"
    },
    "secondary_navy": {
        "name": "Secondary Navy",
        "hex": "#2B2B40",
        "rgb": (43, 43, 64),
        "cmyk": (33, 33, 0, 75),
        "usage": "Secondary text, borders, subtle accents"
    },
    "background_light": {
        "name": "Background Light",
        "hex": "#F2F6FA",
        "rgb": (242, 246, 250),
        "cmyk": (3, 2, 0, 2),
        "usage": "Backgrounds, light sections, cards"
    },
    "accent_teal": {
        "name": "Accent Teal",
        "hex": "#009999",
        "rgb": (0, 153, 153),
        "cmyk": (100, 0, 0, 40),
        "usage": "Highlights, science themes, molecular diagrams"
    },
    "accent_gold": {
        "name": "Accent Gold",
        "hex": "#FFC857",
        "rgb": (255, 200, 87),
        "cmyk": (0, 22, 66, 0),
        "usage": "Warnings, important highlights, premium badges"
    }
}

# RGBColor objects for PowerPoint (direct use in python-pptx)
COLORS_PPT = {
    "primary_dark_blue": RGBColor(31, 78, 121),
    "primary_light_blue": RGBColor(0, 120, 215),
    "secondary_navy": RGBColor(43, 43, 64),
    "background_light": RGBColor(242, 246, 250),
    "accent_teal": RGBColor(0, 153, 153),
    "accent_gold": RGBColor(255, 200, 87),
    "white": RGBColor(255, 255, 255),
    "black": RGBColor(0, 0, 0)
}

# ============================================================================
# TYPOGRAPHY
# ============================================================================

FONTS = {
    "primary": "Segoe UI",
    "primary_fallback": "Arial",
    "headings": "Segoe UI Semibold",
    "body": "Segoe UI",
    "code": "Consolas"
}

FONT_SIZES = {
    "title": 44,
    "heading_1": 36,
    "heading_2": 28,
    "heading_3": 22,
    "body": 18,
    "caption": 14,
    "small": 12
}

# ============================================================================
# BRAND IDENTITY
# ============================================================================

BRAND_INFO = {
    "name": "ModelIt! K12",
    "tagline": "Systems Thinking for Tomorrow's Scientists",
    "mission": "Empowering K-12 students with computational modeling and systems thinking",
    "target_audience": "Middle School Science Teachers (Grades 5-8)",
    "focus_areas": ["NGSS Alignment", "Boolean Modeling", "Cell Collective Integration"]
}

# ============================================================================
# MICRO MAYHEM MASCOT
# ============================================================================

MASCOT_INFO = {
    "name": "Micro Mayhem",
    "description": "A friendly, energetic cartoon microorganism character that represents the microscopic world of cell biology",
    "personality": "Curious, enthusiastic, playful, scientifically accurate",
    "appearance": "Spherical cell-like body with expressive eyes, cilia/flagella for movement, translucent membrane showing internal organelles",
    "color_scheme": [
        BRAND_COLORS["primary_light_blue"]["hex"],
        BRAND_COLORS["accent_teal"]["hex"],
        BRAND_COLORS["accent_gold"]["hex"]
    ],
    "poses": [
        "thinking (hand on chin)",
        "celebrating (arms raised)",
        "teaching (pointing at board)",
        "experimenting (holding test tube)",
        "reading (with book)",
        "surprised (wide eyes)",
        "confused (question mark)",
        "excited (jumping)",
        "working (at computer)",
        "presenting (with pointer)"
    ]
}

# ============================================================================
# IMAGE GENERATION PROMPTS
# ============================================================================

IMAGE_STYLES = {
    "molecular_structure": {
        "style": "scientific illustration",
        "colors": ["#0078D7", "#009999", "#F2F6FA"],
        "elements": ["atoms", "bonds", "molecular orbitals", "3D perspective"],
        "tone": "clean, professional, educational"
    },
    "network_diagram": {
        "style": "technical infographic",
        "colors": ["#1F4E79", "#0078D7", "#009999"],
        "elements": ["nodes", "connections", "data flow", "system relationships"],
        "tone": "modern, clean, technical"
    },
    "cell_imagery": {
        "style": "biological illustration",
        "colors": ["#009999", "#0078D7", "#FFC857"],
        "elements": ["cells", "organelles", "membranes", "biological processes"],
        "tone": "scientifically accurate, vibrant, engaging"
    },
    "educational_graphic": {
        "style": "flat design illustration",
        "colors": ["#0078D7", "#FFC857", "#F2F6FA"],
        "elements": ["icons", "text", "diagrams", "simple shapes"],
        "tone": "friendly, accessible, clear"
    }
}

# ============================================================================
# ASSET SPECIFICATIONS
# ============================================================================

ASSET_SIZES = {
    "tpt_cover": {
        "width": 1800,
        "height": 2400,
        "dpi": 300,
        "format": "PNG"
    },
    "social_media": {
        "facebook_cover": (820, 312),
        "twitter_header": (1500, 500),
        "linkedin_banner": (1584, 396),
        "youtube_thumbnail": (1280, 720),
        "instagram_post": (1080, 1080)
    },
    "powerpoint_slide": {
        "width": 10,  # inches
        "height": 7.5,  # inches (16:9 widescreen)
        "format": "PPTX"
    },
    "banner": {
        "width": 1200,
        "height": 300,
        "dpi": 150,
        "format": "PNG"
    },
    "icon": {
        "width": 512,
        "height": 512,
        "dpi": 72,
        "format": "PNG"
    }
}

# ============================================================================
# NANO BANANA (IMAGE GENERATION) SETTINGS
# ============================================================================

NANO_BANANA = {
    "model": "google/gemini-2.5-flash-image",
    "endpoint": "https://openrouter.ai/api/v1/chat/completions",
    "cost_per_image": 0.039,
    "modalities": ["image", "text"],  # REQUIRED parameter
    "max_tokens": 16000,
    "temperature": 0.7
}

# ============================================================================
# POWERPOINT LAYOUT SETTINGS
# ============================================================================

PPT_LAYOUT = {
    "slide_width": 10,  # inches
    "slide_height": 7.5,  # inches
    "margin_top": 0.5,
    "margin_bottom": 0.5,
    "margin_left": 0.75,
    "margin_right": 0.75,
    "title_area_height": 1.5,
    "content_area_top": 2.0
}

# ============================================================================
# ICON LIBRARY TOPICS
# ============================================================================

ICON_TOPICS = [
    "NGSS Standards",
    "Cell Biology",
    "Systems Thinking",
    "Boolean Modeling",
    "Chemical Reactions",
    "Energy Transfer",
    "Phase Changes",
    "Conservation Laws",
    "Atomic Structure",
    "Feedback Loops",
    "Scientific Method",
    "Lab Equipment"
]

# ============================================================================
# STYLE GUIDE SECTIONS
# ============================================================================

STYLE_GUIDE_SECTIONS = [
    "Color Palette (Primary, Secondary, Accents)",
    "Typography (Fonts, Sizes, Hierarchy)",
    "Logo Usage Guidelines",
    "Micro Mayhem Mascot Guidelines",
    "PowerPoint Template Examples",
    "Social Media Cover Examples",
    "TPT Cover Template",
    "Icon Library Showcase",
    "Do's and Don'ts",
    "Brand Voice and Tone"
]
