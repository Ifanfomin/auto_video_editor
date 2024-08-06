from moviepy.editor import VideoFileClip

import os
from datetime import datetime


class SaveVideo:
    def __init__(
            self,
            save_path: str,
            save_name: str,
            video_clip: VideoFileClip
    ):
        self.video_clip = video_clip
        self.save_path = save_path
        self.save_name = save_name

    def run(self):
        if self.save_name == "":
            self.save_name = datetime.today().strftime("%Y-%m-%d-%H_%M_%S") + ".mp4"
        self.video_clip.write_videofile(
            os.path.join(self.save_path, self.save_name)
        )
