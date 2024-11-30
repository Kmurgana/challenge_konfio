import re
import unicodedata
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env file
load_dotenv()

# Model we are going to use
llm_model = "gpt-3.5-turbo"

# Get the API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Instance the OpenAi client.
client = OpenAI()

# Text cleaning function
def clean_text(text):
    text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', text)
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = ' '.join(text.split())
    return text

# This function is to call the open ai model with the corresponding roles.
def call_openai(system_prompt,prompt, model="gpt-3.5-turbo"):
	chat_completion = client.chat.completions.create(
		messages=[
			{
				"role": "system",
				"content": system_prompt
			},
			{
				"role": "user",
				"content": prompt,
			}
		],
		model=model,
	)
	return chat_completion.choices[0].message.content


def process_result(model, prompt_cleaned):
    
    target_columns = ['crec', 'cred', 'equ', 'inic', 'inv', 'mkt', 'no', 'renta', 'sueldo', 'temp']
    
    # Define the system prompt for the task
    system_prompt = "This model processes financial loans requests and classifies them into categories."


    # Call OpenAI API to get the classification
    result =call_openai(system_prompt, prompt_cleaned, model)

    try: 
        # Post-process the result
        result_list = [int(label) for label in result.split(',')]
        result_predicted = [target_columns[i] for i in range(len(target_columns)) if result_list[i] == 1]
        print("----------")
        print(f'User prompt: {prompt_cleaned}\nPredicted category:{result_predicted}')

        return result_predicted
    except Exception as e:
            print(f"Error in the model return value: {result} skipping this prompt: {prompt_cleaned}")
