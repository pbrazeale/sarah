import os
import time
from functions.openrouter_call import call_openrouter
from functions.process_chapter import process_chapter

def main():
    # Initial processing from .docx -> .md for cleaner LLM interface
    chapter_processing = False
    while not chapter_processing:
        chapter_processing_request = input('Have you placed your manuscript in ./working_dir/import? "Yes", "No"\nOption: ')
        chapter_processing_request = chapter_processing_request.lower()
        if chapter_processing_request == "yes":
            chapter_processing = True
    
    manuscript_file, chapter_files = process_chapter()

    if manuscript_file is None:
        print("No manuscript processed. Exiting.")
        return
    
    # Create parameters
    pov_selection = input('What is your point of view:\n1 -> 1st person\n2 -> limited 3rd person\n3 -> omniscient 3rd person\nSlection 1, 2, or 3: ')
    if pov_selection == "1":
        POV = "1st person"
    elif pov_selection == "2":
        POV = "limited 3rd person"
    elif Ppov_selectionOV == "3":
        POV = "omniscient 3rd person"
    else:
        POV = "N/A"
    
    MC = input('What is the name of your main character? First name, or First and Last\nMain Character: ')

    tense_selection = input('What tense if your mansucript written in? "1: Present" or "2: Past"\nSlection 1, or 2: ')
    if tense_selection == "1":
        tense = "Present"
    elif tense_selection == "2":
        tense = "Past"
    else:
        tense = "N/A"

    subgenre = "N/A"
    genre = "N/A"

    genre_selection = input('What genre is your manuscript? "1: Romance", "2: Mystery", "3: Thriller", "4: Science Fiction", "5: Fantasy", "6: Horror"\n Genre: ')
    if genre_selection == "1":
        genre = "Romance"
        subgenre_selection = input('Select your subgenre: "1: Contemporary", "2: Historical", "3: Paranormal", "4: Romantic Comedy"\nSlection 1, 2, 3, or 4: ')
        if subgenre_selection == "1":
            subgenre = "Contemporary"
        elif subgenre_selection == "2":
            subgenre = "Historical"
        elif subgenre_selection == "3":
            subgenre = "Paranormal"
        elif subgenre_selection == "4":
            subgenre = "Romantic Comedy"
        else:
            subgenre = "N/A"
    elif genre_selection == "2":
        genre = "Mystery"
        subgenre_selection = input('Select your subgenre: "1: Cozy", "2: Detective", "3: Noir", "4: Paranormal"\nSlection 1, 2, 3, or 4: ')
        if subgenre_selection == "1":
            subgenre = "Cozy"
        elif subgenre_selection == "2":
            subgenre = "Detective"
        elif subgenre_selection == "3":
            subgenre = "Noir"
        elif subgenre_selection == "4":
            subgenre = "Paranormal"
        else:
            subgenre = "N/A"
    elif genre_selection == "3":
        genre = "Thriller"
        subgenre_selection = input('Select your subgenre: "1: Psychological", "2: Political", "3: Action", "4: Crime", "5: Legal"\nSlection 1, 2, 3, 4, or 5: ')
        if subgenre_selection == "1":
            subgenre = "Psychological"
        elif subgenre_selection == "2":
            subgenre = "Political"
        elif subgenre_selection == "3":
            subgenre = "Action"
        elif subgenre_selection == "4":
            subgenre = "Crime"
        elif subgenre_selection == "5":
            subgenre = "Legal"
        else:
            subgenre = "N/A"
    elif genre_selection == "4":
        genre = "Science Fiction"
    elif genre_selection == "5":
        genre = "Fantasy"
        subgenre_selection = input('Select your subgenre: "1: Epic", "2: Urban", "3: Dark", "4: Sword & Sorcery"\nSlection 1, 2, 3, or 4: ')
        if subgenre_selection == "1":
            subgenre = "Epic"
        elif subgenre_selection == "2":
            subgenre = "Urban"
        elif subgenre_selection == "3":
            subgenre = "Dark"
        elif subgenre_selection == "4":
            subgenre = "Sword & Sorcery"
        else:
            subgenre = "N/A"
    elif genre_selection == "6":
        genre = "Horror"
    else:
        genre = "N/A"    

    parameters = {
        "POV": POV,
        "main_character": MC,
        "tense": tense,
        "genre": genre,
        "subgenre": subgenre,
    }

    # Start of Developmental Edit
    beat_sheet_path = None
    ms_dev_edit_path = None
    
    # 1. Create Beat Sheet
    bs_dev_edit_request = input('\nWould you like to create a developmental edit report for the FULL manuscript? If Yes, I will start with a Beat Sheet. "Yes", "No"\nOption: ').lower()
    if bs_dev_edit_request == "yes":
        # Objective 0: Create the Beat Sheet. Capture the returned file path.
        beat_sheet_path = call_openrouter(0, manuscript_file, parameters)
        print(f"\n--- Creating Beat Sheet for the Full Manuscript ---")
        print(f"\n--- Please be patient ---")
        counter = 1
        while not beat_sheet_path:
            time.sleep(3)
            print(f"\n--- {coutner * 3} seconds: Still working. Thank you for your patiepatience. ---")
            counter += 1
        print(f"\n--- Beat Sheet for the Full Manuscript cerated in {coutner * 3} seconds ---")

    # 2. Create Full Manuscirpt Developmental Edit
    ms_dev_edit_request = input('\nPlease read the provided Beat Sheet and verify it captures your manuscripts plot?\nIf Yes, would you like a full manuscript Developmental Edit. "Yes", "No"\nOption: ').lower()
    if ms_dev_edit_request == "yes":
        ms_dev_edit_path = call_openrouter(1, manuscript_file, parameters, beat_sheet_path=beat_sheet_path)
        print("\n--- Creating Developmental Edit for the Full Manuscript ---")
        print(f"\n--- Please be patient ---")
        counter = 1
        while not ms_dev_edit_path:
            time.sleep(3)
            print(f"\n--- {coutner * 3} seconds: Still working. Thank you for your patiepatience. ---")
            counter += 1
        print(f"\n--- Developmental Edit for the Full Manuscript cerated in {coutner * 3} seconds ---")

    # 3. Chapter by Chatper Developmental Edit 
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
                call_openrouter(0, chapter_path, parameters, beat_sheet_path, ms_dev_edit_path)
                print(f"\n--- Creating Developmental Edit for {clean_name} ---")
                print(f"\n--- Please be patient ---")
                counter = 1
                while not ms_dev_edit_path:
                    time.sleep(3)
                    print(f"\n--- {coutner * 3} seconds: Still working. Thank you for your patiepatience. ---")
                    counter += 1
                print(f"\n--- Developmental Edit for {clean_name} cerated in {coutner * 3} seconds ---")

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

    print("\nAll tasks complete....\nThank you for chosing to work with Sharah your friendly AI editor!\nExiting.")

if __name__ == "__main__":
    main()