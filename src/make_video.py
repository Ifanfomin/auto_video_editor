from src.corp_silence_moments import CorpSilenceMoments
from src.export_audio_to_video import ExportAudioToVideo
from src.save_video import SaveVideo


class MakeVideo:
    def __init__(
            self,
            video_path: str,
            audio_path: str,
            start_from: int = 0,
            end_at: int = -1,
            save_path: str = "created_videos",
            save_name: str = "",
            corp_silence: bool = True
    ):
        self.save_name = save_name
        self.save_path = save_path
        self.video_path = video_path
        self.audio_path = audio_path
        self.start_from = start_from
        self.end_at = end_at
        self.corp_silence = corp_silence

    def run(self):
        video_clip = ExportAudioToVideo(self.audio_path, self.video_path, self.end_at).run()
        if self.corp_silence:
            video_clip = CorpSilenceMoments(self.start_from, video_clip).run()
        SaveVideo(self.save_path, self.save_name, video_clip).run()
