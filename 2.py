from PyPDF2 import PdfFileMerger
pdf_merger = PdfFileMerger()

from pathlib import Path
reports_dir = (
    Path.cwd()
    / "output_folder"
)
output_folder= list(reports_dir.glob("*.pdf"))
output_folder.sort()

for path in output_folder:
    print(path.name)

for path in output_folder:
    pdf_merger.append(str(path))

with Path("merges.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)