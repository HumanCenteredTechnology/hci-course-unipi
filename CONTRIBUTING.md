# Repository Guidelines & Contributing

This document describes how our automated pipeline works, how to contribute, and the structure/naming conventions you must follow.

---

## The Automated Pipeline (GitHub Actions)

You **do not** need to manually convert files to PDF or update the `README.md`. We have an automated bot (GitHub Actions) that does the heavy lifting for you every time you push your changes.

### How it works:
1. **Push your changes:** You upload a `.pptx` or a `.pdf` presentation, edit a `.md` note, or add images.
2. **The Bot wakes up:** As soon as you push to GitHub, the github server starts the pipeline.
3. **Magic happens (:D) :** 
   - **PPTX to PDF:** All `.pptx` files are converted to `.pdf` and **the original `.pptx` files are deleted** to keep the repo clean.
   - **MD to PDF:** All `.md` notes are converted to `.pdf` using `wkhtmltopdf`.
   - **Master PDF:** All notes are merged into a single master document in `[4] IUM Appunti Completi`.
   - **README Update:** The navigation table in the `README.md` is automatically updated with the new links.

### ⚠️ CRITICAL - PAY ATTENTION --> Always Pull <--
Because the bot modifies the repository (deletes PPTX, creates PDFs, updates README), **you MUST run `git pull`** on your local machine after the bot finishes its job (usually 1-2 minutes after your push). 
*If you don't pull, you will get merge conflicts on your next push!*

### 🛑 PAY ATTENTION --> Handling Presentations (PPTX updates) <--
Since the bot deletes PPTX files after conversion:
- **To update slides:** Upload the new `.pptx` with the **exact same name** as the existing `.pdf`. The bot will overwrite the old PDF.
**OR**
- **To rename/replace slides:** If you upload a PPTX with a new name, the bot will create a new PDF. You must **manually delete the old PDF** to avoid duplicates in the README table.

---

### TO ADD COMMENTS A MARKDONW DOC PLEASE USE:
`[//]: #` 
> If you use HTML to comment the comments WILL appear in the final PDF
---

## 📁 Repository Structure

The repository follows a strict hierarchy:
`Theme → Module → Document // Media`

### 1. Themes
Themes represent major conceptual areas.
- **Format:** `[Number] Name`
- **Example:** `[1] People`, `[2] User Experience`

### 2. Modules
Modules group lessons within a theme.
- **Format:** `Number - Name`
- **Example:** `0 - Methods`, `1 - Fundamental Principles of HCI`

### 3. Documents (Notes)
Each module contains a Markdown document AND PowerPoint documents AND EVENTUALLY pdfs.
- **Rules for markdown files:** No numbers at the start, no underscores, words separated by spaces.
- **Example:** `Fundamental Principles of HCI.md`
- **Rules for powerpoints:** use numbers in this format ("1 - ") before the powerpoint name to order them in the order they are presented in the markdown notes.
- **Example:** `1 - Fundamental Principles.pptx`

### 4. Media Folders
Each document has a dedicated media folder for images.
- **Rules:** Prefix `Media_`, spaces replaced with underscores, title must match the markdown document exactly.
- **Example:** `Media_Fundamental_Principles_of_HCI`

---

## 🛠️ Local Testing (Optional)

If you want to test the pipeline on your computer before pushing:
1. **Requirements:** Python 3.10+, `pypdf` library, Pandoc, wkhtmltopdf, and LibreOffice.
2. **Execution:** Run the following from the root of the repo:
   ```bash
   python tools/pipeline.py
   ```

>   (Warning: This will delete .pptx files on your local machine just like the server does!)