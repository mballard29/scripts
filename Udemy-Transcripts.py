from bs4 import BeautifulSoup
import subprocess

print('''
\n
To use scrape.py:
      (Mac)
      On Udemy video page, type Command+S to save the webpage
      Name the file `scrape-this`
      Select this project folder as the file save destination
      In the file type drop down, select `Webpage, HTML only`
      Click `Save`
      Run `python3 scrape.py`
      Output will be a text file named after video title
      Title string parsing based on Udemy course videos by Jason Dion
      ex: 
        Section 10: Windows Command Line Tools, Lecture 95: System File Checker (OBJ. 1.2)
        to
        Lecture 95: System File Checker.txt

iCloud (iPad) annotation:
      Run this process on each webpage in section.
      Batch drag/drop text files into iCloud drive.
      Wait for iCloud to sync (or force if necessary).
'''
)

transcript = ''
title = ''
with open("scrape-this.html", "r") as inf:
    soup = BeautifulSoup(inf, 'html.parser')
    lines = soup.find_all('p', class_='transcript--underline-cue---xybZ')
    transcript = ''
    for l in lines:
        transcript += (l.get_text() + ' ')
    
    title = soup.find('section', class_='lecture-view--container--mrZSm')['aria-label']
    transcript = title + '\n\n' + transcript

title = title[(title.find(',')+1):(title.find('(')-1)]
fn = title + '.txt'

with open(fn, "w") as of:
    of.write(transcript)


'''
Issues:
- Udemy must authenticate to see page, so cannot use requests (with BS or Selenium)
- Udemy 'Instructors' have an API, but not regular users which they call 'Affiliates' (or the page just wouldn't load on my computer)
- There is no script tag that seems to directly point to metadata or resource fetch requests that are obvious
- The page is dynamically loaded and even looking at the Inspect window, the HTML will only show explicitly visible content
- No FETCH/XHR requests are discernably for transcript data
'''
