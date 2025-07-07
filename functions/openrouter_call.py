from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime
from prompts.prompt import get_llm_text

load_dotenv()
openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")

def call_openrouter(objective_selection, manuscript_path, beat_sheet=None, ms_developmental_edit=None):
  llm_text = get_llm_text(objective_selection, manuscript_path, beat_sheet, ms_developmental_edit)

  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key,
  )

  completion = client.chat.completions.create(
    # extra_headers={
    #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    #   "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    # },
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
    objective_prefix = "Line_Edit_"
  else:
    objective_prefix = f"Objective_{objective_selection}_"

  base_name = os.path.basename(manuscript_path) # Gets 'MyNovel.md'
  file_name_only, _ = os.path.splitext(base_name) # Gets 'MyNovel'
  
  filename = f"{objective_prefix}{file_name_only}_{timestamp}.md"
  filepath = os.path.join(output_dir, filename)

  try:
    with open(filepath, "w", encoding="utf-8") as f:
      f.write(response_content)
    print(f"Successfully saved response to: {filepath}")
  except IOError as e:
    print(f"Error writing to file {filepath}: {e}")

