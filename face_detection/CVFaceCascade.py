import cv2
import numpy as np
from face_detection.FaceDetectionInterface import FaceDetectionInterface


class CVFaceCascade(FaceDetectionInterface):
    def __init__(self, classifier_path):
        super().__init__(classifier_path)
        self._classifier = cv2.CascadeClassifier(classifier_path)
        self._faces = None

    def __get_faces_position(self, image):

        image = cv2.cvtColor(np.uint8(image), cv2.COLOR_BGR2GRAY)
        return self._classifier.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE
        )   # [(x,y,w,h),...,]

    def __crop_face(self, image, face):
        # image is a PIL image, for now we assume each image has a single face on it
        # needed changes: for loop here and duplicate the labels

        [x,y,w,h] = face[0]
        face = image.crop((x,y,x+w, y+h))
        # Shows the image in image viewer
        #face.save("C:\\Users\\DIK\\abc.jpg")
        return face

    def get_name(self):
        return "CV Face Cascade"

    def get_cropped_face(self, image):
        face = self.__get_faces_position(image)
        if face == ():
            return
        return self.__crop_face(image, face)

    def is_face(self):
        return self._faces != []