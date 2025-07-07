from functions.openrouter_call import call_openrouter

def main():
    chapter_processing = False
    while chapter_processing == False:
        chapter_processing_request = input('Have you palced your manuscript in ./working_dir/import? "Yes", "No"\nOption: ')
        chapter_processing_request.lower()
        if chapter_processing_request == "yes":
            chapter_processing = True
    


    # operation_request = input("What ")
    # call_openrouter()


if __name__ == "__main__":
    main()