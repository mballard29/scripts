import pathlib

# INPUT: The drive (search from the root of this drive)
# OUTPUT: install_drivers.cmd script
# PREREQUISITES: a flash drive with extracted drive files, a target Windows system, a (separate) Windows PE or installer flash drive or disk.
# PURPOSE: automated install of device drivers in Windows system (like Win PE or installer environment)
# USAGE: 
    # put extracted drivers onto flash drive
    # run this script
    # in a Win PE / installer environment, access drive FS (e.g. by typing `D:` at commandline where D: is the flashdrive with the script)
    # run `install_drivers.cmd`

with open('install_drivers.cmd', 'w') as f:
    for file in pathlib.Path(r"D:\\").rglob('*'):
        if file.is_file() and file.name.endswith('.inf'):
            inf_path = str(file.resolve())[3:]
            f.write(f'drvload "{inf_path}"\n')
