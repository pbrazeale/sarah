from dotenv import load_dotenv
import os
from prompts.guidelines import (
    LINE_EDITING_GUIDELINES, LINE_EDITING_EXAMPLE,
    DEVELOPMENTAL_EDITING_GUIDELINES, DEVELOPMENTAL_EDITING_EXAMPLE,
    BEATSHEET_ANALYSIS_GUIDELINE,
    CHAPTER_DEVELOPMENTAL_EDITING_GUIDELINES,
)

load_dotenv()
aconite_cafe_code = os.environ.get("ACONITE_CAFE_CODE")

def get_llm_text(objective_selection, manuscript_content, parameters, beat_sheet_content=None, ms_developmental_edit_content=None):
    objectives = [
        "Analyze the following manuscript and create a detailed Beat Sheet.",
        "Perform a full Developmental Edit on the following manuscript.",
        "Perform a Developmental Edit on the following book chapter."
    ]
    try:
        objective = objectives[objective_selection]
    except IndexError:
        return "Error: Unrecognized Editing Objective"

    # Define guidelines and the main content header based on the objective
    if objective_selection == 0: # Beat Sheet
        guidelines = f"Guidelines:\n{BEATSHEET_ANALYSIS_GUIDELINE}"
        main_content_header = "### MANUSCRIPT FOR BEAT SHEET ANALYSIS"
    elif objective_selection == 1: # Full MS Dev Edit
        guidelines = f"Guidelines:\n{DEVELOPMENTAL_EDITING_GUIDELINES}"
        main_content_header = "### MANUSCRIPT FOR DEVELOPMENTAL EDIT"
    elif objective_selection == 2: # Chapter Dev Edit
        guidelines = f"Guidelines:\n{CHAPTER_DEVELOPMENTAL_EDITING_GUIDELINES}"
        main_content_header = "### CHAPTER FOR DEVELOPMENTAL EDIT" # <-- Key change for clarity
    else:
        guidelines = "No specific guidelines provided."
        main_content_header = "### CONTENT FOR ANALYSIS"

    # Build the context section only if content is provided
    context_parts = []
    if beat_sheet_content:
        context_parts.append(f"### CONTEXT: Manuscript Beat Sheet\n---\n{beat_sheet_content}")
    if ms_developmental_edit_content:
        context_parts.append(f"### CONTEXT: Manuscript-Level Developmental Edit\n---\n{ms_developmental_edit_content}")
    
    context_section = "\n\n".join(context_parts)
    if context_section:
        context_section = f"---\n\n{context_section}\n\n"

    # Format parameters into a readable string
    parameters_text = "\n".join([f"- {key}: {value}" for key, value in parameters.items()])

    llm_text = f"""You are Sarah, Aconite Cafe's AI editing agent.
    Verification Code: {aconite_cafe_code}.

    Your objective is to: {objective}

    Use these manuscript parameters to guide your analysis:
    {parameters_text}

    {guidelines}
    {context_section}
    ---
    {main_content_header}
    ---
    {manuscript_content}
"""
    return llm_text