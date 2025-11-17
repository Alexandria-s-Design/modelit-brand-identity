"""
Visual Assets Generator for ModelIt K12
Uses Nano Banana (Gemini 2.5 Flash Image) to generate branded visual assets
Generates: Molecular structures, network diagrams, cell imagery
Output: /assets/visuals/*.png
"""

import os
import sys
import requests
import base64
from pathlib import Path
from datetime import datetime

# Import brand constants
sys.path.append(str(Path(__file__).parent))
from brand_constants import (
    BRAND_COLORS, IMAGE_STYLES, NANO_BANANA, BRAND_INFO
)

# Get API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in environment!")

def generate_image_with_nano_banana(prompt: str, image_type: str = "molecular_structure"):
    """Generate image using Nano Banana (Gemini 2.5 Flash Image)"""

    # Get style specifications
    style_spec = IMAGE_STYLES.get(image_type, IMAGE_STYLES["molecular_structure"])

    # Build enhanced prompt with brand colors
    brand_colors_str = ", ".join([BRAND_COLORS[key]["hex"] for key in ["primary_light_blue", "accent_teal", "primary_dark_blue"]])
    enhanced_prompt = f"""{prompt}

Style: {style_spec['style']}
Color palette: {brand_colors_str} (ModelIt K12 brand colors)
Elements: {', '.join(style_spec['elements'])}
Tone: {style_spec['tone']}
Background: White or light gradient ({BRAND_COLORS['background_light']['hex']})
High quality, professional, educational illustration suitable for middle school science materials.
"""

    print(f"  ├─ Generating: {prompt[:60]}...")

    try:
        response = requests.post(
            NANO_BANANA["endpoint"],
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": NANO_BANANA["model"],
                "messages": [{"role": "user", "content": enhanced_prompt}],
                "modalities": NANO_BANANA["modalities"],  # CRITICAL!
                "max_tokens": NANO_BANANA["max_tokens"],
                "temperature": NANO_BANANA["temperature"]
            },
            timeout=120
        )

        if response.status_code == 200:
            data = response.json()

            # Extract image from response
            if 'choices' in data and len(data['choices']) > 0:
                choice = data['choices'][0]

                # Check for images in response
                if 'message' in choice and 'images' in choice['message']:
                    image_data = choice['message']['images'][0]
                    image_url = image_data['image_url']['url']

                    # Decode base64 image
                    if image_url.startswith('data:image'):
                        # Format: data:image/png;base64,<data>
                        base64_data = image_url.split(',')[1]
                        image_bytes = base64.b64decode(base64_data)
                        return image_bytes
                    else:
                        print(f"  │  ⚠️ Unexpected image URL format")
                        return None
                else:
                    print(f"  │  ⚠️ No images in response")
                    return None
            else:
                print(f"  │  ⚠️ No choices in response")
                return None
        else:
            print(f"  │  ❌ API error: {response.status_code}")
            print(f"  │  Response: {response.text[:200]}")
            return None

    except Exception as e:
        print(f"  │  ❌ Error: {str(e)}")
        return None

def save_image(image_bytes: bytes, filename: str, asset_type: str = "visuals"):
    """Save image to assets directory"""
    output_dir = Path(__file__).parent.parent / "assets" / asset_type
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename
    with open(output_path, 'wb') as f:
        f.write(image_bytes)

    print(f"  └─ ✅ Saved: {filename}")
    return output_path

# ============================================================================
# ASSET DEFINITIONS
# ============================================================================

VISUAL_ASSETS = {
    "molecular_structures": [
        {
            "prompt": "3D molecular structure of a water molecule (H2O) showing electron clouds and bonds, transparent spheres for atoms, scientific illustration",
            "filename": "water_molecule_3d.png",
            "type": "molecular_structure"
        },
        {
            "prompt": "DNA double helix structure with labeled base pairs, scientific diagram style, clean educational illustration",
            "filename": "dna_double_helix.png",
            "type": "molecular_structure"
        },
        {
            "prompt": "ATP molecule (adenosine triphosphate) with phosphate groups highlighted, energy transfer visualization",
            "filename": "atp_molecule_energy.png",
            "type": "molecular_structure"
        },
        {
            "prompt": "Protein structure showing primary, secondary, tertiary, and quaternary levels, educational diagram",
            "filename": "protein_structure_levels.png",
            "type": "molecular_structure"
        },
        {
            "prompt": "Chemical reaction diagram showing reactants and products with energy levels, activation energy graph",
            "filename": "chemical_reaction_energy.png",
            "type": "molecular_structure"
        }
    ],
    "network_diagrams": [
        {
            "prompt": "Systems thinking diagram showing interconnected nodes and feedback loops, clean technical infographic style",
            "filename": "systems_thinking_network.png",
            "type": "network_diagram"
        },
        {
            "prompt": "Biological pathway network with nodes and connections, gene regulatory network visualization",
            "filename": "biological_pathway_network.png",
            "type": "network_diagram"
        },
        {
            "prompt": "Ecosystem food web diagram showing energy flow between organisms, circular network layout",
            "filename": "ecosystem_food_web.png",
            "type": "network_diagram"
        },
        {
            "prompt": "Neural network diagram with input, hidden, and output layers, AI/ML visualization style",
            "filename": "neural_network_layers.png",
            "type": "network_diagram"
        },
        {
            "prompt": "Boolean logic network showing AND, OR, NOT gates connected in a circuit, computational modeling",
            "filename": "boolean_logic_network.png",
            "type": "network_diagram"
        }
    ],
    "cell_imagery": [
        {
            "prompt": "Detailed animal cell cross-section showing all organelles (nucleus, mitochondria, ER, Golgi), labeled educational illustration",
            "filename": "animal_cell_detailed.png",
            "type": "cell_imagery"
        },
        {
            "prompt": "Plant cell showing chloroplasts, cell wall, and large central vacuole, vibrant green and blue tones",
            "filename": "plant_cell_detailed.png",
            "type": "cell_imagery"
        },
        {
            "prompt": "Mitochondria organelle showing inner and outer membranes with cristae, energy production visualization",
            "filename": "mitochondria_powerhouse.png",
            "type": "cell_imagery"
        },
        {
            "prompt": "Cell membrane structure showing phospholipid bilayer with embedded proteins, molecular detail",
            "filename": "cell_membrane_structure.png",
            "type": "cell_imagery"
        },
        {
            "prompt": "Cell division (mitosis) showing all phases: prophase, metaphase, anaphase, telophase, educational sequence",
            "filename": "cell_division_mitosis.png",
            "type": "cell_imagery"
        }
    ],
    "educational_graphics": [
        {
            "prompt": "NGSS science standards icon with gear and beaker symbol, flat design, professional badge style",
            "filename": "ngss_standards_icon.png",
            "type": "educational_graphic"
        },
        {
            "prompt": "Scientific method flowchart with steps: question, hypothesis, experiment, analysis, conclusion, circular diagram",
            "filename": "scientific_method_flowchart.png",
            "type": "educational_graphic"
        },
        {
            "prompt": "Data visualization showing multiple types: bar chart, line graph, pie chart, scatter plot, colorful infographic",
            "filename": "data_visualization_types.png",
            "type": "educational_graphic"
        },
        {
            "prompt": "Lab safety equipment illustrations: goggles, gloves, lab coat, fire extinguisher, first aid kit, icon set",
            "filename": "lab_safety_equipment.png",
            "type": "educational_graphic"
        },
        {
            "prompt": "States of matter transformation diagram: solid to liquid to gas, particle model visualization",
            "filename": "states_of_matter_diagram.png",
            "type": "educational_graphic"
        }
    ]
}

def generate_all_visual_assets(categories=None, max_per_category=None):
    """Generate all visual assets"""

    print("\n🎨 Generating ModelIt K12 Visual Assets with Nano Banana...")
    print(f"   Model: {NANO_BANANA['model']}")
    print(f"   Cost per image: ${NANO_BANANA['cost_per_image']}")

    if categories is None:
        categories = VISUAL_ASSETS.keys()

    total_generated = 0
    total_failed = 0
    total_cost = 0.0

    for category in categories:
        if category not in VISUAL_ASSETS:
            print(f"\n⚠️ Unknown category: {category}")
            continue

        assets = VISUAL_ASSETS[category]
        if max_per_category:
            assets = assets[:max_per_category]

        print(f"\n📁 Category: {category.replace('_', ' ').title()}")
        print(f"   Generating {len(assets)} images...")

        for asset in assets:
            image_bytes = generate_image_with_nano_banana(
                asset["prompt"],
                asset["type"]
            )

            if image_bytes:
                save_image(image_bytes, asset["filename"], "visuals")
                total_generated += 1
                total_cost += NANO_BANANA["cost_per_image"]
            else:
                print(f"  └─ ❌ Failed: {asset['filename']}")
                total_failed += 1

    # Summary
    print(f"\n" + "="*60)
    print(f"📊 Visual Assets Generation Complete!")
    print(f"   ✅ Successfully generated: {total_generated} images")
    if total_failed > 0:
        print(f"   ❌ Failed: {total_failed} images")
    print(f"   💰 Total cost: ${total_cost:.2f}")
    print(f"   📁 Location: /assets/visuals/")
    print("="*60)

    return total_generated, total_failed, total_cost

if __name__ == "__main__":
    import sys

    # Parse command line arguments
    if len(sys.argv) > 1:
        categories = sys.argv[1].split(',')
        max_per = int(sys.argv[2]) if len(sys.argv) > 2 else None
    else:
        # Default: Generate 2 from each category (demo mode)
        categories = list(VISUAL_ASSETS.keys())
        max_per = 2

    generate_all_visual_assets(categories, max_per)
