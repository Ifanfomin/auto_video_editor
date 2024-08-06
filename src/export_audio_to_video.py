from moviepy.editor import VideoFileClip, AudioFileClip
from math import ceil


class ExportAudioToVideo:
    def __init__(
            self,
            audio_path: str,
            video_path: str,
            end_at: int
    ):
        self.audio_clip = AudioFileClip(audio_path)
        self.video_clip = VideoFileClip(video_path)
        self.end_at = end_at

    def run(self):
        if self.video_clip.duration > self.audio_clip.duration:
            self.video_clip = self.video_clip.subclip(0, self.audio_clip.duration)
        else:
            self.audio_clip = self.audio_clip.subclip(0, self.video_clip.duration)
        self.video_clip = self.video_clip.set_audio(self.audio_clip)

        if self.end_at != -1 and 0 <= self.end_at <= self.video_clip.duration:
            self.video_clip = self.video_clip.subclip(
                0,
                self.end_at
            )

        return self.video_clip