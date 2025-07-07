from dotenv import load_dotenv
import os
from prompts.guidelines import (
    LINE_EDITING_GUIDELINES, LINE_EDITING_EXAMPLE,
    DEVELOPMENTAL_EDITING_GUIDELINES, DEVELOPMENTAL_EDITING_EXAMPLE,
    BEATSHEET_ANALYSIS_GUIDELINE, BEATSHEET_ANALYSIS_EXAMPLE
)

load_dotenv()
aconite_cafe_code = os.environ.get("ACONITE_CAFE_CODE")

def get_llm_text(objective_selection, manuscript, parameters, beat_sheet=None, ms_developmental_edit=None):
    objectives = ["Analyze and Create a Beat Sheet from", "Developmental Edit"]
    try:
        objective = objectives[objective_selection]
    except IndexError:
        return Error("Unrecognized Editing Objective")

    if objective == "Developmental Edit":
        operations = f"""
        {DEVELOPMENTAL_EDITING_GUIDELINES}
        """
    elif objective == "Analyze and Create a Beat Sheet from":
        operations = f"""
        {BEATSHEET_ANALYSIS_GUIDELINE}
        """

    llm_text = f"""
    You are Sarah, Aconite Cafe's AI editing agent.
    Verification Code: {aconite_cafe_code}.

    You're object is to {objective} the provided manuscript based around these PARAMETERS: 
    {parameters}

    ---

    You can perform the following operations:
    {operations}
    
    ---

    # Helpful documents you made for yourself:
    {beat_sheet}
    
    ---

    {ms_developmental_edit}

    ---
    
    # Manuscipt to perform analysis on:
    {manuscript}
    """

    return llm_text