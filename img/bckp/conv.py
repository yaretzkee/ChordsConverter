import sys, subprocess, pathlib

root = pathlib.Path('.')
for o in root.iterdir():
    if o.is_file:
        if o.suffix == '.svg':
            subprocess.run(['convert', '-resize', '64x64', 'o.name', f'{o.stem}.png']) 
            #print(o.name, o.stem, o.suffix)
