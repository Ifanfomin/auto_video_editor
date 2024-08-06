from src.make_video import MakeVideo


def main():
    make_video = MakeVideo(
        "media/Запись экрана от 2024-08-05 21-38-38.webm",
        "media/audio_2024-08-05_21-42-10.ogg",
        0,
    ).run()


if __name__ == '__main__':
    main()
