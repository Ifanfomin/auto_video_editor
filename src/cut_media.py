from moviepy.editor import VideoFileClip, AudioFileClip


class CutVideo:
    def __init__(
            self,
            video_clip: VideoFileClip = -1,
            start_at: int = 0,
            end_at: int = -1,
    ):
        self.video_clip = video_clip
        self.start_at = start_at
        self.end_at = end_at

    def run(self):
        if self.start_at < 0:
            self.start_at = 0

        if self.end_at != -1 and 0 <= self.end_at <= self.video_clip.duration:
            self.video_clip = self.video_clip.subclip(
                self.start_at,
                self.end_at
            )

        return self.video_clip


class CutAudio:
    def __init__(
            self,
            audio_clip: AudioFileClip = -1,
            start_at: int = 0,
            end_at: int = -1,
    ):
        self.audio_clip = audio_clip
        self.start_at = start_at
        self.end_at = end_at

    def run(self):
        if self.start_at < 0:
            self.start_at = 0

        if self.end_at != -1 and 0 <= self.end_at <= self.audio_clip.duration:
            self.audio_clip = self.audio_clip.subclip(
                self.start_at,
                self.end_at
            )

        return self.audio_clip
