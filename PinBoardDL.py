import subprocess
import time

if __name__ == '__main__':
    url = input("Enter url of a public Pinterest board: ")
    username = input("Computer username: ")

    subprocess.Popen(f'gallery-dl "{url}" > loc.txt', shell=True)

    time.sleep(5)

    with open('loc.txt') as f:
        loc = f.readlines()[-1]
        end = loc.find('pinterest_')
        loc = loc[2:end]
        print('Location: ', loc)

    print("Opening finder folder and photos...")
    print(f"Opening {loc}")
    subprocess.Popen(f'open "{loc}"', shell=True)
    print("Opening pictures!")
    subprocess.Popen(f'open /Users/{username}/Pictures/Photos\ Library.photoslibrary', shell=True)
    subprocess.Popen(f'rm loc.txt', shell=True)
    # subprocess.Popen(f'rm gallery-dl', shell=True)

    print("DONE!")
