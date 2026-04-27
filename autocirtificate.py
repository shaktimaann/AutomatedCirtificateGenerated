from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# -------------------------
#  LOAD EXCEL DATA
# -------------------------
df = pd.read_excel("StudentData.xlsx")

# -------------------------
#  LOAD TEMPLATE
# -------------------------
template = Image.open("template_C1.jpg").convert("RGBA")
width, height = template.size

# -------------------------
#  REQUIRED FOLDERS
# -------------------------
os.makedirs("certificates", exist_ok=True)
os.makedirs("hod_signatures", exist_ok=True)
os.makedirs("principal_signatures", exist_ok=True)

# -------------------------
#  FONTS
# -------------------------
name_font = ImageFont.truetype("arial.ttf", 120)
content_font = ImageFont.truetype("arial.ttf", 45)
label_font = ImageFont.truetype("arial.ttf", 48)

# -------------------------
#  AUTO CONTENT GENERATOR
# -------------------------
def auto_content(course, achievement):
    achievement = str(achievement).strip().lower()

    if achievement in ["completion", ""]:
        lines = [
            f"In recognition of your successful completion of the {course} course.",
            "Your dedication and hard work have been truly outstanding.",
            "This certificate celebrates your excellent achievement and commitment.",
        ]
    elif achievement == "participation":
        lines = [
            f"In appreciation of your active participation in the {course} event.",
            "Your involvement and enthusiasm made a strong impact.",
            "Thank you for contributing your best to the occasion.",
        ]
    elif achievement == "winner":
        lines = [
            f"For securing first place in the {course} competition.",
            "Your skills and determination were exceptional.",
            "This certificate honors your outstanding performance.",
        ]
    else:
        lines = [
            f"In recognition of your achievement in {course}.",
            "Your effort and excellence are being celebrated here.",
            "This certificate reflects your dedication and success.",
        ]

    return "\n".join(lines)

# -------------------------
#  EXCEL COLUMNS
# -------------------------
name_col = "Student Name"
course_col = "Course/Achivement/Event"
achievement_col = "Course/Achivement/Event"
hod_col = "HoD Name"
principal_col = "HoE name"

# -------------------------
#  SIGNATURE MATCHING SYSTEM
# -------------------------
def clean_name(name):
    """Removes spaces, dots, lowercase → for matching."""
    return name.replace(".", "").replace(" ", "").lower()

def load_signature(name, folder):
    target = clean_name(name)

    for file in os.listdir(folder):
        if file.lower().endswith(".png"):
            file_clean = clean_name(os.path.splitext(file)[0])
            if file_clean == target:
                return Image.open(os.path.join(folder, file)).convert("RGBA")

    print(f"[WARNING] Signature NOT FOUND for {name}")
    return None

# -------------------------
# TEXT POSITIONS (Shifted down by ~1 cm = 40px)
NAME_POS = (1000, 750)          # was 720
CONTENT_POS = (1000, 915)       # was 930
HOD_POS = (600, 1260)           # was 1220
PRINCIPAL_POS = (1400, 1260)    # was 1220
# -------------------------
#  SIGNATURE POSITIONS
# -------------------------
HOD_SIGN_POS = (500, 1050)
PRINCIPAL_SIGN_POS = (1300, 1050)

# -------------------------
#  GENERATE CERTIFICATES
# -------------------------
for idx, row in df.iterrows():

    name = row[name_col]
    course = row[course_col]
    achievement = row[achievement_col]
    hod = row[hod_col]
    principal = row[principal_col]

    cert = template.copy()
    draw = ImageDraw.Draw(cert)

    # NAME
    draw.text(NAME_POS, name, font=name_font, fill="#b00000", anchor="mm")

    # CONTENT
    content = auto_content(course, achievement)
    lines = content.split("\n")
    line_spacing = 60
    start_y = CONTENT_POS[1] - (len(lines) - 1) * line_spacing // 2

    for i, line in enumerate(lines):
        y = start_y + i * line_spacing
        draw.text((CONTENT_POS[0], y), line, font=content_font, fill="black", anchor="mm")

    # HOD NAME
    draw.text(HOD_POS, hod, font=label_font, fill="black", anchor="mm")

    # PRINCIPAL NAME
    draw.text(PRINCIPAL_POS, principal, font=label_font, fill="black", anchor="mm")

    # --------- SIGNATURES ---------
    hod_sign = load_signature(hod, "hod_signatures")
    principal_sign = load_signature(principal, "principal_signatures")

    # Paste HOD signature
    if hod_sign:
        hod_sign = hod_sign.resize((350, 150))
        cert.paste(hod_sign, HOD_SIGN_POS, hod_sign)

    # Paste Principal signature
    if principal_sign:
        principal_sign = principal_sign.resize((350, 150))
        cert.paste(principal_sign, PRINCIPAL_SIGN_POS, principal_sign)

    # SAVE FILE
    filename = name.replace(" ", "_") + ".png"
    cert.save(f"certificates/{filename}")

print("\n✔ ALL CERTIFICATES GENERATED SUCCESSFULLY!")