from functions.openrouter_call import call_openrouter
from functions.process_chapter import process_chapter

def main():
    chapter_processing = False
    while not chapter_processing:
        chapter_processing_request = input('Have you palced your manuscript in ./working_dir/import? "Yes", "No"\nOption: ')
        chapter_processing_request = chapter_processing_request.lower()
        if chapter_processing_request == "yes":
            chapter_processing = True
    
    manuscript_file, chapter_files = process_chapter()

    if manuscript_file is None:
        print("No manuscript processed. Exiting.")
        return

    create_developmental_edit = False
    while not create_developmental_edit:
        beat_sheet_request = input('Would you like to create a developmental edit report? "Yes", "No"\nOption: ')
        beat_sheet_request = beat_sheet_request.lower()
        if beat_sheet_request == "yes":
            create_developmental_edit = True
            call_openrouter(0, manuscript_file)
            call_openrouter(1, manuscript_file)


if __name__ == "__main__":
    main()