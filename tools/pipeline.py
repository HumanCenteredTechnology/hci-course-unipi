import os
import re
import urllib.parse
import subprocess
import logging
from pypdf import PdfWriter, PdfReader

logging.getLogger("pypdf").setLevel(logging.ERROR)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# ==========================================
# CONFIGURAZIONI DELLA PIPELINE 
# ==========================================
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(TOOLS_DIR, ".."))

NOTES_DIR = os.path.join(ROOT_DIR, "course_notes")
README = os.path.join(ROOT_DIR, "README.md")
MASTER_PDF_FOLDER = os.path.join(NOTES_DIR, "[4] IUM Appunti Riassunti Completi")
MASTER_PDF_NAME = "Appunti_HCI_Riassunti_Completi.pdf"

EMOJI_FOLDER = "📁"
EMOJI_DOC_PDF = "📕"

def natural_sort_key(s):
    return[int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def url_encode_path(path):
    # La codifica URL definitiva e sicura (es. trasforma gli spazi in %20 senza corrompere gli slash)
    return urllib.parse.quote(path.replace("\\", "/"), safe="/")

def get_rel_link(target_path):
    rel_path = os.path.relpath(target_path, ROOT_DIR)
    return url_encode_path(rel_path)

def check_dependencies():
    try:
        subprocess.run(["pandoc", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except Exception:
        logging.warning("PANDOC non trovato.")
        
    try:
        subprocess.run(["soffice", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return "soffice"
    except Exception:
        try:
            subprocess.run(["libreoffice", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return "libreoffice"
        except Exception:
            logging.warning("LIBREOFFICE non trovato.")
            return None

# ==========================================
# CONVERSIONI
# ==========================================

def process_pptx(directory, lo_cmd):
    if not lo_cmd: return
    for root, _, files in os.walk(directory):
        if "Media_" in root: continue
        for file in files:
            if file.endswith(".pptx"):
                pptx_path = os.path.join(root, file)
                pdf_path = os.path.splitext(pptx_path)[0] + ".pdf"
                
                logging.info(f"Converting PPTX to PDF: {file}")
                try:
                    # Aggiunto --nologo per evitare blocchi nei server Linux
                    subprocess.run([lo_cmd, "--headless", "--nologo", "--nofirststartwizard", "--convert-to", "pdf", file, "--outdir", root],
                        cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
                        os.remove(pptx_path)
                        logging.info(f"PPTX originale eliminato: {file}")
                except subprocess.CalledProcessError as e:
                    logging.error(f"Errore nella conversione PPTX di {file}")

def process_markdown(directory):
    md_pdfs_generated =[]
    for root, _, files in os.walk(directory):
        if "Media_" in root: continue
        
        md_files =[f for f in files if f.endswith(".md") and f != "README.md" and "Appunti" not in f]
        for file in md_files:
            md_path = os.path.join(root, file)
            pdf_name = os.path.splitext(file)[0] + ".pdf"
            pdf_path = os.path.join(root, pdf_name)
            
            if not os.path.exists(pdf_path) or os.path.getmtime(md_path) > os.path.getmtime(pdf_path):
                logging.info(f"Converting MD to PDF: {file}")
                try:
                    # Ora usiamo wkhtmltopdf (via HTML). NESSUN crash per caratteri speciali!
                    cmd =[
                        "pandoc", file, "-o", pdf_name, 
                        "--pdf-engine=wkhtmltopdf", 
                        "-V", "margin-top=25mm", 
                        "-V", "margin-bottom=25mm", 
                        "-V", "margin-left=25mm", 
                        "-V", "margin-right=25mm"
                    ]
                    subprocess.run(cmd, cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except Exception as e:
                    # Nel caso Pandoc fallisca, riproviamo col motore standard (pdflatex) come fallback
                    try:
                        logging.warning(f"wkhtmltopdf fallito su {file}, tento con pdflatex...")
                        cmd_fallback =["pandoc", file, "-o", pdf_name, "--pdf-engine=pdflatex"]
                        subprocess.run(cmd_fallback, cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    except Exception:
                        logging.error(f"Errore DEFINITIVO Pandoc su {file}. Controlla i path delle immagini!")
                    
            if os.path.exists(pdf_path):
                md_pdfs_generated.append(pdf_path)
                
    return sorted(md_pdfs_generated, key=natural_sort_key)

def merge_pdfs(pdf_list, output_folder, output_filename):
    if not pdf_list: return
    logging.info(f"Merging {len(pdf_list)} files in {output_filename}...")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    merger = PdfWriter()
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except Exception:
            pass
            
    output_path = os.path.join(output_folder, output_filename)
    with open(output_path, "wb") as f_out:
        merger.write(f_out)

# ==========================================
# GESTIONE README
# ==========================================

def generate_table_navigation():
    lines =[
        "> 💡 **Nota:** Cliccando sui link alle cartelle dei moduli (📁) potrai accedere ai file Markdown originali usati per stilare gli appunti, alle relative cartelle contenenti le immagini, e ai PDF delle Slide.",
        "",
        "| Theme | Module | Notes |",
        "|-------|--------|-------|"
    ]
    
    themes =[d for d in os.listdir(NOTES_DIR) if os.path.isdir(os.path.join(NOTES_DIR, d)) and d.startswith("[") and "Appunti" not in d]
    themes.sort(key=natural_sort_key)
    
    for theme in themes:
        theme_path = os.path.join(NOTES_DIR, theme)
        theme_link = get_rel_link(theme_path)
        
        items = os.listdir(theme_path)
        modules =[d for d in items if os.path.isdir(os.path.join(theme_path, d)) and not d.startswith("Media_")]
        modules.sort(key=natural_sort_key)
        
        first_row = True
        
        for module in modules:
            module_path = os.path.join(theme_path, module)
            module_link = get_rel_link(module_path)
            files = os.listdir(module_path)
            
            md_bases =[f.replace(".md", "") for f in files if f.endswith(".md")]
            all_pdfs =[f for f in files if f.endswith(".pdf")]
            
            # Link esclusivamente ai PDF derivati dai markdown
            notes_links =[]
            for md_base in sorted(md_bases, key=natural_sort_key):
                pdf_version = f"{md_base}.pdf"
                if pdf_version in all_pdfs:
                    pdf_link = get_rel_link(os.path.join(module_path, pdf_version))
                    notes_links.append(f"{EMOJI_DOC_PDF}[{md_base}]({pdf_link})")
            notes_cell = "<br>".join(notes_links) if notes_links else "-"
            
            theme_cell = f"[{theme}]({theme_link})" if first_row else ""
            first_row = False
            
            lines.append(f"| {theme_cell} | {EMOJI_FOLDER} [{module}]({module_link}) | {notes_cell} |")
    
    return "\n".join(lines)

def update_readme(nav_text):
    if not os.path.exists(README):
        with open(README, "w", encoding="utf-8") as f:
            f.write("# Indice del Corso\n\n<!-- AUTO_NAV_START -->\n<!-- AUTO_NAV_END -->\n")
            
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()
    
    start = "<!-- AUTO_NAV_START -->"
    end = "<!-- AUTO_NAV_END -->"
    new_section = f"{start}\n\n### Repository Navigation\n{nav_text}\n\n{end}"
    
    if start in content and end in content:
        content = content.split(start)[0] + new_section + content.split(end)[1]
    else:
        content += "\n\n" + new_section
    
    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    logging.info("=== AVVIO PIPELINE ===")
    lo_cmd = check_dependencies()
    
    process_pptx(NOTES_DIR, lo_cmd)
    md_pdfs = process_markdown(NOTES_DIR)
    merge_pdfs(md_pdfs, MASTER_PDF_FOLDER, MASTER_PDF_NAME)
    
    nav_text = generate_table_navigation()
    update_readme(nav_text)
    logging.info("=== PIPELINE COMPLETATA ===")

if __name__ == "__main__":
    main()