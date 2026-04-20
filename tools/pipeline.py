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

MASTER_PDF_FOLDER = os.path.join(NOTES_DIR, "[4] Appunti Completi")
MASTER_PDF_NAME = "Appunti_Completi.pdf"

EMOJI_FOLDER = "📁"
EMOJI_DOC_PDF = "📕"
EMOJI_SLIDES = "📊"  # Reinserito per la nuova colonna

def natural_sort_key(s):
    return[int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def url_encode_path(path):
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
# TELEMETRIA E CONVERSIONI
# ==========================================

def get_stat(stats, root):
    """Inizializza il dizionario delle statistiche per una cartella se non esiste."""
    if root not in stats:
        stats[root] = {
            'pptx_found': 0, 'pptx_conv': 0, 'pptx_err': 0,
            'md_found': 0, 'md_conv': 0, 'md_err': 0,
            'initial_pdf_slides': 0, 'initial_pdf_notes': 0,
            'final_slides': 0, 'final_notes': 0
        }
    return stats[root]

def init_module_stats():
    """Censisce lo stato INIZIALE delle cartelle prima di qualsiasi operazione."""
    stats = {}
    if not os.path.exists(NOTES_DIR): return stats
    for theme in os.listdir(NOTES_DIR):
        theme_path = os.path.join(NOTES_DIR, theme)
        if not os.path.isdir(theme_path) or not theme.startswith("[") or "Appunti" in theme:
            continue
        for module in os.listdir(theme_path):
            module_path = os.path.join(theme_path, module)
            if not os.path.isdir(module_path) or module.startswith("Media_"):
                continue
            
            s = get_stat(stats, module_path)
            
            # Fotografia iniziale: Quanti MD e PDF ci sono già?
            files = os.listdir(module_path)
            md_bases =[f.replace(".md", "") for f in files if f.endswith(".md") and f != "README.md"]
            all_pdfs = [f for f in files if f.endswith(".pdf")]
            
            for pdf in all_pdfs:
                # Se c'è un MD col nome del PDF, è una nota. Altrimenti è una slide.
                if pdf.replace(".pdf", "") in md_bases:
                    s['initial_pdf_notes'] += 1
                else:
                    s['initial_pdf_slides'] += 1
                    
    return stats

def process_pptx(directory, lo_cmd, stats):
    if not lo_cmd: return
    for root, _, files in os.walk(directory):
        if "Media_" in root or "Appunti Completi" in root: continue
        for file in files:
            if file.endswith(".pptx"):
                s = get_stat(stats, root)
                s['pptx_found'] += 1
                
                pptx_path = os.path.join(root, file)
                pdf_path = os.path.splitext(pptx_path)[0] + ".pdf"
                
                logging.info(f"Converting PPTX to PDF: {file}")
                try:
                    subprocess.run([lo_cmd, "--headless", "--nologo", "--nofirststartwizard", "--convert-to", "pdf", file, "--outdir", root],
                        cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
                        os.remove(pptx_path)
                        s['pptx_conv'] += 1
                        logging.info(f"PPTX originale eliminato: {file}")
                    else:
                        s['pptx_err'] += 1
                except subprocess.CalledProcessError as e:
                    s['pptx_err'] += 1
                    logging.error(f"Errore nella conversione PPTX di {file}")

def process_markdown(directory, stats):
    md_pdfs_generated =[]
    for root, _, files in os.walk(directory):
        if "Media_" in root or "Appunti Completi" in root: continue
        
        md_files =[f for f in files if f.endswith(".md") and f != "README.md"]
        for file in md_files:
            s = get_stat(stats, root)
            s['md_found'] += 1
            
            md_path = os.path.join(root, file)
            pdf_name = os.path.splitext(file)[0] + ".pdf"
            pdf_path = os.path.join(root, pdf_name)
            
            if not os.path.exists(pdf_path) or os.path.getmtime(md_path) > os.path.getmtime(pdf_path):
                logging.info(f"Converting MD to PDF: {file}")
                try:
                    cmd =[
                        "pandoc", file, "-o", pdf_name, 
                        "--strip-comments",
                        "--webtex",
                        "--pdf-engine=wkhtmltopdf", 
                        "-V", "margin-top=25mm", 
                        "-V", "margin-bottom=25mm", 
                        "-V", "margin-left=40mm", 
                        "-V", "margin-right=40mm"
                    ]
                    subprocess.run(cmd, cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    s['md_conv'] += 1
                except Exception as e:
                    try:
                        logging.warning(f"wkhtmltopdf fallito su {file}, tento con pdflatex...")
                        cmd_fallback =[
                            "pandoc", file, "-o", pdf_name, 
                            "--strip-comments",
                            "--pdf-engine=pdflatex", 
                            "-V", "geometry:top=25mm,bottom=25mm,left=40mm,right=40mm"
                        ]
                        subprocess.run(cmd_fallback, cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        s['md_conv'] += 1
                    except Exception:
                        s['md_err'] += 1
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
# GESTIONE README E LOG FINALE
# ==========================================

def generate_table_navigation():
    master_pdf_link = get_rel_link(os.path.join(MASTER_PDF_FOLDER, MASTER_PDF_NAME))
    

    lines = [
        f"### 📚[👉 If you want to download the entire lecture notes in a single PDF, click here]({master_pdf_link})",
        "",
        "> 💡 **Note**: By clicking on the links to the module folders (📁) you can access the original Markdown files used to create the notes, the corresponding folders containing the images, and the PDFs of the slides.",
        "",
        "| Theme | Module | Notes | Slides |",
        "|-------|--------|-------|--------|"
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
            
            md_bases = [f.replace(".md", "") for f in files if f.endswith(".md")]
            all_pdfs = [f for f in files if f.endswith(".pdf")]
            
            # 1. Notes Links
            notes_links =[]
            for md_base in sorted(md_bases, key=natural_sort_key):
                pdf_version = f"{md_base}.pdf"
                if pdf_version in all_pdfs:
                    pdf_link = get_rel_link(os.path.join(module_path, pdf_version))
                    notes_links.append(f"{EMOJI_DOC_PDF}[{md_base}]({pdf_link})")
            notes_cell = "<br>".join(notes_links) if notes_links else "-"
            
            # 2. Slides Links
            slide_pdfs = [f for f in all_pdfs if f.replace(".pdf", "") not in md_bases]
            slides_links =[]
            for sp in sorted(slide_pdfs, key=natural_sort_key):
                sp_base = sp.replace(".pdf", "")
                sp_link = get_rel_link(os.path.join(module_path, sp))
                slides_links.append(f"{EMOJI_SLIDES} [{sp_base}]({sp_link})")
            slides_cell = "<br>".join(slides_links) if slides_links else "-"
            
            theme_cell = f"[{theme}]({theme_link})" if first_row else ""
            first_row = False
            
            lines.append(f"| {theme_cell} | {EMOJI_FOLDER}[{module}]({module_link}) | {notes_cell} | {slides_cell} |")
    
    return "\n".join(lines)

def update_readme(nav_text):
    if not os.path.exists(README):
        with open(README, "w", encoding="utf-8") as f:
            f.write("# Indice del Corso\n\n<!-- AUTO_NAV_START -->\n<!-- AUTO_NAV_END -->\n")
            
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()
    
    start = "<!-- AUTO_NAV_START -->"
    end = "<!-- AUTO_NAV_END -->"
    new_section = f"{start}\n\n## Repository Navigation\n\n{nav_text}\n\n{end}"
    
    if start in content and end in content:
        before = content.split(start)[0]
        after = content.split(end)[1]
        content = before + new_section + after
    else:
        content += "\n\n" + new_section
    
    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

def print_execution_summary(stats):
    print("\n" + "="*100)
    print("📊 RIEPILOGO GRANULARE ESECUZIONE PIPELINE GITHUB ACTIONS 📊".center(100))
    print("="*100)
    
    for root in sorted(stats.keys(), key=natural_sort_key):
        # Calcolo situazione PDF Finali Uscenti
        files = os.listdir(root)
        md_bases =[f.replace(".md", "") for f in files if f.endswith(".md") and f != "README.md"]
        all_pdfs = [f for f in files if f.endswith(".pdf")]
        
        for pdf in all_pdfs:
            if pdf.replace(".pdf", "") in md_bases:
                stats[root]['final_notes'] += 1
            else:
                stats[root]['final_slides'] += 1
        
        rel_path = os.path.relpath(root, NOTES_DIR).replace(os.sep, ' / ')
        s = stats[root]
        
        print(f"\n📁 {rel_path}")
        print(f"   ▶ SLIDES : Inizio [{s['pptx_found']} PPTX, {s['initial_pdf_slides']} PDF]  -->  Convertiti: {s['pptx_conv']} | Errori: {s['pptx_err']} || Fine: {s['final_slides']} PDF totali (Slides)")
        print(f"   ▶ NOTES  : Inizio [{s['md_found']} MD, {s['initial_pdf_notes']} PDF]    -->  Convertiti: {s['md_conv']} | Errori: {s['md_err']} || Fine: {s['final_notes']} PDF totali (Notes)")
        
    print("\n" + "="*100 + "\n")

def main():
    logging.info("=== AVVIO PIPELINE ===")
    lo_cmd = check_dependencies()
    
    # 0. Inizializza statistiche scattando la FOTOGRAFIA INIZIALE della repo
    stats = init_module_stats()
    
    # 1. Processa tutto
    process_pptx(NOTES_DIR, lo_cmd, stats)
    md_pdfs = process_markdown(NOTES_DIR, stats)
    
    # 2. Merge e UI
    merge_pdfs(md_pdfs, MASTER_PDF_FOLDER, MASTER_PDF_NAME)
    nav_text = generate_table_navigation()
    update_readme(nav_text)
    
    # 3. Confronto e Stampa Log
    print_execution_summary(stats)
    logging.info("=== PIPELINE COMPLETATA CON SUCCESSO ===")

if __name__ == "__main__":
    main()