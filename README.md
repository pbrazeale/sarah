# Sarah: Your AI Editor

Sarah is an AI-powered editing assistant designed to help fiction authors refine their manuscripts. 
1. It processes `.docx` files into clean, editable chapters. 
2. Applies intelligent line and developmental editing based on author preferences.
3. Delivers polished `.docx` output ready for download and formatting into epub/print.

---

## 🚧 Project Status
This project is currently in active development. Core functionality is being implemented in phases:
- ✅ `.docx` upload and chapter splitting
- 🔄 Editing pipeline (line and developmental)
- 🛠️ GUI for file handling and option selection
- 📦 Export features for download

---

## Features

### 📝 Upload Your Manuscript (`.docx`)
- **Title Extraction**: Automatically reads the document's title.
- **Project Directory**: Creates a new directory named after the title.
- **Safe Storage**: Saves a copy of the original `.docx` file for reference.
- **Chapter Parsing**:
    - Splits the manuscript by identifying `Heading 1` (`H1`) tags.
    - Each `H1` becomes a new file title.
    - Preserves rich text formatting like **bold**, _italics_, and <u>underline</u>.

---

### 🛠️ Editing Options
#### Line Editing
Customize editing based on your story’s tone and structure:
- **Genre Selection**: Tailors voice and pacing accordingly.
- **Tense**:
    - Past Tense
    - Present Tense
- **Point of View (POV)**:
    - 1st Person
    - 2nd Person
    - Limited 3rd Person
    - Omniscient 3rd Person

#### Developmental Editing
Provides feedback on story structure, pacing, and emotional arcs:
- Inherits all **Line Editing** options.
- Adjust scope of feedback:
    - **Full Novel** – Big-picture (beta reader-style)
    - **Plot-Level** – Feedback at the act-level
    - **Act-Level** – Scene-sequence level guidance
    - **Chapter-Level** – Detailed beat-by-beat analysis

---

### 📥 Output & Downloads
Get your edited content in the format that works best for you:
- **Individual Chapters** – Download chapter files separately.
- **Full Novel Compilation** – Reassembled and enhanced `.docx`.
