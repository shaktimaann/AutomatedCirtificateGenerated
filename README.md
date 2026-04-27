# Automated Certificate Generation

A Python-based application that automatically generates certificates from Excel data or structured data sources. This tool streamlines the process of creating personalized certificates in bulk by reading participant/recipient information from Excel files.

## 🎯 Features

- **Bulk Certificate Generation** - Generate multiple certificates automatically from a single data source
- **Excel Data Support** - Read recipient data from Excel (.xlsx, .xls) files
- **Customizable Templates** - Create and customize certificate templates to match your requirements
- **Data-Driven** - Personalize certificates with data fields like names, dates, course names, etc.
- **Batch Processing** - Efficiently process large datasets
- **Multiple Output Formats** - Generate certificates in various formats (PDF, PNG, etc.)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/shaktimaann/AutomatedCirtificateGenerated.git
cd AutomatedCirtificateGenerated
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💡 Usage

### Basic Usage

1. **Prepare Your Data**
   - Create an Excel file with recipient information
   - Columns should include data fields like: Name, Date, Course, etc.

2. **Configure Your Certificate Template**
   - Set up your certificate template with placeholders for dynamic data
   - Define field mappings between Excel columns and template placeholders

3. **Run the Generator**
```bash
python generate_certificates.py --input data.xlsx --output certificates/
```

### Example

```python
from certificate_generator import CertificateGenerator

# Initialize generator
generator = CertificateGenerator(
    template_path='template.png',
    data_file='recipients.xlsx'
)

# Generate certificates
generator.generate_all(output_directory='./output/')
```

## 📁 Project Structure

```
AutomatedCirtificateGenerated/
├── README.md
├── requirements.txt
├── certificate_generator.py
├── templates/
│   └── certificate_template.png
├── data/
│   └── recipients.xlsx
└── output/
    └── (generated certificates)
```

## 🔧 Configuration

Customize the following in your configuration:

- **Template Path**: Location of your certificate template image
- **Data Source**: Excel file path with recipient information
- **Output Directory**: Where to save generated certificates
- **Field Mappings**: Map Excel columns to template placeholders
- **Output Format**: Choose PDF, PNG, or other formats

## 📦 Dependencies

Key libraries used in this project:

- `openpyxl` - For reading Excel files
- `Pillow` - For image manipulation and certificate generation
- `reportlab` - For PDF generation (optional)

See `requirements.txt` for the complete list.

## 📝 Excel Data Format

Your Excel file should follow this structure:

| Name | Email | Course | Date | ID |
|------|-------|--------|------|-----|
| John Doe | john@example.com | Python Basics | 2026-04-27 | 001 |
| Jane Smith | jane@example.com | Web Development | 2026-04-27 | 002 |

## 🎨 Customization

To customize your certificates:

1. Edit the certificate template image
2. Update field placeholders in the template
3. Modify the field mapping configuration
4. Adjust font, size, and positioning as needed

## 🚦 Getting Started

1. Fork or clone this repository
2. Prepare your certificate template
3. Create an Excel file with recipient data
4. Configure the generator settings
5. Run the application to generate certificates

## 📌 Example Workflow

```bash
# 1. Prepare data in Excel
# 2. Set up template

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate certificates
python generate_certificates.py

# 5. Find your certificates in the output folder
```

## ⚙️ Configuration Example

```python
config = {
    'template_path': './templates/certificate_template.png',
    'data_file': './data/recipients.xlsx',
    'output_directory': './output/',
    'sheet_name': 'Sheet1',
    'field_mappings': {
        'Name': 'recipient_name',
        'Course': 'course_name',
        'Date': 'completion_date'
    }
}
```

## 🐛 Troubleshooting

- **Excel file not found**: Ensure the file path is correct and the file exists
- **Template issues**: Verify the template image path and format
- **Permission errors**: Check write permissions for the output directory

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest improvements
- Submit pull requests
- Share ideas for new features

## 📞 Support

For issues, questions, or suggestions, please create an issue on the GitHub repository.

---

**Author**: [shaktimaann](https://github.com/shaktimaann)

**Last Updated**: 2026-04-27