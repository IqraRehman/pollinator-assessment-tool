from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
import io

def create_recipe_guide():
    """Generate a PDF guide for natural cleaning recipes"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Recipe',
        fontSize=12,
        spaceAfter=20,
        leading=16
    ))

    story = []

    # Title
    story.append(Paragraph("🌿 Natural Cleaning Recipes Guide", styles['Title']))
    story.append(Spacer(1, 20))

    # Introduction
    story.append(Paragraph("""
    Welcome to your guide to pollinator-friendly cleaning solutions! These natural recipes are safe 
    for your home and our important pollinator friends. All ingredients are readily available and 
    biodegradable.
    """, styles['Recipe']))

    # Safety Note
    story.append(Paragraph("""
    ⚠️ Safety Notes:
    • Always label your cleaning solutions clearly
    • Keep out of reach of children and pets
    • Test on a small area first
    • Never mix different cleaning solutions
    • Store in a cool, dark place
    """, styles['Recipe']))
    story.append(Spacer(1, 20))

    # Recipes
    recipes = {
        "All-Purpose Cleaner": {
            "ingredients": [
                "2 cups white vinegar",
                "2 cups water",
                "1 lemon rind",
                "2-3 sprigs fresh rosemary (optional)",
            ],
            "instructions": [
                "Combine vinegar and water in a spray bottle",
                "Add lemon rind and rosemary",
                "Let infuse for 1 week",
                "Strain and use on surfaces",
            ],
            "notes": "Great for countertops, appliances, and most hard surfaces. The vinegar smell dissipates quickly."
        },
        "Window & Glass Cleaner": {
            "ingredients": [
                "2 cups water",
                "1/2 cup white vinegar",
                "1/4 cup rubbing alcohol (optional, for faster drying)",
            ],
            "instructions": [
                "Mix all ingredients in a spray bottle",
                "Shake well before each use",
                "Spray on surface and wipe with lint-free cloth",
            ],
            "notes": "For streak-free results, use newspaper or microfiber cloth. Clean on a cool, cloudy day to prevent premature drying."
        },
        "Natural Air Freshener": {
            "ingredients": [
                "2 cups water",
                "1/2 cup dried lavender, mint, or citrus peels",
                "2 tablespoons baking soda",
            ],
            "instructions": [
                "Simmer ingredients in a pot on low heat",
                "For spray version: strain and transfer to spray bottle",
                "Add a drop of essential oil if desired",
            ],
            "notes": "You can also place bowls of baking soda around the house to absorb odors naturally."
        },
        "Tile & Grout Cleaner": {
            "ingredients": [
                "1/2 cup baking soda",
                "1/4 cup hydrogen peroxide",
                "1 teaspoon liquid castile soap",
            ],
            "instructions": [
                "Mix ingredients to form a paste",
                "Apply to grout lines with a brush",
                "Let sit for 10 minutes",
                "Scrub and rinse thoroughly",
            ],
            "notes": "Test on a small area first. This paste can also be used for tough bathroom stains."
        }
    }

    for title, recipe in recipes.items():
        # Recipe Title
        story.append(Paragraph(f"🧪 {title}", styles['Heading1']))

        # Ingredients
        story.append(Paragraph("Ingredients:", styles['Heading2']))
        for ingredient in recipe['ingredients']:
            story.append(Paragraph(f"• {ingredient}", styles['Recipe']))

        # Instructions
        story.append(Paragraph("Instructions:", styles['Heading2']))
        for step in recipe['instructions']:
            story.append(Paragraph(f"• {step}", styles['Recipe']))

        # Notes
        story.append(Paragraph("Notes:", styles['Heading2']))
        story.append(Paragraph(recipe['notes'], styles['Recipe']))

        story.append(Spacer(1, 20))

    # Final Tips
    story.append(Paragraph("✨ Pro Tips:", styles['Heading2']))
    tips = [
        "Always use clean, recycled spray bottles",
        "Label all containers with ingredients and date",
        "Make small batches to ensure freshness",
        "Store solutions away from direct sunlight",
        "Never mix different cleaning solutions"
    ]
    for tip in tips:
        story.append(Paragraph(f"• {tip}", styles['Recipe']))

    # Add Bee Friends Cleaners pitch
    story.append(Spacer(1, 30))
    story.append(Paragraph("🌟 Want More Time for What You Love?", styles['Heading2']))
    story.append(Paragraph("""
    While making your own natural cleaners is rewarding, we understand life gets busy! 
    Want to spend more time enjoying your garden or pursuing your passions? 
    Let Bee Friends Cleaners handle your eco-friendly cleaning needs!

    • Professional pollinator-safe cleaning services
    • Expert green cleaning techniques
    • Time-saving convenience
    • Peace of mind for you and our pollinator friends

    Contact us today:
    📞 Call: 207-805-5524
    🌐 Visit: beefriendscleaners.com
    """, styles['Recipe']))

    doc.build(story)
    buffer.seek(0)
    return buffer