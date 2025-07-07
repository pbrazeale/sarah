from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime
from prompts.prompt import get_llm_text

load_dotenv()
openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")

def read_file_content(file_path):
  if not file_path or not os.path.exists(file_path):
    return None
  try:
    with open(file_path, "r", encoding="utf-8") as f:
      return f.read()
  except Exception as e:
    print(f"Error reading file {file_path}: {e}")
    return None

def call_openrouter(objective_selection, manuscript_path, parameters, beat_sheet_path=None, ms_developmental_edit_path=None):
  manuscript_content = read_file_content(manuscript_path)
  beat_sheet_content = read_file_content(beat_sheet_path)
  ms_dev_edit_content = read_file_content(ms_developmental_edit_path)

  if not manuscript_content:
    print(f"Could not read manuscript file: {manuscript_path}")
    return None

  llm_text = get_llm_text(objective_selection, manuscript_content, parameters, beat_sheet_content, ms_dev_edit_content)

  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key,
  )

  completion = client.chat.completions.create(
    model="openai/gpt-4.1",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": llm_text
          }
        ]
      }
    ]
  )

  response_content = completion.choices[0].message.content
  
  output_dir = os.path.join("working_dir", "export")
  os.makedirs(output_dir, exist_ok=True)
  
  timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
  
  if objective_selection == 0:
        objective_prefix = "Beat_Sheet_"
  elif objective_selection == 1:
      objective_prefix = "MS_Dev_Edit_"
  elif objective_selection == 2:
      objective_prefix = "Chapter_Dev_Edit_"
  else:
      objective_prefix = f"Objective_{objective_selection}_"

  base_name = os.path.basename(manuscript_path) 
  file_name_only, _ = os.path.splitext(base_name) 
  
  filename = f"{objective_prefix}{file_name_only}_{timestamp}.md"
  filepath = os.path.join(output_dir, filename)

  try:
    with open(filepath, "w", encoding="utf-8") as f:
      f.write(response_content)
    print(f"Successfully saved response to: {filepath}")
    return filepath
  except IOError as e:
    print(f"Error writing to file {filepath}: {e}")
    return None

