from bs4 import BeautifulSoup
import os
from fpdf import FPDF

print('''
\n
Workflow (Mac):
  For each Udemy video:
      Click the 'open transcript' button
      Right click > `Inspect` to open the inspector window (make window smaller to make sure all dynamic content is visible and therefore visible in the DOM)
      Select the 'html' tagged element, Command+C to copy
      In `sources` project folder, create a new file, paste html contents (should paste html and child nodes; i.e., all content on page including dynamic elements)
      
  To run:
      Run `python3 scrape.py`
      Output will be placed in `output` folder
        (Title string parsing based on Udemy course videos by Jason Dion)
      Right `output` folder in solution explorer, click `Reveal in Finder`
      Open target iCloud folder in separate Window
      Copy+Paste / Drag+Drop files to target folder
      Annotate on iPad
'''
)

# clean out old put folders before run
path = '<project path>/output'
old_out = os.listdir(path)
for o in old_out:
    os.remove(f'output/{o}')

# change if necessary
path = '<project path>/sources'
sources = os.listdir(path)

# "scraping" date
transcript = ''
title = ''
for s in sources:
  with open(f"sources/{s}", "r") as inf:
      soup = BeautifulSoup(inf, 'html.parser')
      lines = soup.find_all('p', class_='transcript--underline-cue---xybZ')
      transcript = ''
      for l in lines:
          transcript += (l.get_text() + ' ')
      
      title = soup.find('section', class_='lecture-view--container--mrZSm')['aria-label']
      transcript = title + '\n\n' + transcript

  # ex. `Section 10: Windows Command Line Tools, Lecture 95: System File Checker (OBJ. 1.2)`
  # shortened to `Lecture 95: System File Checker`
  # change if necessary
  title = title[(title.find(',')+1):(title.find('(')-1)]
  fn = 'output/' + title + '.txt'

  # output to pdf
  pdf = FPDF(format='letter', unit='in')
  pdf.add_page()
  pdf.set_font("helvetica", size = 12)
  pdf.set_margins(1, 1)
  effective_page_width = pdf.w - 2*pdf.l_margin
  pdf.multi_cell(
      w=effective_page_width, 
      h=0.22, 
      text=transcript,
      align='J'
      )
  fn = 'output/' + title + '.pdf'
  pdf.output(fn)

  # clean out sources folder for next run
  os.remove(f'source/{s}')


'''
Issues:
- Udemy must authenticate to see page, so cannot use requests (with BeautifulSoup or Selenium)
- Udemy 'Instructors' have an API, but not regular users which they call 'Affiliates' (or the page just wouldn't load on my computer)
- There is no script tag that seems to directly point to metadata or resource fetch requests that are obvious
- The page is dynamically loaded and looking at the Inspect window, the HTML will only show explicitly visible content
  - e.g. Video titles (inner text) not visible in inspect window if the page section is not large enough to toggle visibility
- No FETCH/XHR requests are discernably for transcript data
'''
