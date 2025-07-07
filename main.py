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
    
    parameters = parameters()
    
    # Start of Developmental Edit
    beat_sheet_path = None
    ms_dev_edit_path = None
    
    # 1. Create Beat Sheet
    bs_dev_edit_request = input('\nWould you like to create a developmental edit report for the FULL manuscript? If Yes, I will start with a Beat Sheet. "Yes", "No"\nOption: ').lower()
    if bs_dev_edit_request == "yes":
         beat_sheet_path = run_with_spinner(
            "Creating Beat Sheet for the Full Manuscript",
            call_openrouter,
            0, manuscript_file, parameters
        )
    else:
        print("Skipping Beat Sheet creation, and exiting...")
        sys.exit()


    # 2. Create Full Manuscirpt Developmental Edit
    ms_dev_edit_request = input('\nPlease read the provided Beat Sheet and verify it captures your manuscripts plot?\nIf Yes, would you like a full manuscript Developmental Edit. "Yes", "No"\nOption: ').lower()
    if ms_dev_edit_request == "yes":
        ms_dev_edit_path = run_with_spinner(
            "Creating Developmental Edit for the Full Manuscript",
            call_openrouter,
            1, manuscript_file, parameters, beat_sheet_path=beat_sheet_path
        )
    else:
        print("Skipping full manuscript Developmental Edit.")

    # 3. Chapter by Chatper Developmental Edit 
    chapter_edit_request = input('\nWould you like to create a developmental edit for individual chapters? "Yes", "No"\nOption: ').lower()        
    if chapter_edit_request == "yes":
        print("\n--- Starting Individual Chapter Processing ---")
        for chapter_path in chapter_files:
            base_name = os.path.basename(chapter_path)
            clean_name, _ = os.path.splitext(base_name)

            process_this_chapter = input(f'\nCreate developmental edit for "{clean_name}"? "Yes", "No"\nOption: ').lower()

            if process_this_chapter == 'yes':
                # Call run_with_spinner for each chapter
                run_with_spinner(
                    f'Creating Developmental Edit for {clean_name}',
                    call_openrouter,
                    2, # CORRECTED: Use objective 2 for chapter-level developmental edits
                    chapter_path,
                    parameters,
                    beat_sheet_path=beat_sheet_path,
                    ms_developmental_edit_path=ms_dev_edit_path
                )
            else:
                print(f'Skipping "{clean_name}".')

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
        print("Skipping individual chapter edits.")


print("\nAll tasks complete....\nThank you for choosing to work with Sarah, your friendly AI editor!\nExiting.")

if __name__ == "__main__":
    main()