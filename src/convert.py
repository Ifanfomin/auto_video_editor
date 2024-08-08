from moviepy.editor import VideoFileClip


class Converter:
    def video_to_mp4(self, video_path) -> str:
        clip = VideoFileClip(video_path)
        clip.write_videofile(video_path[:video_path.find(".")] + ".mp4")
        return video_path[:video_path.find(".")] + ".mp4"
