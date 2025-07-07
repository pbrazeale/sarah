
# Create parameters
def parameters():
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

    genre_selection = input('What genre is your manuscript? "1: Romance", "2: Mystery", "3: Thriller", "4: Science Fiction", "5: Fantasy", "6: Horror"\n Slection 1, 2, 3, 4, 5, or 6: ')
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

    return parameters