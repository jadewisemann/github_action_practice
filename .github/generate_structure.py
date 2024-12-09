import os

def generate_structure(path="src", prefix=""):
    if not os.path.exists(path):
        return []

    entries = sorted(os.listdir(path))
    lines = []
    
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)

        if entry.startswith('.'):
            continue
        
        is_last = i == len(entries) - 1

        if os.path.isdir(full_path):
            icon = "📂"
            connector = "┗━ " if is_last else "┣━ "
            lines.append(f"{prefix}{connector}{icon} {entry}")

            next_prefix = prefix + ("    " if is_last else "┃   ")
            lines.extend(generate_structure(full_path, prefix=next_prefix))
        elif os.path.isfile(full_path):
            icon = "📜"
            connector = "┗━ " if is_last else "┣━ "
            lines.append(f"{prefix}{connector}{icon} {entry}")

    return lines

if __name__ == "__main__":
    output = generate_structure("src")

    with open("README.md", "r", encoding="utf-8") as readme:
        content = readme.read()

    tree_section_start = content.find("## tree")
    if tree_section_start != -1:
        content = content[:tree_section_start] + "## tree\n" + "```" + "\n" + "\n".join(output) + "\n```" + content[tree_section_start + 7:]

    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(content)
