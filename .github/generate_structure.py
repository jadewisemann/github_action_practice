import os

def generate_structure(path="src", prefix=""):
    entries = sorted(os.listdir(path))
    lines = []
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = i == len(entries) - 1

        icon = "📂" if os.path.isdir(full_path) else "📜"
        connector = "┗━ " if is_last else "┣━ "
        lines.append(f"{prefix}{connector}{icon} {entry}")

        if os.path.isdir(full_path):
            next_prefix = prefix + ("    " if is_last else "┃   ")
            lines.extend(generate_structure(full_path, prefix=next_prefix))

    return lines

if __name__ == "__main__":
    output = ["📦 src"] + generate_structure("src")

    with open("README.md", "r", encoding="utf-8") as readme:
        content = readme.read()

    tree_section_start = content.find("## tree")
    if tree_section_start != -1:
        content = content[:tree_section_start] + "## tree\n" + "\n".join(output) + content[tree_section_start + 7:]

    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(content)
