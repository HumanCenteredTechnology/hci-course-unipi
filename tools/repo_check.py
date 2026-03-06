import os
import urllib.parse

NOTES_DIR = "course_notes"
README = "README.md"

EMOJI_FOLDER = "📁"
EMOJI_DOC = "📄"

def url_encode_path(path):
    return urllib.parse.quote(path.replace("\\", "/"))

def generate_table_navigation():
    lines = [""] # ## Repository Navigation\n
    lines.append("| Theme | Module | Documents |")
    lines.append("|-------|--------|-----------|")
    
    themes = [d for d in os.listdir(NOTES_DIR) if os.path.isdir(os.path.join(NOTES_DIR, d))]
    themes.sort()
    
    for theme in themes:
        theme_path = os.path.join(NOTES_DIR, theme)
        theme_link = url_encode_path(theme_path)
        
        items = os.listdir(theme_path)
        modules = [d for d in items if os.path.isdir(os.path.join(theme_path, d)) and not d.startswith("Media_")]
        modules.sort()
        theme_docs = [f for f in items if f.endswith(".md")]
        
        first_row = True
        
        if theme_docs and not modules:
            doc_links = []
            for doc in theme_docs:
                doc_name = doc.replace(".md", "")
                doc_path = os.path.join(theme_path, doc)
                doc_link = url_encode_path(doc_path)
                doc_links.append(f"{EMOJI_DOC} [{doc_name}]({doc_link})")
            docs_line = " | ".join(doc_links)
            lines.append(f"| [{theme}]({theme_link}) |  | {docs_line} |")
        
        for module in modules:
            module_path = os.path.join(theme_path, module)
            module_link = url_encode_path(module_path)
            documents = [f for f in os.listdir(module_path) if f.endswith(".md")]
            documents.sort()
            
            doc_links = []
            for doc in documents:
                doc_name = doc.replace(".md", "")
                doc_path = os.path.join(module_path, doc)
                doc_link = url_encode_path(doc_path)
                doc_links.append(f"{EMOJI_DOC} [{doc_name}]({doc_link})")
            
            docs_line = " | ".join(doc_links) if doc_links else ""
            theme_cell = f"[{theme}]({theme_link})" if first_row else ""
            first_row = False
            
            lines.append(f"| {theme_cell} | {EMOJI_FOLDER} [{module}]({module_link}) | {docs_line} |")
    
    return "\n".join(lines)

def update_readme(nav_text):
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()
    
    start = "<!-- AUTO_NAV_START -->"
    end = "<!-- AUTO_NAV_END -->"
    new_section = f"{start}\n\n{nav_text}\n{end}"
    
    if start in content and end in content:
        before = content.split(start)[0]
        after = content.split(end)[1]
        content = before + new_section + after
    else:
        content += "\n\n" + new_section
    
    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    nav_text = generate_table_navigation()
    update_readme(nav_text)
    print("README aggiornato con tabella Tema/Modulo/Documenti!")

if __name__ == "__main__":
    main()