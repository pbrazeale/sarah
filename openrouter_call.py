from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=openrouter_api_key,
)

completion = client.chat.completions.create(
  model="${Model.GPT_4_Omni}",
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
      "content": "Say this is a test",
    },
  ],
)
print(completion.choices[0].message.content)
