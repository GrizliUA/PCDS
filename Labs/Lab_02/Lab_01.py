import cv2
import pyaudio
import wave
 
capture = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640,480))
 
# # Define recording parameters
# FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
# CHANNELS = 2              # Mono audio
# RATE = 44100              # Sample rate (samples per second)
# CHUNK = 1024              # Number of frames per buffer
# OUTPUT_FILENAME = "audio.wav"  # Output file name

# audio = pyaudio.PyAudio()

# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                     rate=RATE, input=True,
#                     frames_per_buffer=CHUNK)


print("Recording...")
#frames = []
while (True):
 
    ret, frame = capture.read()
     
    if ret:
        cv2.imshow('video', frame)
        videoWriter.write(frame)
        #data = stream.read(CHUNK)
        #frames.append(data)
 
    if cv2.waitKey(1) == 27:
        break
 
print("Finished recording.")
capture.release()
videoWriter.release()
# stream.stop_stream()
# stream.close()
# audio.terminate()
 
# cv2.destroyAllWindows()
# with wave.open(OUTPUT_FILENAME, 'wb') as wf:
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(audio.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))



# from moviepy.editor import VideoFileClip, AudioFileClip

# video_clip = VideoFileClip("video.avi")
# audio_clip = AudioFileClip("audio.wav")

# final_clip = video_clip.set_audio(audio_clip)

# final_clip.write_videofile("result.mp4")

# print(f"Recordings saved")