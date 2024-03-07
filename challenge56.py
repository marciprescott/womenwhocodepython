"A function to extract all URLs from a given text using regular expressions" ""
import re


def get_urls(text):
    urls = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", text)
    return urls


text = """Now a days you can learn almost anything by 
just visiting http://www.google.com. But if you are 
completely new to cooking or baking then first you need to learn those 
fundamentals like boiling water. Next you can visit a good cooking site like 
- https://www.goodeats.com to 
learn further on a variety of cooking techniques."""

print(get_urls(text))  # Prints ['http://www.google.com.', 'https://www.goodeats.com']
