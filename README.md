# Sarah: AI Developmental Editor for Fiction Authors

Sarah is an **AI-powered editing assistant** designed to help fiction authors refine their manuscripts with professional-grade insights. It automates chapter parsing, beat sheet analysis, line editing, and developmental feedback to support your storytelling and publishing goals.

---

## ✨ Key Features

✅ **Manuscript Upload & Processing**
- Accepts `.docx` files.
- Extracts title and creates project directories for organized outputs.
- Splits manuscripts into chapters based on `Heading 1` structure.
- Preserves rich text formatting (**bold**, _italics_, <u>underline</u>).

📝 **Editing Options**
- **Line Editing** tailored to:
  - Genre & subgenre
  - Tense (past/present)
  - Point of View (1st, 3rd limited, 3rd omniscient)

- **Developmental Editing** providing deep, actionable feedback:
  - Full novel analysis
  - Beat sheet creation
  - Act-level and chapter-level developmental edits

⚡ **Output & Downloads**
- Generates clean `.md` files for each chapter.
- Saves Beat Sheets, Manuscript Developmental Edits, and Chapter Edits.
- Designed for easy conversion back to `.docx`, `.epub`, or print-ready formats.

---

## 🚧 Project Status

Sarah is under **active development** with core functionality in place:

- ✅ `.docx` upload and chapter splitting
- ✅ Beat Sheet generation
- ✅ Manuscript Developmental Editing
- ✅ Chapter Developmental Editing
- 🛠️ CLI-based workflow (GUI planned for future)
- 📦 Export features to organized directories

---

## 🔧 Installation

**Requirements**
Ensure you have Python 3.10+ and install dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies:**
- python-dotenv
- openai
- python-docx
- markdownify

## 🚀 Usage
1. Prepare Your Manuscript
    - Place your .docx file in the ./working_dir/import folder.
2. Run Sarah
```bash
python main.py
```

3. Follow CLI Prompts
    - Select genre, tense, POV, and your main character.
    - Generate your Beat Sheet first.
    - Proceed to Manuscript Developmental Editing.
    - Process individual chapter edits as desired.
4. Retrieve Outputs
    - Edited files are saved in ./working_dir/export for easy integration back into your manuscript workflow.

---

## ⚠️ Note on Prompts & Guidelines
This project uses a modular prompting system. You must provide your own:
- guidelines.py
This file defines your editing guidelines and examples to guide the LLM according to your editorial style or genre expectations.

---

## 🛠️ Project Structure
```bash
Sarah/
├── main.py
├── requirements.txt
├── functions/
│   ├── process_chapter.py
│   └── openrouter_call.py
├── prompts/
│   └── prompt.py
│   └── guidelines.py*
├── working_dir/
│   ├── import/
│   ├── export/
│   └── markdown/
└── .env
└── README.md
```
---

## 🔑 Environment Variables
Create a .env file with your credentials:

```ini
OPENROUTER_API_KEY=your_openrouter_api_key
ACONITE_CAFE_CODE=your_verification_code
```
---

## 📅 Roadmap
- GUI-based interface for easier usage
- EPUB export integration
- Enhanced error handling and validation
- Author-focused SaaS deployment
---

## 📄 License
This project is currently proprietary to Aconite Cafe for internal author tooling. Licensing terms for external use are pending.

---

## 💡 Credits

Sarah is developed by Aconite Cafe, combining AI editing expertise with indie author publishing experience to create tools that empower storytellers.

“Helping authors tell better stories, one AI edit at a time.”
