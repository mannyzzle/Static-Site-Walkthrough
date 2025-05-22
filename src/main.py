import shutil
from pathlib import Path

from page_generator import generate_page, generate_pages_recursive  # ✨ import both
from copy_static import copy_static

PUBLIC_DIR = Path("public")

# -------------------------------------------------
def clean_public() -> None:
    """Remove and re-create the public/ build directory."""
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir()
# -------------------------------------------------

def main() -> None:
    clean_public()                                     # 1. empty build dir
    copy_static("static", PUBLIC_DIR)                  # 2. copy assets
    print("Static assets copied!")

    # ✨ Use new recursive generator
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="public",
    )

    print("✔ All pages generated.")

if __name__ == "__main__":
    main()
