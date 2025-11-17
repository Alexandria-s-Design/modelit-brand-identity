"""
Micro Mayhem Mascot Generator for ModelIt K12
Uses Nano Banana to generate mascot character in various poses
Output: /assets/mascot/*.png
"""

import os
import sys
import requests
import base64
from pathlib import Path

# Import brand constants
sys.path.append(str(Path(__file__).parent))
from brand_constants import MASCOT_INFO, NANO_BANANA

# Get API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in environment!")

def generate_mascot_image(pose_description: str, filename: str):
    """Generate mascot image with Nano Banana"""

    # Build detailed prompt
    prompt = f"""Character design for educational mascot named "{MASCOT_INFO['name']}":

Description: {MASCOT_INFO['description']}
Personality: {MASCOT_INFO['personality']}
Appearance: {MASCOT_INFO['appearance']}

Pose: {pose_description}

Style: Friendly cartoon illustration, cel-shaded, smooth gradients
Color scheme: {', '.join(MASCOT_INFO['color_scheme'])}
Background: Transparent or white
Quality: High resolution, clean edges, professional character design suitable for educational materials

The character should look friendly, approachable, and scientifically accurate while being engaging for middle school students."""

    print(f"  ├─ Generating mascot: {pose_description}...")

    try:
        response = requests.post(
            NANO_BANANA["endpoint"],
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": NANO_BANANA["model"],
                "messages": [{"role": "user", "content": prompt}],
                "modalities": NANO_BANANA["modalities"],
                "max_tokens": NANO_BANANA["max_tokens"],
                "temperature": 0.8  # Slightly higher for creative variation
            },
            timeout=120
        )

        if response.status_code == 200:
            data = response.json()

            if 'choices' in data and len(data['choices']) > 0:
                choice = data['choices'][0]

                if 'message' in choice and 'images' in choice['message']:
                    image_data = choice['message']['images'][0]
                    image_url = image_data['image_url']['url']

                    if image_url.startswith('data:image'):
                        base64_data = image_url.split(',')[1]
                        image_bytes = base64.b64decode(base64_data)

                        # Save image
                        output_dir = Path(__file__).parent.parent / "assets" / "mascot"
                        output_dir.mkdir(parents=True, exist_ok=True)

                        output_path = output_dir / filename
                        with open(output_path, 'wb') as f:
                            f.write(image_bytes)

                        print(f"  └─ ✅ Saved: {filename}")
                        return True

        print(f"  └─ ❌ Failed to generate {filename}")
        return False

    except Exception as e:
        print(f"  └─ ❌ Error: {str(e)}")
        return False

def generate_all_mascots(poses=None):
    """Generate Micro Mayhem mascot in multiple poses"""

    print("\n🎭 Generating Micro Mayhem Mascot Variations...")
    print(f"   Character: {MASCOT_INFO['name']}")
    print(f"   Model: {NANO_BANANA['model']}")

    if poses is None:
        poses = MASCOT_INFO["poses"]

    success_count = 0
    total_cost = 0.0

    for pose in poses:
        filename = f"micro_mayhem_{pose.replace(' ', '_').replace('(', '').replace(')', '')}.png"
        success = generate_mascot_image(pose, filename)

        if success:
            success_count += 1
            total_cost += NANO_BANANA["cost_per_image"]

    print(f"\n📊 Mascot Generation Complete!")
    print(f"   ✅ Generated: {success_count}/{len(poses)} poses")
    print(f"   💰 Total cost: ${total_cost:.2f}")
    print(f"   📁 Location: /assets/mascot/")

    return success_count

if __name__ == "__main__":
    # Generate 5 key poses (can be expanded later)
    key_poses = MASCOT_INFO["poses"][:5]
    generate_all_mascots(key_poses)
