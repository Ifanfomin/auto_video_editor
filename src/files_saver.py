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

    return save_path, save_name


class SaveVideo:
    def __init__(
            self,
            save_path: str = "",
            save_name: str = "",
            video_clip: VideoFileClip = VideoFileClip,
            save_ext: str = ".mp4"
    ):
        self.video_clip = video_clip
        self.save_path = save_path
        self.save_name = save_name
        self.save_ext = save_ext
        self.run()

    def run(self):
        self.save_path, self.save_name = make_path_and_name(
            self.save_path,
            self.save_name,
            self.save_ext
        )

        self.video_clip.write_videofile(
            os.path.join(self.save_path, self.save_name)
        )


class SaveAudio:
    def __init__(
            self,
            save_path: str = "",
            save_name: str = "",
            audio_clip: AudioFileClip = AudioFileClip,
            save_ext: str = ".mp3"
    ):
        self.audio_clip = audio_clip
        self.save_path = save_path
        self.save_name = save_name
        self.save_ext = save_ext
        self.run()

    def run(self):
        self.save_path, self.save_name = make_path_and_name(
            self.save_path,
            self.save_name,
            self.save_ext
        )

        self.audio_clip.write_audiofile(
            os.path.join(self.save_path, self.save_name)
        )
