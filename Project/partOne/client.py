import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinterhtml import HtmlFrame  # Tkinter HTML rendering library
from datetime import datetime, timedelta
import os

# Function to make HTTP GET request with caching
def get_page_with_caching(url):
    cache_file = "cache.html"
    cache_validity = timedelta(minutes=5)  # Cache validity duration

    # Check if cache file exists and if it's still valid
    if os.path.exists(cache_file):
        modification_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if datetime.now() - modification_time < cache_validity:
            with open(cache_file, "r") as file:
                return file.read()

    # Send GET request to the server
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save response content to cache file
        with open(cache_file, "w") as file:
            file.write(response.text)
        return response.text
    else:
        print(f"Error: {response.status_code} - {response.reason}")

# URL entered by the user
url = input("Enter HTTP URL: ")
# Call the function to get the page content with caching
page_content = get_page_with_caching(url)
if page_content:
    # Parse HTML content
    soup = BeautifulSoup(page_content, 'html.parser')
    # Extract body content
    body_content = soup.body if soup.body else soup
    # Create Tkinter window
    root = tk.Tk()
    root.title("HTML Page")
    # Create Tkinter HTMLFrame
    html_frame = HtmlFrame(root)
    html_frame.grid(row=0, column=0, padx=5, pady=5)
    # Render HTML content in HTMLFrame
    html_frame.set_content(str(body_content))
    root.mainloop()

