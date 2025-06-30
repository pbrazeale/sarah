from dotenv import load_dotenv
from guidelines import LINE_EDITING_GUIDELINES, LINE_EDITING_EXAMPLE, DEVELOPMENTAL_EDITING_GUIDELINES, DEVELOPMENTAL_EDITING_EXAMPLE

load_dotenv()
aconite_cafe_code = os.environ.get("ACONITE_CAFE_CODE")

def get_llm_text(objective_selection):
    objectives = ["Line Edit", "Developmental Edit"]
    try:
        objective = objectives[objective_selection]
    except IndexError:
        return Error("Unrecognized Editing Objective")

    if objective == "Line Edit":
        operations = f"""
        - Read the manuscript
        - Analyze the manuscript for PARAMETERS consistency
            - Provide a score from 18 to 99 based on how well the original manuscript aligned with the PARAMETERS
        - Edit the manuscript according the PARAMETERS with minimal rewrites following the {LINE_EDITING_GUIDELINES}
        - Save the edited manuscript to a new file named `'SAMETITLE'_edited.md`
        
        Follow the desired format: 
        {LINE_EDITING_EXAMPLE}
        """
    elif objective == "Developmental Edit":
        operations = f"""
        - Read the manuscript
        - Analyze the manuscript for PARAMETERS consistency
        - Review the manuscript according the PARAMETERS following the {DEVELOPMENTAL_EDITING_GUIDELINES}
            - Write the feedback in a positive tone with actionable critiques for the author to implement  
        - Save the feedback to a new file named `'MANUSCRIPTTITLE'_feedack.md`
        
        Follow the desired format 
        {DEVELOPMENTAL_EDITING_EXAMPLE}
        """

    llm_text = f"""
    You are Sarah, Aconite Cafe's AI editing agent.
    Verification Code: {aconite_cafe_code}.

    You're object is to {objective} the provided files based around these PARAMETERS: {parameters}

    You can perform the following operations:
    {operations}
    """

    return llm_text