import shutil
import sys
from pathlib import Path

from page_generator import generate_pages_recursive
from copy_static import copy_static

# Destination folder for GitHub Pages
DOCS_DIR = Path("docs")

def clean_docs() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True)

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    clean_docs()
    copy_static("static", DOCS_DIR)
    print("Static assets copied!")

    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="docs",
        base_path=base_path,
    )
    print("✔ All pages generated into docs/")

if __name__ == "__main__":
    main()
