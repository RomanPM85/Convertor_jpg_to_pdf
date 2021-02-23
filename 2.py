from PyPDF2 import PdfFileMerger
pdf_merger = PdfFileMerger()

from pathlib import Path
reports_dir = (
    Path.cwd()
    / "im2pdf_output"
)

for path in reports_dir.glob("*.pdf"):
    print(path.name)