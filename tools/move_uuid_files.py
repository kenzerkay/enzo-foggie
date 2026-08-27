#!/usr/bin/env python3
"""Move Enzo machine makefiles to and from enzo-trash.

Run without --apply to preview file moves.
"""

from __future__ import annotations

import argparse

import shutil
from pathlib import Path

EXCLUDED_FILES = {"Make.mach.linux-conda"}

def uuid_files(source_root: Path, trash_root: Path, restore: bool) -> list[str]:
    root = trash_root if restore else source_root
    print(f"Looking for UUID files in: {root}")

    for path in root.rglob('*'):
        if path.is_file() and 'uuid' in path.as_posix().lower():
            print(f"Found file: {path.name} (at {path.relative_to(root)})")

    files = {
        path.relative_to(root).as_posix()
        for path in root.rglob('*')
        if path.is_file() and 'uuid' in path.as_posix().lower()
    }

    print(files)
    return sorted(files)

def move_files(source_root: Path, trash_root: Path, files: list[str], apply: bool) -> None:
	for filename in files:
		source = source_root / filename
		destination = trash_root / filename
		if not source.exists():
			print(f"missing: {source}")
			continue
		if destination.exists():
			raise SystemExit(f"Refusing to overwrite existing file: {destination}")
		print(f"move: {source} -> {destination}")
		if apply:
			trash_root.mkdir(parents=True, exist_ok=True)
			shutil.move(str(source), str(destination))

def restore_files(source_root: Path, trash_root: Path, files: list[str], apply: bool) -> None:
	for filename in files:
		source = trash_root / filename
		destination = source_root / filename
		if not source.exists():
			print(f"missing from trash: {source}")
			continue
		if destination.exists():
			raise SystemExit(f"Refusing to overwrite existing file: {destination}")
		print(f"restore: {source} -> {destination}")
		if apply:
			source_root.mkdir(parents=True, exist_ok=True)
			shutil.move(str(source), str(destination))

def object_files_for_sources(files: list[str]) -> list[str]:
    return list(dict.fromkeys(
        str(Path(filename).with_suffix(".o"))
        for filename in files
        if filename.endswith(".C")
    ))


def remove_object_entries(manifest: Path, files: list[str], apply: bool) -> None:
    object_files = set(object_files_for_sources(files))
    if not manifest.exists():
        raise SystemExit(f"Manifest not found: {manifest}")

    original_lines = manifest.read_text().splitlines(keepends=True)
    kept_lines = []
    removed = []
    for line in original_lines:
        object_name = line.strip().rstrip("\\").strip()
        if object_name in object_files:
            removed.append(object_name)
        else:
            kept_lines.append(line)

    for object_name in sorted(removed):
        print(f"remove manifest entry: {object_name} from {manifest}")

    if apply and removed:
        manifest.write_text("".join(kept_lines))

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or apply moves of ENZO UUID files."
    )
    parser.add_argument(
        "--enzo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "src" / "enzo",
        help="Enzo source directory (default: ../src/enzo relative to this script).",
    )
    parser.add_argument(
        "--trash-root",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "enzo-trash",
        help="Archive directory (default: workspace-level enzo-trash).",
    )
    parser.add_argument(
        "--restore",
        action="store_true",
        help="Restore files from enzo-trash instead of moving them there.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually perform the moves. Without this flag, only preview them.",
    )
    parser.add_argument(
        "--update-manifest",
        action="store_true",
        help="Remove mapped .o entries from Make.config.objects.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Make.config.objects path (default: ../src/enzo/Make.config.objects).",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    files = uuid_files(args.enzo_root, args.trash_root, args.restore)
    if args.update_manifest:
        manifest = args.manifest or args.enzo_root / "Make.config.objects"
        remove_object_entries(manifest, files, args.apply)
    if args.restore:
        restore_files(args.enzo_root, args.trash_root, files, args.apply)
    else:
        move_files(args.enzo_root, args.trash_root, files, args.apply)

if __name__ == "__main__":
	main()