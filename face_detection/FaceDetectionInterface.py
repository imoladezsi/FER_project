class FaceDetectionInterface(object):
    """
    All the face detection algorithms need to implement a common interface

    """
    def __init__(self, classifier):
        self.__classifier = classifier


    def is_face(self):
        raise NotImplementedError

    def get_face_position(self, image):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

