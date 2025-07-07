import os
import time
import threading
import itertools
import sys
from functions.openrouter_call import call_openrouter
from functions.process_chapter import process_chapter

def run_with_spinner(message, target_func, *args, **kwargs):
    result_container = {'result': None}
    def thread_target():
        result_container['result'] = target_func(*args, **kwargs)
    thread = threading.Thread(target=thread_target)
    thread.start()
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    start_time = time.time()
    sys.stdout.write(f"{message}... ")
    sys.stdout.flush()
    while thread.is_alive():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    thread.join()
    end_time = time.time()
    sys.stdout.write('\b \b')
    print(f"Done in {end_time - start_time:.2f} seconds.")
    return result_container['result']

def find_latest_file(directory, prefix, manuscript_basename):
    try:
        matching_files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.startswith(prefix) and manuscript_basename in f
        ]
        if not matching_files:
            return None
        return sorted(matching_files, key=os.path.getmtime, reverse=True)[0]
    except FileNotFoundError:
        return None

def main():
    # --- Part 1: One-Time Setup ---
    print("--- Welcome to Sarah, your AI Editor ---")
    chapter_processing = False
    while not chapter_processing:
        chapter_processing_request = input('Have you placed your manuscript in ./working_dir/import? "Yes", "No"\nOption: ')
        chapter_processing_request = chapter_processing_request.lower()
        if chapter_processing_request == "yes":
            chapter_processing = True
        
    manuscript_file, chapter_files = process_chapter()

    if manuscript_file is None:
        print("Could not process manuscript. Exiting.")
        return
    
    manuscript_basename, _ = os.path.splitext(os.path.basename(manuscript_file))
    export_dir = os.path.join("working_dir", "export")
    
    # --- Parameter Collection ---
    print("\n--- Manuscript Parameters ---")
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

    tense_selection = input('What tense if your mansucript written in?\n1 -> Present\n2 -> Past\nSlection 1, or 2: ')
    if tense_selection == "1":
        tense = "Present"
    elif tense_selection == "2":
        tense = "Past"
    else:
        tense = "N/A"

    subgenre = "N/A"
    genre = "N/A"

    genre_selection = input('What genre is your manuscript?\n1 -> Romance\n2 -> Mystery\n3 -> Thriller\n4 -> Science Fiction\n5 -> Fantasy\n6 -> Horror\n Slection 1, 2, 3, 4, 5, or 6: ')
    if genre_selection == "1":
        genre = "Romance"
        subgenre_selection = input('Select your subgenre\n1 -> Contemporary\n2 -> Historical\n3 -> Paranormal\n4 -> Romantic Comedy\nSlection 1, 2, 3, or 4: ')
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
        subgenre_selection = input('Select your subgenre\n1 -> Cozy\n2 -> Detective\n3 -> Noir\n4 -> Paranormal\nSlection 1, 2, 3, or 4: ')
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
        subgenre_selection = input('Select your subgenre:\n1 -> Psychological\n2 -> Political\n3 -> Action\n4 -> Crime\n5 -> Legal\nSlection 1, 2, 3, 4, or 5: ')
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
        subgenre_selection = input('Select your subgenre\n1 -> Epic\n2 -> Urban\n3 -> Dark\n4 -> Sword & Sorcery\nSlection 1, 2, 3, or 4: ')
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

    # --- Part 2: Main Application Loop ---
    beat_sheet_path = find_latest_file(export_dir, "Beat_Sheet_", manuscript_basename)
    ms_dev_edit_path = find_latest_file(export_dir, "MS_Dev_Edit_", manuscript_basename)

    while True:
        # Display current status at the start of the loop
        print("\n" + "="*40)
        print("--- MAIN MENU ---")
        print(f"Manuscript: {manuscript_basename}")
        print(f"Beat Sheet:      {os.path.basename(beat_sheet_path) if beat_sheet_path else 'NOT CREATED'}")
        print(f"MS Dev Edit:     {os.path.basename(ms_dev_edit_path) if ms_dev_edit_path else 'NOT CREATED'}")
        print("="*40)
        
        print("Please choose an action:")
        print("1. Generate/Overwrite Beat Sheet")
        print("2. Generate/Overwrite Manuscript Developmental Edit")
        print("3. Process Individual Chapter's Developmental Edit")
        print("4. Exit")
        
        choice = input("Option: ")

        if choice == '1':
            if beat_sheet_path:
                if input("Beat Sheet already exists. Overwrite? (yes/no): ").lower() != 'yes':
                    continue
            beat_sheet_path = run_with_spinner(
                "Creating Beat Sheet",
                call_openrouter, 0, manuscript_file, parameters
            )

        elif choice == '2':
            if not beat_sheet_path:
                print("\nERROR: You must generate a Beat Sheet (Option 1) before this step.")
                time.sleep(2)
                continue
            if ms_dev_edit_path:
                if input("MS Dev Edit already exists. Overwrite? (yes/no): ").lower() != 'yes':
                    continue
            ms_dev_edit_path = run_with_spinner(
                "Creating Manuscript Dev Edit",
                call_openrouter, 1, manuscript_file, parameters, beat_sheet_path=beat_sheet_path
            )

        elif choice == '3':
            if not ms_dev_edit_path:
                print("\nERROR: You must generate a Manuscript Dev Edit (Option 2) before this step.")
                time.sleep(2)
                continue
            
            print("\n--- Starting Individual Chapter Processing ---")
            for chapter_path in chapter_files:
                clean_name = os.path.splitext(os.path.basename(chapter_path))[0]
                process_this = input(f'\nProcess "{clean_name}"? (yes/no): ').lower()
                if process_this == 'yes':
                    run_with_spinner(
                        f'Creating Dev Edit for {clean_name}',
                        call_openrouter, 2, chapter_path, parameters,
                        beat_sheet_path=beat_sheet_path,
                        ms_developmental_edit_path=ms_dev_edit_path
                    )
                    # You could add the delete confirmation logic back here if you wish
                else:
                    print(f'Skipping "{clean_name}".')
            print("\nFinished processing all selected chapters.")
            time.sleep(2)


        elif choice == '4':
            print("\nThank you for choosing to work with Sarah, your friendly AI editor!\nExiting.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
            time.sleep(2)

if __name__ == "__main__":
    main()