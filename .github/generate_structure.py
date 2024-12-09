ref_element = "## Folder Structure"

import os

def generate_structure(path="src", prefix=""):
    entries = sorted(os.listdir(path))
    lines = []
    
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = i == len(entries) - 1

        icon = "📂" if os.path.isdir(full_path) else "📜"
        connector = "┗━ " if is_last else "┣━ "

        if i == 0 and prefix == "":
            lines.append(f"📦 src")
        lines.append(f"{prefix}{connector}{icon} {entry}")

        if os.path.isdir(full_path):
            next_prefix = prefix + ("    " if is_last else "┃   ")
            lines.extend(generate_structure(full_path, prefix=next_prefix))

    return lines

if __name__ == "__main__":
    output = generate_structure("src")

    with open("README.md", "r", encoding="utf-8") as readme:
        content = readme.read()

    tree_section_start = content.find(ref_element)
    if tree_section_start != -1:
        content = content[:tree_section_start + len(ref_element)] + "\n" + "```" + "\n" + "\n".join(output) + "\n```" + content[tree_section_start + len(ref_element):]
    else:
        content += "\n" + ref_element + "\n" + "```" + "\n" + "\n".join(output) + "\n```"

    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(content)
