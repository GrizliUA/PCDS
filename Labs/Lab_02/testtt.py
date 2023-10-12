import cv2
import numpy as np
import wave
import audioop
import pyaudio
import time

# Set up the video capture
video_capture = cv2.VideoCapture(0)  # You can specify the video file path here instead of the camera (0 for default camera)
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Video codec for the output video
out = cv2.VideoWriter('output_video.avi', fourcc, fps, (width, height))


# Set up audio recording
audio_format = pyaudio.paInt16
audio_channels = 2
audio_rate = 44100  # You can adjust this as needed
audio_chunk = 1024
audio_output_filename = 'output_audio.wav'

audio_capture = pyaudio.PyAudio()

audio_stream = audio_capture.open(format=audio_format,
                                  channels=audio_channels,
                                  rate=audio_rate,
                                  input=True,
                                  frames_per_buffer=audio_chunk)

# Initialize the audio frames list
audio_frames = []

# Record audio and save frames
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Record audio
    audio_data = audio_stream.read(audio_chunk)
    audio_frames.append(audio_data)

    # Write video frame
    out.write(frame)

# Release video and audio resources
video_capture.release()
out.release()

# Save audio to a WAV file
audio_stream.stop_stream()
audio_stream.close()
audio_capture.terminate()

#time.sleep(10)

# with wave.open(audio_output_filename, 'wb') as wf:
#     wf.setnchannels(audio_channels)
#     wf.setsampwidth(audio_capture.get_sample_size(audio_format))
#     wf.setframerate(audio_rate)
#     wf.writeframes(b''.join(audio_frames))

