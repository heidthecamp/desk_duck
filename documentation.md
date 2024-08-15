# Documenting resource and methods used

## Audio

Using `speech_recognition` for STT and `pyttsx3` as TTS allows for easy speach input
and converts text to audio outputs.[1]

### Definitions

- STT: Speech to Text
- TTS: Text to Speech

## Video

`Opencv-python` acts as an interface that can use your system's video devices.[2]


## Eye tracking

After much effort I found a project that handles eye tracking fairly reliably. I
believe this can be used in our project. It seems to mee the requirements and is
hosted on an public github page but it does not have a listed license.[3]

### failed resources

- pygaze: running the base example with pygaze threw errors with types within the
module itself. After resolving several issues in the module there was a function
call in the init that was not providing the appropriate number of arguments. At this
point I decide it was not worth pursuing further.

## Resources

1. [geeksforgeeks (STT and TTS)](https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/)
2. [geeksforgeeks (video from camera)](https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/)
3. [Gaze Estimation (github)](https://github.com/amitt1236/Gaze_estimation)
4. [Gaze Estimation (medium)](https://medium.com/@amit.aflalo2/eye-gaze-estimation-using-a-webcam-in-100-lines-of-code-570d4683fe23)
