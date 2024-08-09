# Auto Video Editor

## How main.py works
```python
video = MakeVideo()  # create MakeVideo object
video.export_video("media/Видео.mp4")  # export video to object

audio = MakeVideo()  # create new MakeVideo object
audio.export_audio("media/audio.ogg")  # export audio to new object
video.add_audio(audio)  # add audio to video
video.corp_silence_moments()  # corp silence from video

audio = MakeVideo()  # create new MakeVideo object
audio.export_audio("media/background_audio.mp3")  # export audio

video.add_audio(audio, volume=0.2)  # add audio to video at volume * 0.2

video.save_video("created_videos")  # save video
```
