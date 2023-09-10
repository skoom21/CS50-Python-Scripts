from typing_extensions import Literal
from fpdf import FPDF
from PIL import Image


# Create a subclass of FPDF to add a header
class PDF(FPDF):
    def __init__(self, orientation = "portrait", unit: float = "mm", format:  tuple[float, float] = "A4", font_cache_dir: Literal['DEPRECATED'] = "DEPRECATED") -> None:
        super().__init__(orientation, unit, format, font_cache_dir)
    def header(self):
        self.set_font("Helvetica", "B", 54)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(10)

# Create a PDF object
pdf = PDF(orientation="portrait", unit="mm", format="A4")
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Set font and size for the user's name

# Add the shirt image
image_path = "shirtificate.png"  # Replace with the path to your shirt image
img = Image.open(image_path)
img_width, img_height = img.size
pdf.image(image_path, x=(pdf.w - 200) / 2, y=pdf.get_y()+30, w=200)

pdf.set_font("Helvetica", "B", size=32)
# set font color to white
pdf.set_text_color(255, 255, 255)
user_name = input("Name: ")
user_name = f"{user_name} took CS50"

# Add user's name on top of the shirt
pdf.cell(0, 200, user_name, align="C")
# Output the PDF to a file
pdf_file_name = "shirtificate.pdf"
pdf.output(pdf_file_name)

