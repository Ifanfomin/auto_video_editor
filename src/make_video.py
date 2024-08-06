from moviepy.editor import *
import os
from datetime import datetime
from math import ceil


class MakeVideo:
    def __init__(
            self,
            video_path: str,
            audio_path: str,
            start_from: int = 0,
            end_at: int = -1,
            save_path: str = "created_videos",
            save_name: str = datetime.today().strftime("%Y-%m-%d-%H_%M_%S") + ".mp4"
    ):
        self.save_name = save_name
        self.save_path = save_path
        self.video_clip = VideoFileClip(video_path)
        self.audio_clip = AudioFileClip(audio_path)
        self.start_from = start_from
        self.end_at = end_at

        self.export_audio_to_video()
        self.corp_silence_moments()
        self.save_video()

    def export_audio_to_video(self):
        if self.video_clip.duration > self.audio_clip.duration:
            self.video_clip = self.video_clip.subclip(0, self.audio_clip.duration)
        else:
            self.audio_clip = self.audio_clip.subclip(0, self.video_clip.duration)
        self.video_clip = self.video_clip.set_audio(self.audio_clip)

        if self.end_at == -1:
            self.end_at = ceil(self.video_clip.duration)

    def corp_silence_moments(self):
        new_video_clip = 0
        count = 0
        for interval_start in range(self.start_from, self.end_at):
            count += 1
            print("Count: ", count)

            audio_array = self.video_clip.audio.subclip(
                interval_start,
                interval_start + 1
            ).to_soundarray(fps=10)

            max_volume = 0
            for frame in audio_array:
                max_volume = max(max_volume, abs(frame[0]))

            if max_volume > 0.02:
                if new_video_clip == 0:
                    new_video_clip = self.video_clip.subclip(
                            interval_start,
                            interval_start + 1
                        )
                else:
                    new_video_clip = concatenate_videoclips(
                        [
                            new_video_clip,
                            self.video_clip.subclip(
                                interval_start,
                                interval_start + 1
                            )
                        ]
                    )
        self.video_clip = new_video_clip

    def save_video(self):
        self.video_clip.write_videofile(
            os.path.join(self.save_path, self.save_name)
        )
