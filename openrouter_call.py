from openai import OpenAI
from dotenv import load_dotenv
from prompts.prompt import get_llm_text

load_dotenv()
openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")

def call_openrouter(objective_selection):
  llm_text = get_llm_text(objective_selection)
  # gets API Key from environment variable OPENAI_API_KEY
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key,
  )

  completion = client.chat.completions.create(
    model="openai/gpt-4.1",
    # extra_headers={
    #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    #   "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    # },
    # pass extra_body to access OpenRouter-only arguments.
    # extra_body={
      # "models": [
      #   "${Model.GPT_4_Omni}",
      #   "${Model.Mixtral_8x_22B_Instruct}"
      # ]
    # },
    messages=[
      {
        "role": "user",
        "content": [
          "type": "text",
          "text": llm_text
        ]
      },
    ],
  )
  print(completion.choices[0].message.content)
