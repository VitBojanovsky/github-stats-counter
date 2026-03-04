# Coding Stats Counter

This is a Python script that counts how many lines of code you have written and breaks them down by language.

## Function

The script **does not read your code from GitHub**. It just scans all files in a single folder. For example, VS Code saves all of your code by default in `/source/repos`, so you enter this path, and in a few seconds it will count all the lines in all files in that folder.

## Output example
```shell
HTML: 82.6%
   Code lines: 88225
   Comment lines: 0

JSON: 7.3%
   Code lines: 7798
   Comment lines: 0

Rust: 4.4%
   Code lines: 4714
   Comment lines: 361

JavaScript: 1.6%
   Code lines: 1676
   Comment lines: 82

CSS: 1.3%
   Code lines: 1393
   Comment lines: 0

C#: 0.9%
   Code lines: 990
   Comment lines: 198

Python: 0.7%
   Code lines: 723
   Comment lines: 52

PHP: 0.6%
   Code lines: 649
   Comment lines: 2

Markdown: 0.5%
   Code lines: 564
   Comment lines: 0

C++: 0.0%
   Code lines: 21
   Comment lines: 12

Shell: 0.0%
   Code lines: 5
   Comment lines: 2

========== TOTAL ==========
Total Code Lines: 106758
Total Comment Lines: 709
```

## Important Info

* If you have a `.gitignore` in a folder, it will **ignore the files listed in it**.
* If you collaborate on a project, it will count all lines, even the ones you didn’t write. I could add a filter for your contributions only, but I’m lazy. Most people keep their own projects in separate folders, so it’s probably not worth my time.

## Public Repo Cloner

This tool also allows you to **clone all your public repositories** into a selected folder — which is useful if you want to count them with the script.

## Previous Versions

* Previous versions of the counter script are less sophisticated.
* If you code in some “ancient” language, they might still count your lines, while version 3 might not.

## Requirements

* Git installed and added in path
* Python 3.7+
    * requests (for github clonner) `pip install requests`
