import os
import shutil
from pathlib import Path


def copy_static(src_root: str = "static", dst_root: str = "public") -> None:
    """
    Recursively copy everything in `static/` into `public/`, creating
    directories as needed. Existing files are overwritten *only* when
    the source file is newer (based on modified-time).
    """
    src_root = Path(src_root)
    dst_root = Path(dst_root)

    if not src_root.exists():
        raise FileNotFoundError(f"{src_root} directory does not exist")

    for src_path in src_root.rglob("*"):
        rel_path = src_path.relative_to(src_root)
        dst_path = dst_root / rel_path

        if src_path.is_dir():
            dst_path.mkdir(parents=True, exist_ok=True)
        else:
            # Create parent dirs if they don’t exist
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            # Only copy if missing or out-of-date
            if (not dst_path.exists()
                    or src_path.stat().st_mtime > dst_path.stat().st_mtime):
                shutil.copy2(src_path, dst_path)

