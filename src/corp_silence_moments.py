from moviepy.editor import VideoFileClip, concatenate_videoclips
from math import ceil


class CorpSilenceMoments:
    def __init__(
            self,
            start_from: int,
            video_clip: VideoFileClip
    ):
        self.segments = []
        self.start_from = start_from
        self.end_at = ceil(video_clip.duration)
        self.video_clip = video_clip

    @staticmethod
    def check_available_cut(start, end, video_clip, segments_dict):
        print("Work with:", start, "second")
        audio_array = video_clip.audio.subclip(
            start,
            end
        ).to_soundarray(fps=10)

        max_volume = 0
        for frame in audio_array:
            max_volume = max(max_volume, abs(frame[0]))

        if max_volume > 0.02:
            clip_segment = video_clip.subclip(
                start,
                end
            )
            segments_dict[start] = clip_segment

    def run(self) -> VideoFileClip:
        segments_dict = {}
        for n in range(self.start_from, self.end_at):
            self.check_available_cut(n, n + 1, self.video_clip, segments_dict)
        self.video_clip = concatenate_videoclips(list(segments_dict.values()))

        return self.video_clip

