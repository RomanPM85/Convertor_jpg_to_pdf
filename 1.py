import os
import PIL.Image

from PyPDF2 import PdfFileMerger
from pathlib import Path

def img2pdf(fname):
    filename = fname
    name = filename.split('.')[0]
    im = PIL.Image.open(filename)
    if not os.path.exists('output_folder'):
        os.makedirs('output_folder')
    newfilename = ''.join(['output_folder/',name,'.pdf'])
    PIL.Image.Image.save(im, newfilename, "PDF", resolution = 100.0)
    print("processed successfully: {}".format(newfilename))

files = [f for f in os.listdir('./') if f.endswith('.jpg')]
for fname in files:
    img2pdf(fname)

pdf_merger = PdfFileMerger()
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