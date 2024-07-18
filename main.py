import os
import shutil
from datetime import datetime, timedelta
import time


def main() -> None:
    """Copies and pastes all files in a directory also clears
     all files in the manual directory, ready to upload."""
    src_dir = os.path.dirname(os.path.abspath(__file__))
    dest_dir = src_dir + '/manual'
    try:
        shutil.rmtree(dest_dir)
    except Exception as e:
        print(f'failed to clear old manual folder: {e}')

    os.makedirs(dest_dir, exist_ok=True)
    today = datetime.today().strftime('%d-%m-%Y')
    files = os.listdir(src_dir)

    for file in files:
        modified = datetime.fromtimestamp(os.path.getmtime(file))
        current_time = datetime.now()
        delta = current_time - modified
        update = delta <= timedelta(hours=24)
        if file.endswith(".xlsx") and True == update:
            file_src_dir = os.path.join(src_dir, file)
            new_file_name = 'manual_' + today + "_" + file
            file_dest_dir = os.path.join(dest_dir, new_file_name)
            shutil.copy(file_src_dir, file_dest_dir)
            time.sleep(0.1)


if __name__ == '__main__':
    main()
