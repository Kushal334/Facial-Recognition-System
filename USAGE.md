# Setup

Cloning the repo and installing the dependencies
```
 git clone https://github.com/gargimahale/Facial-Recognition-System.git
 pip install -r requirements.txt
```
   
# Face Recognition
Depending on the use case, whether to aim for accuracy and stability or speed etc., you can pick the face detector. Also, there are customization options inside face detectors to decide the facial ROI.


To register a face using a webcam
```python
# Inside project root
import video_main

# You can pick a face detector depending on Acc/speed requirements
face_recognizer = FaceRecognitionVideo(face_detector='dlib')
face_recognizer.register_face_webcam(name="Susanta")
```

To register a face using an image on disk
```python
# Inside project root
import video_main

face_recognizer = FaceRecognitionVideo(face_detector='dlib')
face_recognizer.register_face_path(img_path='data/sample/conan.jpg', name="Conan")
```

To register a face using a loaded image 
```python
# Inside project root
from face_recog.media_utils import load_image_path
from face_recog.face_recognition import FaceRecognition

face_recognizer = FaceRecognition(
                    model_loc="models",
                    persistent_data_loc="data/facial_data.json",
                    face_detector="dlib",
                )
img = load_image_path("data/sample/1.jpg")
# Matches is a list containing information about the matches
# for each of the faces in the image
matches = face_recognizer.register_face(image=img, name=name)
```

Face recognition with a webcam feed
```python
# Inside project root
import video_main

face_recognizer = FaceRecognitionVideo(face_detector='dlib')
face_recognizer.recognize_face_video(video_path=None, \
                                    detection_interval=2, save_output=True, \
                                    preview=True, resize_scale=0.25)
```

Face recognition on a video
```python
# Inside project root
import video_main

face_recognizer = FaceRecognitionVideo(face_detector='dlib')
face_recognizer.recognize_face_video(video_path='data/trimmed.mp4', \
                                    detection_interval=2, save_output=True, \
                                    preview=True, resize_scale=0.25)
```

Face recognition using an image
```python
# Inside project root
from face_recog.media_utils import load_image_path
from face_recog.face_recognition import FaceRecognition

face_recognizer = FaceRecognition(
                    model_loc="models",
                    persistent_data_loc="data/facial_data.json",
                    face_detector="dlib",
                )
img = load_image_path("data/sample/1.jpg")
# Matches is a list containing information about the matches
# for each of the faces in the image
matches = face_recognizer.recognize_faces(
                image=img, threshold=0.6
            )
```


There are 4 face detectors namely dlib (HOG, MMOD), MTCNN, OpenCV (CNN). 
All the face detectors are based on a common abstract class and have a common detection interface **detect_faces(image)**.

```python
# import the face detector you want, it follows absolute imports
from face_recog.media_utils import load_image_path
from face_recog.face_detection_dlib import FaceDetectorDlib

face_detector = FaceDetectorDlib(model_type="hog")
# Load the image in RGB format
image = load_image_path("data/sample/1.jpg")
# Returns a list of bounding box coordinates
bboxes = face_detector.detect_faces(image)
```
