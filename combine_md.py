#!/usr/bin/env python3
"""
Combine multiple Markdown files starting with a given prefix into one file.

Usage:
    python combine_md.py 02_05_ML_PipeLine
"""

import sys
from pathlib import Path

def clean_title(filename: str) -> str:
    """Convert filename to a nice title, removing prefix, extension, and underscores/brackets."""
    name = filename.stem  # without .md
    # Remove the prefix (everything up to and including the last underscore before content)
    # But simpler: just replace underscores with spaces and clean brackets
    title = name.replace('_', ' ')
    title = title.replace('[', '').replace(']', '')
    title = title.strip()
    # Capitalize words
    return title.title()

def main():
    if len(sys.argv) != 2:
        print("Usage: python combine_md.py <prefix>")
        print("Example: python combine_md.py 02_05_ML_PipeLine")
        sys.exit(1)

    prefix = sys.argv[1].strip()
    directory = Path(".")

    # Find all .md files starting with the prefix
    md_files = sorted(directory.glob(f"{prefix}*.md"))

    if not md_files:
        print(f"No .md files found starting with '{prefix}'")
        sys.exit(1)

    # Output file
    output_file = directory / f"{prefix}.md"

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(f"# {prefix.replace('_', ' ')}\n\n")
        
        for md_file in md_files:
            print(f"Adding: {md_file.name}")
            title = clean_title(md_file)
            outfile.write(f"# {title}\n\n")
            
            try:
                content = md_file.read_text(encoding="utf-8")
                outfile.write(content)
                # Ensure at least one blank line between sections
                if not content.endswith('\n'):
                    outfile.write('\n')
                outfile.write('\n')
            except Exception as e:
                print(f"Error reading {md_file.name}: {e}")

    print(f"\nCombined file created: {output_file.name}")

if __name__ == "__main__":
    main()