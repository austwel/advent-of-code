import shutil, os

day = max(int(file.name) for file in os.scandir('.') if file.name != os.path.basename(__file__))+1
shutil.copytree(f'00', f'{day:02d}')
shutil.move(os.path.join(f'{day:02d}', '00.py'), os.path.join(f'{day:02d}', f'{day:02d}.py'))