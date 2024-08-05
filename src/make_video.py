from moviepy.editor import *
import os
from datetime import datetime


class MakeVideo:
    def __init__(
            self,
            video_path,
            audio_path,
            save_path="created_videos",
            save_name=datetime.today().strftime("%Y-%m-%d-%H_%M_%S") + ".mp4"
    ):
        self.save_name = save_name
        self.save_path = save_path
        self.video_clip = VideoFileClip(video_path)
        self.audio_clip = AudioFileClip(audio_path)

        self.export_audio_to_video()
        self.save_video()

    def export_audio_to_video(self):
        self.video_clip = self.video_clip.set_audio(self.audio_clip)

    def save_video(self):
        self.video_clip.write_videofile(os.path.join(self.save_path, self.save_name))
