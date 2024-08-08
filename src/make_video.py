from moviepy.editor import VideoFileClip, AudioFileClip

from src.corp_silence_moments import CorpSilenceMoments
from src.files_exporter import ExportVideo, ExportAudio
from src.files_saver import SaveVideo, SaveAudio
from src.add_media import AddAudio, AddVideo


class MakeVideo:
    def __init__(
            self,
            # video_path: str,
            # audio_path: str,
            # start_from: int = 0,
            # end_at: int = -1,
            # save_path: str = "created_videos",
            # save_name: str = "",
            # corp_silence: bool = True
    ):
        # self.save_name = save_name
        # self.save_path = save_path
        # self.video_path = video_path
        # self.audio_path = audio_path
        # self.start_from = start_from
        # self.end_at = end_at
        # self.corp_silence = corp_silence
        self.video_clip = None
        self.audio_clip = None

    def export_video(
            self,
            video_path: str,
            start_at: int = 0,
            end_at: int = -1
    ):
        self.video_clip = ExportVideo(
            video_path,
            start_at,
            end_at
        ).run()

    def export_audio(
            self,
            audio_path: str,
            start_at: int = 0,
            end_at: int = -1
    ):
        self.audio_clip = ExportAudio(
            audio_path,
            start_at,
            end_at
        ).run()

    def add_audio(
            self,
            mv_audio,
            volume: float = 1,
            start_at: int = 0,
            end_at: int = -1
    ):
        self.video_clip = AddAudio(
            mv_audio.audio_clip,
            self.video_clip,
            volume,
            start_at,
            end_at
        ).run()

    def corp_silence_moments(
            self,
            start_at: int = 0,
    ):
        self.video_clip = CorpSilenceMoments(start_at, self.video_clip).run()

    def save_video(
            self,
            save_path: str = "",
            save_name: str = "",
            save_ext: str = ".mp4"
    ):
        SaveVideo(
            save_path,
            save_name,
            self.video_clip,
            save_ext
        )

    def save_audio(
            self,
            save_path: str = "",
            save_name: str = "",
            save_ext: str = ".mp3"
    ):
        SaveAudio(
            save_path,
            save_name,
            self.audio_clip,
            save_ext
        )
