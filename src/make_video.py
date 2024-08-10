from moviepy.editor import VideoFileClip, AudioFileClip

from src.corp_silence_moments import CorpSilenceMoments
from src.files_exporter import ExportVideo, ExportAudio
from src.files_saver import Saver
from src.add_media import AddAudio, AddVideo
from src.convert import Converter


class MakeVideo:
    def __init__(self):
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

    def convert_to_ext(
            self,
            ext: str
    ):
        if self.video_clip is not None:
            self.video_clip = Converter(self.video_clip, ext).video_to_ext()
        elif self.audio_clip is not None:
            self.audio_clip = Converter(self.audio_clip, ext).audio_to_ext()

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
        Saver(
            save_path,
            save_name,
            self.video_clip,
            save_ext
        ).video()

    def save_audio(
            self,
            save_path: str = "",
            save_name: str = "",
            save_ext: str = ".mp3"
    ):
        Saver(
            save_path,
            save_name,
            self.audio_clip,
            save_ext
        ).audio()
