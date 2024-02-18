from bs4 import BeautifulSoup
import requests
 
def scrape(links):
    text =""
    r = requests.get(links[0])
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    irrelevant_elements = ['script', 'style', 'header', 'footer', 'nav', 'aside']
    for element in soup.find_all(irrelevant_elements):
        element.decompose()
 
    # Extract text from remaining elements
    cleaned_text = ''
    for element in soup.find_all(['p', 'h1', 'h2', 'h3']):
        # Preserve headings and proper line breaks
        if element.name in ['h1', 'h2', 'h3']:
            cleaned_text += '\n' + element.text + '\n'
        else:
            cleaned_text += element.text + ' '
 
    # Lowercase, remove punctuation, convert to Unicode
    cleaned_text = cleaned_text.lower()
    # cleaned_text = remove_stopwords(cleaned_text)
    cleaned_text = cleaned_text.encode('ascii', 'ignore').decode('unicode-escape')

    return cleaned_text