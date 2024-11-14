import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

def generate_labels(csv_file, output_pdf="etiquettes.pdf"):
    # Lecture du fichier CSV
    data = pd.read_csv(csv_file)
    
    conference_name = "Journée LVP - GdR GPL - Novembre 2024"
    # Dimensions des étiquettes et de la page
    label_width = 9 * cm
    label_height = 5.5 * cm
    page_width, page_height = A4
    labels_per_row = int(page_width // label_width)
    labels_per_column = int(page_height // label_height)
    
    # Création du canvas PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    
    x_offset = 0.5 * cm
    y_offset = 0.5 * cm
    
    # Boucle pour créer chaque étiquette
    x = x_offset
    y = page_height - y_offset - label_height
    
    for index, row in data.iterrows():
        nom = row['NOM'].upper()
        prenom = row['Prénom']
        affiliation = row['Affiliation']
        
        # Dessiner les lignes de découpe autour de l'étiquette
        c.setStrokeColorRGB(0.6, 0.6, 0.6)  # Couleur gris clair
        c.setLineWidth(0.5)
        c.rect(x, y, label_width, label_height, stroke=1, fill=0)
        
        # Ajout du texte de l'étiquette
        c.setFont("Helvetica-Bold", 20)
        c.drawString(x + 0.2 * cm, y + label_height - 1 * cm, nom)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x + 0.2 * cm, y + label_height - 2 * cm, prenom)
        c.setFont("Helvetica", 10)
        c.drawString(x + 0.2 * cm, y + label_height - 3 * cm, affiliation)
        c.drawString(x + 0.2 * cm, y + label_height - 5 * cm, conference_name)
        # Passer à la prochaine étiquette
        x += label_width
        if x + label_width > page_width:
            x = x_offset
            y -= label_height
            if y < y_offset:
                c.showPage()  # Nouvelle page si nécessaire
                x = x_offset
                y = page_height - y_offset - label_height
    
    # Sauvegarde du fichier PDF
    c.save()
    print(f"PDF généré: {output_pdf}")

# Exemple d'utilisation :
generate_labels("montableau.csv")
