import os
from docx import Document
from markdownify import markdownify as md

def process_chapter():
    import_dir = './working_dir/import'
    markdown_dir = './working_dir/markdown'

    if not os.path.exists(markdown_dir):
        os.makedirs(markdown_dir)

    files = os.listdir(import_dir)
    if not files:
        print("No manuscript found in ./working_dir/import")
        return

    for filename in files:
        filepath = os.path.join(import_dir, filename)

        if os.path.isfile(filepath) and filename.lower().endswith('.docx'):
            document = Document(filepath)
            markdown_lines = []
            for paragraph in document.paragraphs:
                style = paragraph.style.name.lower()
                md_line = ""

                # Check if Heading
                if "heading 1" in style:
                    md_line += f"# {paragraph.text}"
                elif "heading 2" in style:
                    md_line += f"## {paragraph.text}"
                else:
                    # Process runs within the paragraph for bold/italic
                    for run in paragraph.runs:
                        run_text = run.text
                        if run.bold:
                            run_text = f"**{run_text}**"
                        if run.italic:
                            run_text = f"_{run_text}_"
                        md_line += run_text

                markdown_lines.append(md_line)

            # Join all converted lines
            markdown_text = '\n\n'.join(markdown_lines)

            # Save full manuscript.md
            base_name, _ = os.path.splitext(filename)
            manuscript_md_filename = base_name + '.md'
            manuscript_md_path = os.path.join(markdown_dir, manuscript_md_filename)

            with open(manuscript_md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_text)

            print(f"Processed {filename} -> {manuscript_md_filename}")

    for filename in files:
        os.remove(os.path.join(import_dir, filename))
