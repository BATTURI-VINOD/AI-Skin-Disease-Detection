import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)


REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def create_pdf(disease, confidence, info, image_path):

    filename = f"Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf_path = os.path.join(REPORT_FOLDER, filename)

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "<b><font size=20 color='blue'>AI Skin Disease Detection Report</font></b>",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    if os.path.exists(image_path):

        img = Image(image_path)

        img.drawWidth = 250
        img.drawHeight = 250

        story.append(img)

        story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Predicted Disease:</b> {disease}",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence}%",
            styles["Heading3"]
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Description</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            info["description"],
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Symptoms</b>",
            styles["Heading2"]
        )
    )

    for symptom in info["symptoms"]:

        story.append(
            Paragraph(
                "• " + symptom,
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Precautions</b>",
            styles["Heading2"]
        )
    )

    for precaution in info["precautions"]:

        story.append(
            Paragraph(
                "• " + precaution,
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<font color='red'><b>Disclaimer:</b></font> This AI prediction is for educational purposes only. Please consult a qualified dermatologist for medical diagnosis.",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename