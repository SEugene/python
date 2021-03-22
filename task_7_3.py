import os
import shutil

for root, dirs, files in os.walk('my_project'):
    for file in files:
        if 'templates' in os.path.join(root, file):
            try:
                os.makedirs(os.path.join('my_project', 'templates', os.path.basename(root)))
            except FileExistsError as e:
                print(f'concrete error: {e}')
            src = os.path.join(root, file)
            dst = os.path.join('my_project', 'templates', os.path.basename(root), file)
            shutil.copy2(src, dst)
