from pathlib import Path
import os

from extract_title import extract_title
from markdown_renderer import markdown_to_html_node  # your earlier work
from copy_static import copy_static                  # if you moved that helper

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} -> {dest_path} using {template_path}")

    # --- read markdown + template ---
    md_text   = Path(from_path).read_text(encoding="utf-8")
    template  = Path(template_path).read_text(encoding="utf-8")

    # --- convert markdown to HTML ---
    content_html = markdown_to_html_node(md_text).to_html()
    title        = extract_title(md_text)

    # --- merge into template ---
    page_html = (
        template
        .replace("{{ Title }}",   title)
        .replace("{{ Content }}", content_html)
    )

    # --- write output ---
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(page_html, encoding="utf-8")

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    content_root = Path(dir_path_content)
    template = Path(template_path)
    dest_root = Path(dest_dir_path)

    for md_file in content_root.rglob("*.md"):
        # Compute the relative path from content/
        rel_path = md_file.relative_to(content_root)
        # Change extension to .html
        dest_path = dest_root / rel_path.with_suffix(".html")
        # Make sure destination folder exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        generate_page(
            from_path=md_file,
            template_path=template,
            dest_path=dest_path,
        )
        print(f"✔ Generated: {md_file} -> {dest_path}")

