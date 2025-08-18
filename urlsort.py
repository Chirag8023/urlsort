#!/usr/bin/env python3
import argparse
from urllib.parse import urlparse

BANNER = """
\033[93m █████  █████           ████   █████████                      █████   \033[0m
\033[93m░░███  ░░███           ░░███  ███░░░░░███                    ░░███    \033[0m
\033[93m ░███   ░███  ████████  ░███ ░███    ░░░   ██████  ████████  ███████  \033[0m
\033[93m ░███   ░███ ░░███░░███ ░███ ░░█████████  ███░░███░░███░░███░░░███░   \033[0m
\033[93m ░███   ░███  ░███ ░░░  ░███  ░░░░░░░░███░███ ░███ ░███ ░░░   ░███    \033[0m
\033[93m ░███   ░███  ░███      ░███  ███    ░███░███ ░███ ░███       ░███ ███\033[0m
\033[93m ░░████████   █████     █████░░█████████ ░░██████  █████      ░░█████ \033[0m
\033[93m  ░░░░░░░░   ░░░░░     ░░░░░  ░░░░░░░░░   ░░░░░░  ░░░░░        ░░░░░  \033[0m \033[92mv1.0.1\033[0m

\033[93mUrlSort - tool to categorize URLs from tools like Katana, Waybackurls and Gau.\033[0m
\033[92mAuthor: @chirag8023\033[0m
"""

def get_file_extension(line):
    # Parse URL properly
    parsed = urlparse(line if line.startswith(('http://', 'https://')) else 'http://' + line)
    path = parsed.path
    if not path or path.endswith('/'):
        return None
    # Get last segment
    last_segment = path.split('/')[-1]
    if '.' in last_segment:
        return last_segment.split('.')[-1].upper()
    return None

def categorize_line(line):
    line = line.strip()
    if not line:
        return None, line

    # Free text if line contains spaces
    if ' ' in line:
        return "FREE FORM TEXT", line

    # Check for file extension
    ext = get_file_extension(line)
    if ext:
        return ext, line

    # Check for query parameters
    if '?' in line:
        return "ENDPOINT + PARAM", line

    # Otherwise, endpoint
    return "ENDPOINT", line

def process_lines(lines):
    categories = {}
    for line in lines:
        cat, full_line = categorize_line(line)
        if not cat:
            continue
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(full_line)
    return categories

def display_categories(categories, output_file=None):
    output_lines = []
    for cat, items in categories.items():
        heading = f"[{cat}]"
        print(heading)
        output_lines.append(heading)
        for item in items:
            print(item)
            output_lines.append(item)
        print()
        output_lines.append("")
    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(output_lines))

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="UrlSort CLI Tool categorizes URLs based on filetype, endpoints and endpoint + parameter.")
    parser.add_argument('-f', '--file', help='Input file with URLs')
    parser.add_argument('-d', '--data', help='Direct comma-separated URLs/data')
    parser.add_argument('-o', '--output', help='Output file (also prints to terminal)')
    args = parser.parse_args()

    lines = []
    if args.file:
        with open(args.file, 'r') as f:
            lines.extend(f.readlines())
    if args.data:
        lines.extend([item.strip() for item in args.data.split(',') if item.strip()])

    categories = process_lines(lines)
    display_categories(categories, args.output)

if __name__ == "__main__":
    main()
