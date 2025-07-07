from functions.openrouter_call import call_openrouter
from functions.process_chapter import process_chapter

def main():
    chapter_processing = False
    while chapter_processing == False:
        chapter_processing_request = input('Have you palced your manuscript in ./working_dir/import? "Yes", "No"\nOption: ')
        chapter_processing_request.lower()
        if chapter_processing_request == "yes":
            chapter_processing = True
    
    process_chapter()

    create_developmental_edit = False
    while create_developmental_edit == False:
        beat_sheet_request = input('Would you like to create a developmental edit report? "Yes", "No"\nOption: ')
        beat_sheet_request.lower()
        if beat_sheet_request == "yes":
            create_developmental_edit = True
            call_openrouter(0)


if __name__ == "__main__":
    main()