from moviepy.editor import VideoFileClip, AudioFileClip

import os
from datetime import datetime


def make_path_and_name(
        save_path: str = "",
        save_name: str = "",
        save_ext: str = ""
):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if save_name == "":
        save_name = datetime.today().strftime("%Y-%m-%d-%H_%M_%S") + save_ext
    else:
        save_name = ".".join(save_name.split(".")[:-1]) + save_ext

    return save_path, save_name


class Saver:
    def __init__(
            self,
            save_path: str,
            save_name: str,
            clip: VideoFileClip or AudioFileClip,
            save_ext: str
    ):
        self.clip = clip
        self.save_path, self.save_name = make_path_and_name(
            save_path,
            save_name,
            save_ext
        )

    def video(self):
        self.clip.write_videofile(
            os.path.join(self.save_path, self.save_name)
        )

    def audio(self):
        self.clip.write_audiofile(
            os.path.join(self.save_path, self.save_name)
        )
