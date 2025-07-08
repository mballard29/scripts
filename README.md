# Scripts
### short scripts I use sometimes

### PinBoardDL.py
I use Pinterest to create moodboards, or just collect stuff I find on Pinterest sometimes. Sometimes, I want to print these out, create stickers, or have printouts to reference charts I've saved. This script was created to automate a process I do on my Mac. It prompts the user for link to the Pinterest board, and it downloads all of the photos on that board (must be public) to a folder called `gallery-dl` (in the same location as my script). Because I like to make my life hard :upside_down_face:, I use iCloud to let me edit together pictures I find using Procreate on my iPad. Once the script is done downloading the pictures, it will open the folder it created and Apple's Photos app where I can drag and drop what I have downloaded and access them via iCloud on my iPad.


### GithubUL.sh
The commands I don't like to type out when creating a Github repo from an existing folder on my local machine. Skips me a couple steps forward to actually naming and setting permissions for the repo on Github using the CLI.

### Udemy Transcripts
Made to allow me get Udemy transcrips in an annotatable format. Parses HTML to create output pdf files to be printed or copied/moved to iCloud folder for annotation using iPad. (Example files in folders to understand input/output functioning of script. I'm trying to respect IP, so they are redacted to only show what is necessary)
(*note: Udemy is not very developer friendly. Makes sense because the content hosted is paid/proprietary. The purpose of the script is to increase accessibility friendliness and studying flexibility. Specific issues mentioned in comments in script.)

### find_drivers.py
When getting drivers from the Dell website, they come as executables that must be extracted. You can use `drvload <Path to .inf file>` to install a driver from the Windows command prompt if you know the Path to the driver, but they are often in deeply nested folders that may be ambiguously named. Given a drive with the extracted driver files, I can put `find_drivers.py` on the same drive, run it, and then run the outputted `install_drivers.cmd` on the target system to quickly install drivers on my flash drive (particularly for recovering a Windows system).




<h4>Future projects</h4>

- [ ] <next>
