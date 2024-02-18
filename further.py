import google.generativeai as palm
import prompts as pr

api_key = "AIzaSyBqHsPuJdQmzoKQhvTNIkdkCBMa9_aln10"

def extract(text):
    text = text.replace("*", "")
    lines = [line.strip() for line in text.splitlines()]  # Keep this line

    keywords = [lines[i] for i in range(len(lines)) if i > 1]
    return keywords

def furtherSearch(text:str):
    palm.configure(api_key=api_key)
    model = palm.get_model('models/chat-bison-001')

    response = palm.chat(messages=f"return keywords for the following text: {text}. return only the keywords and no other text. just the keywords in form of a python list.", temperature=1, context=pr.context1)
    keywords = extract(response.last)

    return {'keywords':keywords}