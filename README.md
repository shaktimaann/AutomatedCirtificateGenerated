# Automated Certificate Generation

A Python-based application that automatically generates personalized certificates from Excel data. This tool streamlines bulk certificate creation with customizable templates, dynamic content, and automatic signature integration.

## 🎯 Features

- ✅ **Bulk Certificate Generation** - Generate multiple certificates in seconds
- ✅ **Excel Data Integration** - Read recipient data from Excel (.xlsx) files
- ✅ **Customizable Templates** - Use your own certificate template images
- ✅ **Dynamic Content** - Auto-generate certificate text based on achievement type
- ✅ **Signature Support** - Automatically embed signatures from HOD and Principal
- ✅ **Robust Error Handling** - Detailed validation and helpful error messages
- ✅ **Smart Font Fallback** - Works even if system fonts are unavailable

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/shaktimaann/AutomatedCirtificateGenerated.git
cd AutomatedCirtificateGenerated
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Prepare your data:**
   - Create an Excel file with student information
   - Add signature images for HOD and Principal

4. **Run the generator:**
```bash
python autocirtificate.py
```

## 📁 Project Structure

```
AutomatedCirtificateGenerated/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── autocirtificate.py           # Main certificate generator
├── StudentData.xlsx             # Student data (template provided)
├── template_C1.jpg              # Certificate template image
├── certificates/                # Output folder (auto-created)
├── hod_signatures/              # HOD signature images
└── principal_signatures/        # Principal signature images
```

## 📝 Excel Data Format

Your `StudentData.xlsx` file should have these columns:

| Student Name | Course/Achievement/Event | HoD Name | HoE name |
|---|---|---|---|
| John Doe | Python Basics | Dr. Smith | Principal Johnson |
| Jane Smith | Web Development | Dr. Brown | Principal Johnson |
| Alex Kumar | Competition Winner | Dr. Davis | Principal Johnson |

**Column Names** (must match exactly):
- `Student Name` - Name of the student
- `Course/Achievement/Event` - Course name or event (used for content generation)
- `HoD Name` - Head of Department name
- `HoE name` - Head of Education / Principal name

## 🔧 Achievement Types

The script automatically generates different certificate messages based on the achievement type:

| Type | Example | Message |
|------|---------|---------|
| **Completion** | Leave blank or type "completion" | Recognizes successful course completion |
| **Participation** | Type "participation" | Appreciates active event participation |
| **Winner** | Type "winner" | Honors competition victory |
| **Generic** | Any other value | Generic achievement recognition |

## 🖼️ Signature Image Setup

1. **Prepare signature images** (PNG format):
   - Save as `HoD_Name.png` (e.g., `Dr_Smith.png`, `Dr.Smith.png`)
   - Save as `Principal_Name.png` (e.g., `Principal_Johnson.png`)
   - Name matching is flexible (spaces and dots are ignored)

2. **Place in correct folders:**
   - HOD signatures → `hod_signatures/` folder
   - Principal signatures → `principal_signatures/` folder

3. **If signatures are not found:**
   - Script will continue and skip the signature (no errors)
   - You'll see a warning: `[WARNING] Signature NOT FOUND for Dr. Smith`

## ⚙️ Customization

### Adjust Text Positions
Edit these constants in `autocirtificate.py` (in pixels):

```python
NAME_POS = (1000, 750)              # Student name position
CONTENT_POS = (1000, 915)           # Certificate content position
HOD_POS = (600, 1260)               # HOD name position
PRINCIPAL_POS = (1400, 1260)        # Principal name position
HOD_SIGN_POS = (500, 1050)          # HOD signature position
PRINCIPAL_SIGN_POS = (1300, 1050)   # Principal signature position
```

### Adjust Font Sizes
```python
name_font = load_font("arial.ttf", 120)      # Student name (120pt)
content_font = load_font("arial.ttf", 45)    # Certificate text (45pt)
label_font = load_font("arial.ttf", 48)      # Official names (48pt)
```

### Modify Certificate Content
Edit the `auto_content()` function to customize the default messages for each achievement type.

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| **"StudentData.xlsx not found"** | Ensure the Excel file is in the same directory as the script |
| **"Missing column: Student Name"** | Check that Excel column names match exactly (case-sensitive) |
| **"template_C1.jpg not found"** | Ensure the template image is in the same directory |
| **Fonts not loading** | Script will use default font automatically - no action needed |
| **Signatures not appearing** | Check file names in signature folders and ensure they match the names in Excel |
| **Permission denied** | Ensure write permissions for the `certificates/` folder |

## 📊 Output

Generated certificates are saved in the `certificates/` folder with names like:
- `John_Doe.png`
- `Jane_Smith.png`
- `Alex_Kumar.png`

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| **Pillow (PIL)** | Image processing and certificate generation |
| **pandas** | Excel file reading and data manipulation |
| **openpyxl** | Excel format support for pandas |

See `requirements.txt` for specific versions.

## 🔍 Example Workflow

```bash
# 1. Prepare your data
# - Create StudentData.xlsx with student information
# - Add signature PNG files to hod_signatures/ and principal_signatures/

# 2. Install dependencies
pip install -r requirements.txt

# 3. Customize (optional)
# - Edit positions, fonts, or content in autocirtificate.py
# - Update certificate template if needed

# 4. Generate certificates
python autocirtificate.py

# Output:
# [1/5] Loading Excel data...
# [✓] Loaded 50 records from StudentData.xlsx
# [2/5] Validating files and columns...
# [5/5] Generating certificates...
#   [1/50] ✓ Generated: John_Doe.png
#   [2/50] ✓ Generated: Jane_Smith.png
#   ...
# ✓ CERTIFICATES GENERATED: 50/50

# 5. Find your certificates in the certificates/ folder
```

## 🎨 Creating a Custom Template

1. Create a certificate design in any image editor (Photoshop, Canva, GIMP, etc.)
2. Export as JPG or PNG
3. Replace `template_C1.jpg` with your template
4. Adjust position constants in the code to match your template layout
5. Re-run the script with your data

## ⚡ Tips & Best Practices

- ✅ Use high-resolution templates (1400+ pixels) for print-quality certificates
- ✅ Keep signature images at 350x150px or larger for best results
- ✅ Use PNG for signatures (transparency is preserved)
- ✅ Test with 2-3 records first before bulk generation
- ✅ Maintain consistent naming for signatures (e.g., always use first and last name)
- ✅ Back up your template and data files

## 🚦 Performance

- Generates ~50 certificates per minute on average hardware
- Speed depends on template size and number of signatures
- No real-time optimization needed for <1000 certificates

## 📄 License

This project is open source and available under the **MIT License**. See LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! You can:
- Report bugs via GitHub Issues
- Suggest improvements
- Submit pull requests
- Share feedback and ideas

## 💬 Support & Questions

For issues, questions, or feature requests:
1. Check the Troubleshooting section above
2. Create a GitHub Issue with details
3. Provide your Excel structure and error messages

---

**Author**: [shaktimaann](https://github.com/shaktimaann)

**Last Updated**: 2026-04-27

**Status**: Active & Maintained ✓
