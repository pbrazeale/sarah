import os
from functions.openrouter_call import call_openrouter
from functions.process_chapter import process_chapter

def main():
    # Initial processing from .docx -> .md for cleaner LLM interface
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

    # Create parameters
    POV = input('What is your point of view:\n1 -> 1st person\n2 -> limited 3rd person\n3 -> omniscient 3rd person\nSlection 1, 2, or 3: ')
    if POV == 1:
        POV = "1st person"
    elif POV == 2:
        POV = "limited 3rd person"
    elif POV == 3:
        POV = "omniscient 3rd person"
    else:
        POV = "N/A"
    
    MC = input('What is the name of your main character? First name, or First and Last\nMain Character: ')

    tense = input('What tense if your mansucript written in? "Present" or "Past"\nTense: ')

    genre = input('What genre is your manuscript? "1: Romance", "2: Mystery", "3: Thriller", "4: Science Fiction", "5: Fantasy", "6: Horror"\n Genre:')
    if genre == 1:
        genre = "Romance"
        subgenre = input('Select your subgenre: "Contemporary", "Historical", "Paranormal", "Romantic Comedy"\nSubgenre:')
    elif genre == 2:
        genre = "Mystery"
        subgenre = input('Select your subgenre: "Cozy", "Detective", "Noir", "Paranormal"\nSubgenre:')
    elif genre == 3:
        genre = "Thriller"
        subgenre = input('Select your subgenre: "Psychological", "Political", "Action", "Crime", "Legal"\nSubgenre:')
    elif genre == 4:
        genre = "Science Fiction"
        subgenre = "N/A"
    elif genre == 5:
        genre = "Fantasy"
        subgenre = input('Select your subgenre: "Epic", "Urban", "Dark", "Sword & Sorcery"\nSubgenre:')
    elif genre == 6:
        genre = "Horror"
        subgenre = "N/A"
    
    parameters = {
        "POV": POV,
        "main_character": MC,
        "tense": tense,
        "genre": genre,
        "subgenre": subgenre,
    }
    # Start of Developmental Edit
    create_developmental_edit = False
    while not create_developmental_edit:
        beat_sheet_request = input('\nWould you like to create a developmental edit report for the FULL manuscript? "Yes", "No"\nOption: ')
        beat_sheet_request = beat_sheet_request.lower()
        if beat_sheet_request == "yes":
            create_developmental_edit = True
            print("\n--- Creating Developmental Edit for the Full Manuscript ---")
            # Creats the Beat_Sheet used moving forward
            call_openrouter(0, manuscript_file, parameters)
            # Creates the Main Developmental Edit Docuemnt used moving forward 
            call_openrouter(1, manuscript_file, parameters, beat_sheet_manuscript)

    # Chapter by Chatper Developmental Edit 
    chapter_edit_request = input('\nWould you like to create a developmental edit for individual chapters? "Yes", "No"\nOption: ').lower()
    
    if not chapter_files:
        print("\nNo individual chapters were found to process.")
        return
    
    if chapter_edit_request == "yes":
        print("\n--- Starting Individual Chapter Processing ---")
        for chapter_path in chapter_files:
            base_name = os.path.basename(chapter_path)
            clean_name, _ = os.path.splitext(base_name)

            process_this_chapter = input(f'\nCreate developmental edit for "{clean_name}"? "Yes", "No"\nOption: ').lower()

            if process_this_chapter == 'yes':
                print(f'Sending "{clean_name}" for developmental edit...')
                call_openrouter(0, chapter_path, parameters, beat_sheet_manuscript, developmental_edit_manuscript)

                # Ask for confirmation before deleting the source file
                confirm_delete = input('Happy with the generated report? "Yes" to delete the original chapter file from markdown/, "No" to keep it.\nOption: ').lower()
                if confirm_delete == 'yes':
                    try:
                        os.remove(chapter_path)
                        print(f'--> DELETED original chapter file: {chapter_path}')
                    except FileNotFoundError:
                        print(f'--> ERROR: Could not find file to delete: {chapter_path}')
                    except Exception as e:
                        print(f"--> ERROR: An unexpected error occurred while deleting file: {e}")
                else:
                    print(f'--> KEPT original chapter file: {chapter_path}')
            else:
                print(f'Skipping "{clean_name}".')

    print("\nAll tasks complete. Exiting.")

if __name__ == "__main__":
    main()