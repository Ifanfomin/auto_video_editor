from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, CompositeVideoClip

from src.cut_media import CutVideo, CutAudio


class ExportVideo:
    def __init__(
            self,
            video_path: str,
            start_at: int = 0,
            end_at: int = -1
    ):
        self.video_clip = VideoFileClip(video_path)
        self.start_at = start_at
        self.end_at = end_at

    def run(self):
        self.video_clip = CutVideo(
            self.video_clip,
            self.start_at,
            self.end_at
        ).run()

        return self.video_clip


class ExportAudio:
    def __init__(
            self,
            audio_path: str,
            start_at: int = 0,
            end_at: int = -1
    ):
        self.audio_clip = AudioFileClip(audio_path)
        self.start_at = start_at
        self.end_at = end_at

    def run(self):
        self.audio_clip = CutAudio(
            self.audio_clip,
            self.start_at,
            self.end_at
        ).run()

        return self.audio_clip
