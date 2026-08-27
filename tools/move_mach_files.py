#!/usr/bin/env python3
"""Move Enzo machine makefiles to and from enzo-trash.

Run without --apply to preview file moves.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

EXCLUDED_FILES = {"Make.mach.linux-conda"}

def machine_files(source_root: Path, trash_root: Path, restore: bool) -> list[str]:
	root = trash_root if restore else source_root
	files = {
		path.name
		for path in root.glob("Make.mach.*")
		if path.is_file() and path.name not in EXCLUDED_FILES
	}
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

def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Preview or apply moves of Enzo machine makefiles."
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
	return parser.parse_args()

def main() -> None:
	args = parse_args()
	files = machine_files(args.enzo_root, args.trash_root, args.restore)
	if args.restore:
		restore_files(args.enzo_root, args.trash_root, files, args.apply)
	else:
		move_files(args.enzo_root, args.trash_root, files, args.apply)

if __name__ == "__main__":
	main()
