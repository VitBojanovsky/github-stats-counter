import os

def is_binary_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except:
        return True
    return False

def count_lines_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except:
        return 0

def main():
    folder_path = input("Enter folder path: ").strip()

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    total_lines = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)

            if is_binary_file(filepath):
                continue

            lines = count_lines_in_file(filepath)
            total_lines += lines
            print(f"{filepath} -> {lines} lines")

    print("\n======================")
    print(f"TOTAL LINES: {total_lines}")

if __name__ == "__main__":
    main()