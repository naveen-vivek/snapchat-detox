"""Module to help users correct timestamps on Snapchat memories."""

import os
import shutil
import re
from datetime import datetime
import piexif
from PIL import Image


def adjust_image_timestamp(image_path: str, timestamp: str) -> None:
    """Adjusts image timestamp

    Args:
        image_path (str): absolute path to image
        timestamp (str): new timestamp as a string
    """
    print(f'adjust_image_timestamp for {image_path}')
    try:
        exif_dict = piexif.load(image_path)
        exif_dict['0th'][piexif.ImageIFD.DateTime] = timestamp
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = timestamp
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = timestamp
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, image_path)
    except Exception as e:
        with open('fail.txt', 'w', encoding='UTF-8') as f:
            f.write(f'{image_path}\n')
        print(f'{image_path} did not work. Error: {e}')


if __name__ == "__main__":

    ORIGINAL_SNAPCHAT_MEMORY_FOLDER = '/Users/naveenvivek/Downloads/snapchat'
    COPY_SNAPCHAT_MEMORY_FOLDER = '/Users/naveenvivek/Downloads/snapchat_copy'
    shutil.copytree(ORIGINAL_SNAPCHAT_MEMORY_FOLDER, COPY_SNAPCHAT_MEMORY_FOLDER)

    for dirpath,_,filename_list in os.walk(ORIGINAL_SNAPCHAT_MEMORY_FOLDER):

        for filename in filename_list:

            file_abs_path = os.path.join(dirpath, filename)
            filename_without_extension = filename.split('.')[0]

            # Ignores overlay files and non-images
            if ('overlay' in filename_without_extension) or not(filename.endswith('.png') or filename.endswith('.jpg')):
                print(f'Removing {file_abs_path}')
                os.remove(file_abs_path)
                continue

            # Changes PNG files to JPGs for easy timestamp modification
            if filename.endswith('.png'):
                Image.open(file_abs_path).convert('RGB').save(os.path.join(dirpath, f'{filename_without_extension}.jpg'))
                os.remove(file_abs_path)
                filename = f'{filename_without_extension}.jpg'

            new_file_abs_path = os.path.join(dirpath, filename)
            result = re.search("([0-9]{4}\-[0-9]{2}\-[0-9]{2})", filename)[0]
            new_timestamp = datetime.strptime(result, '%Y-%m-%d').strftime("%Y:%m:%d %H:%M:%S")
            adjust_image_timestamp(new_file_abs_path, new_timestamp)
