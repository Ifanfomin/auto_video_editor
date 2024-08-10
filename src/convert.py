from moviepy.editor import VideoFileClip, AudioFileClip
import os

from src.files_saver import Saver


class Converter:
    def __init__(
            self,
            clip: VideoFileClip or AudioFileClip,
            ext: str = "",
    ):
        self.clip = clip
        self.ext = ext

    def video_to_ext(self) -> VideoFileClip:
        file_name = self.clip.filename
        file_dir_path = "/".join(file_name.split("/")[:-1])
        file_name = file_name.split("/")[-1]
        file_name = Saver(file_dir_path, file_name, self.clip, self.ext).video().save_name

        self.clip = VideoFileClip(os.path.join(file_dir_path, file_name))

        return self.clip

    def audio_to_ext(self) -> AudioFileClip:
        file_name = self.clip.filename
        file_dir_path = "/".join(file_name.split("/")[:-1])
        file_name = file_name.split("/")[-1]
        file_name = Saver(file_dir_path, file_name, self.clip, self.ext).audio().save_name

        self.clip = AudioFileClip(os.path.join(file_dir_path, file_name))

        return self.clip
