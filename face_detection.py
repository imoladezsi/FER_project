import os
import pickle
import sys

from load_data import DataGenerator
#from viola_jones import ViolaJones

batch_sz = int(sys.argv[2]) if len(sys.argv) == 3 else 0
gen = DataGenerator(sys.argv[1])
data = gen.data_generator(batch_sz) if len(sys.argv) == 3 else gen.get_images()
# image, label = next(data) this is how it is returned

# get an image and its label

# path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "viola_jones")
# clf = ViolaJones.load(path)
# fd = FaceDetector(clf)
# is_detection = fd.was_face_detected(image)
# if not is_detection:
#     raise Exception("No face detected on this image")

# fd.get_cropped_face(image)
