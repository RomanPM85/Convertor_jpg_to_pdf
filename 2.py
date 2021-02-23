from PyPDF2 import PdfFileMerger
pdf_merger = PdfFileMerger()

from pathlib import Path
reports_dir = (
    Path.cwd()
    / "im2pdf_output"
)
im2pdf_output= list(reports_dir.glob("*.pdf"))
im2pdf_output.sort()

for path in im2pdf_output:
    print(path.name)

for path in im2pdf_output:
    pdf_merger.append(str(path))

with Path("merges.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)