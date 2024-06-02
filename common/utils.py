from pathlib import Path
from common.profile import Profile
from datetime import datetime

def get_file_name_parts(filename: str):
    pos = filename.rfind('.')
    if pos == -1:
        return filename, ''

    return filename[:pos], filename[pos+1:]


def get_save_filepath(file_path: Path, filename: str):
    save_file = file_path.joinpath(filename)
    name, ext = get_file_name_parts(filename)
    timestamp = str(int(datetime.now().timestamp()))
    save_file = file_path.joinpath(f'{name}_{timestamp}.{ext}')
    return save_file



class ImageService:
    def get_image_filename_list(self):
        image_path = Profile.get_images_path()

        filename_list = []

        if image_path.exists():
            for item in image_path.iterdir():
                if item.is_file():
                    filename_list.append(item.name)

        return filename_list