from pathlib import Path
import os

from extract_title import extract_title
from markdown_renderer import markdown_to_html_node  # your earlier work
from copy_static import copy_static                  # if you moved that helper

def generate_page(from_path, template_path, dest_path, base_path="/"):
    from markdown_renderer import markdown_to_html_node

    with open(template_path, "r") as f:
        template = f.read()

    with open(from_path, "r") as f:
        markdown = f.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = markdown.split("\n")[0].replace("# ", "").strip()

    out = template.replace("{{ Title }}", title)
    out = out.replace("{{ Content }}", html)

    #  Replace href/src absolute paths
    out = out.replace('href="/', f'href="{base_path}')
    out = out.replace('src="/', f'src="{base_path}')

    with open(dest_path, "w") as f:
        f.write(out)




def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, base_path: str) -> None:
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
            base_path=base_path,
        )
        print(f"✔ Generated: {md_file} -> {dest_path}")

