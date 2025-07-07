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
            full_text = []
            for paragraph in document.paragraphs:
                full_text.append(paragraph.text)
            text = '\n\n'.join(full_text)

            # Convert to markdown
            markdown_text = md(text)

            base_name, _ = os.path.splitext(filename)
            new_filename = base_name + '.md'
            output_path = os.path.join(markdown_dir, new_filename)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_text)

            print(f"Processed {filename} -> {new_filename}")

 