from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
import io

def create_pdf(score_level, percentage, recommendations):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Custom',
        fontSize=12,
        spaceAfter=30
    ))
    
    story = []
    
    # Title
    story.append(Paragraph(f"Your Pollinator-Friendly Cleaning Guide", styles['Title']))
    story.append(Spacer(1, 12))
    
    # Score
    story.append(Paragraph(f"Score: {percentage:.1f}%", styles['Heading1']))
    story.append(Spacer(1, 12))
    
    # Recommendations
    story.append(Paragraph("Recommended Actions:", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    for rec in recommendations:
        story.append(Paragraph(f"<b>{rec['title']}</b>", styles['Custom']))
        story.append(Paragraph(f"Impact: {rec['impact']}", styles['Custom']))
        story.append(Paragraph(f"Effort: {rec['effort']}", styles['Custom']))
        story.append(Paragraph(f"Description: {rec['description']}", styles['Custom']))
        
        story.append(Paragraph("Implementation Steps:", styles['Custom']))
        for step in rec['implementation']:
            story.append(Paragraph(f"• {step}", styles['Custom']))
        
        story.append(Spacer(1, 12))
    
    doc.build(story)
    buffer.seek(0)
    return buffer
