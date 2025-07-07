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

    