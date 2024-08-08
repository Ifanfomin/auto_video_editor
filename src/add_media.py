from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, CompositeVideoClip
from moviepy.audio.fx.volumex import volumex

from src.cut_media import CutAudio


class AddAudio:
    def __init__(
            self,
            audio_clip: AudioFileClip,
            video_clip: VideoFileClip,
            volume: float,
            start_at: int,
            end_at: int
    ):
        self.audio_clip = audio_clip
        self.video_clip = video_clip
        self.volume = volume
        self.start_at = start_at
        self.end_at = end_at

    def run(self):
        self.audio_clip = CutAudio(self.audio_clip, 0, self.video_clip.duration).run()

        self.audio_clip = volumex(self.audio_clip, self.volume)
        audio_clips = [self.audio_clip]

        if self.video_clip.audio is not None:
            audio_clips.append(self.video_clip.audio)

        self.audio_clip = CompositeAudioClip(audio_clips)
        self.video_clip = self.video_clip.set_audio(self.audio_clip)

        return self.video_clip


class AddVideo:
    ...
