import os
from dotenv import load_dotenv

import time
import openai

# Import prompt files
import copyPrompts
import logicPrompts
import mattersPrompts
import calebPrompts


# Load API key
load_dotenv()
openai.api_key = os.getenv('api_key')

# CHOOSE PROMPT
# promptText = mattersPrompts.getText()
promptText = calebPrompts.getText()

# CHOOSE MAX_TOKENS
maxTokens = 500

print('------------ NEW RUN -------------')

# Generate Result
result = openai.Completion.create(
    engine="davinci",
    prompt=promptText,
    max_tokens=maxTokens
)

# Parse generated text
generatedText = result.choices[0].text
print(generatedText)

# Save result
timestr = time.strftime("%m%d-%H:%M-%S")
f = open('history/' + timestr + ".txt", "a")
f.write('Prompt:' + promptText + '\n\nGenerated:\n' + generatedText)
f.close()
