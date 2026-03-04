import os
import fnmatch
from collections import defaultdict

EXTENSION_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".rs": "Rust",
    ".php": "PHP",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".go": "Go",
    ".html": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".md": "Markdown",
    ".sh": "Shell"
}

COMMENT_MARKERS = {
    "Python": "#",
    "JavaScript": "//",
    "TypeScript": "//",
    "Rust": "//",
    "PHP": "//",
    "Java": "//",
    "C++": "//",
    "C": "//",
    "C#": "//",
    "Go": "//",
    "Shell": "#"
}

def load_gitignore_patterns(folder):
    gitignore_path = os.path.join(folder, ".gitignore")
    patterns = []

    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(line)

    return patterns

def matches_gitignore(path, patterns, base_folder):
    rel_path = os.path.relpath(path, base_folder).replace("\\", "/")

    for pattern in patterns:
        if pattern.endswith("/"):
            if rel_path.startswith(pattern.rstrip("/")):
                return True
        if fnmatch.fnmatch(rel_path, pattern):
            return True

    return False

def is_binary_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except:
        return True
    return False

def analyze_file(filepath, language):
    code_lines = 0
    comment_lines = 0

    marker = COMMENT_MARKERS.get(language)

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                stripped = line.strip()

                if not stripped:
                    continue  

                if marker and stripped.startswith(marker):
                    comment_lines += 1
                else:
                    code_lines += 1

    except:
        pass

    return code_lines, comment_lines

def main():
    root_folder = input("Enter folder path: ").strip()

    if not os.path.isdir(root_folder):
        print("Invalid folder path.")
        return

    totals = defaultdict(lambda: {"code": 0, "comments": 0})

    for current_root, dirs, files in os.walk(root_folder):
        patterns = load_gitignore_patterns(current_root)

        dirs[:] = [
            d for d in dirs
            if not matches_gitignore(os.path.join(current_root, d), patterns, current_root)
        ]

        for file in files:
            filepath = os.path.join(current_root, file)

            if matches_gitignore(filepath, patterns, current_root):
                continue

            if is_binary_file(filepath):
                continue

            _, ext = os.path.splitext(file)
            language = EXTENSION_MAP.get(ext.lower())

            if not language:
                continue

            code, comments = analyze_file(filepath, language)
            totals[language]["code"] += code
            totals[language]["comments"] += comments

    grand_total_code = sum(v["code"] for v in totals.values())

    print("\n========== Breakdown ==========\n")

    for language, data in sorted(totals.items(), key=lambda x: x[1]["code"], reverse=True):
        percent = (data["code"] / grand_total_code * 100) if grand_total_code else 0
        print(f"{language}: {percent:.1f}%")
        print(f"   Code lines: {data['code']}")
        print(f"   Comment lines: {data['comments']}")
        print()

    print("========== TOTAL ==========")
    print(f"Total Code Lines: {grand_total_code}")
    print(f"Total Comment Lines: {sum(v['comments'] for v in totals.values())}")

if __name__ == "__main__":
    main()