from src.make_video import MakeVideo


def main():
    video = MakeVideo()
    video.export_video("media/Видео.mp4")

    audio = MakeVideo()
    audio.export_audio("media/audio.ogg")
    video.add_audio(audio)
    video.corp_silence_moments()

    audio = MakeVideo()
    audio.export_audio("media/background_audio.mp3")

    video.add_audio(audio, volume=0.2)

    video.save_video("created_videos")


if __name__ == '__main__':
    main()
