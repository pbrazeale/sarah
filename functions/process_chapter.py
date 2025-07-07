import os
from docx import Document

def process_chapter():
    import_dir = './working_dir/import'
    markdown_dir = './working_dir/markdown'

    if not os.path.exists(markdown_dir):
        os.makedirs(markdown_dir)

    files = os.listdir(import_dir)
    if not files:
        print("No manuscript found in ./working_dir/import")
        return None, []

    for filename in files:
        filepath = os.path.join(import_dir, filename)

        if os.path.isfile(filepath) and filename.lower().endswith('.docx'):
            document = Document(filepath)
            markdown_lines = []
            title_text = ""

            for paragraph in document.paragraphs:
                style = paragraph.style.name.lower()
                md_line = ""

                if "title" in style:
                    title_text = paragraph.text.strip()
                    continue
                elif "heading 1" in style:
                    md_line += f"# {paragraph.text.strip()}"
                elif "heading 2" in style:
                    md_line += f"## {paragraph.text.strip()}"
                else:
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

            # Split into chapters and capture returned chapter file paths
            chapter_files = split_into_chapters(markdown_text, base_name, markdown_dir, title_text)

    # Clear import directory after processing
    # for filename in files:
    #     os.remove(os.path.join(import_dir, filename))

    return manuscript_md_path, chapter_files


def split_into_chapters(markdown_text, manuscript_title, output_dir, title_text):
    chapters = []
    current_chapter = []
    lines = markdown_text.split('\n')
    created_chapter_files = []

    title_skipped = False

    for line in lines:
        if line.startswith('# '):
            heading_text = line[2:].strip()

            if not title_skipped and title_text and heading_text == title_text:
                print(f"Skipping title heading: {line}")
                title_skipped = True
                continue

            if current_chapter:
                chapters.append(current_chapter)

            current_chapter = [line]
        else:
            if current_chapter:
                current_chapter.append(line)

    if current_chapter:
        chapters.append(current_chapter)

    # Write each chapter to its own .md file and record file paths
    for idx, chapter_lines in enumerate(chapters, start=1):
        # Skip creating files for empty chapters
        if not any(line.strip() for line in chapter_lines):
            continue

        chapter_filename = f"Chapter {idx} {manuscript_title}.md"
        chapter_path = os.path.join(output_dir, chapter_filename)

        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(chapter_lines))

        created_chapter_files.append(chapter_path)
        print(f"Created {chapter_filename}")

    return created_chapter_files
