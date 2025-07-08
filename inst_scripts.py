import pathlib

with open('inst_drivers.cmd', 'w') as f:
    for file in pathlib.Path(r"D:\\").rglob('*'):
        if file.is_file() and file.name.endswith('.inf'):
            inf_path = str(file.resolve())[3:]
            f.write(f'drvload "{inf_path}"\n')
