import os
import pickle

from sklearn.preprocessing import LabelBinarizer
from keras.engine.saving import load_model

from facial_expression_recognition import ModelInterface
from interfaces.Repository import Repository

import numpy as np

from load_data import DataGenerator
from utils.Helpers import Helpers


class FerRepository(Repository):

    @staticmethod
    def load_label_binarizer(model_path):
        print("[INFO] loading label binarizer...")
        lst = model_path.split(os.path.sep)
        lb = os.path.join(os.path.sep.join(lst[0:-1]), "label_binarizer_" + str(lst[-1]))
        mlb = pickle.loads(open(lb, "rb").read())
        return mlb

    @staticmethod
    def save_model(model: ModelInterface, output_path, save_as):
        print("[INFO] saving model...")
        model.save_weights(os.path.join(output_path, save_as + '.h5'))
        model.save(os.path.join(output_path, save_as))

    @staticmethod
    def save_label_binarizer(lb_object, output_path, save_as):
        print("[INFO] saving label binarizer...")
        f = open(os.path.join(output_path, "label_binarizer_" + save_as), "wb")
        f.write(pickle.dumps(lb_object))
        f.close()

    @staticmethod
    def load_model(model, model_path):
        print("[INFO] loading model..")
        return model.load_model(model_path)

    @staticmethod
    def train(model, dataset_path, img_dim, split, epochs, batch_size):
        try:
            gen = DataGenerator(dataset_path)
            data, labels = gen.get_images(img_dim)


            # manually split them
            split = int(len(data)*split/100)
            train_x, test_x = data[:split], data[split:]
            train_y, test_y = labels[:split], labels[split:]

            lb = LabelBinarizer()
            train_y = lb.fit_transform(train_y)
            test_y = lb.transform(test_y)

            # TODO: PNG problem
            # train model
            train_x = np.array(train_x)
            train_y = np.array(train_y)
            test_x = np.array(test_x)
            test_y = np.array(test_y)
            return lb, model.fit(train_x, train_y, test_x, test_y, epochs, batch_size)

        except Exception as e:
            print(e)

    @staticmethod
    def save_training_data(model, lb, output_path, save_as, figure_epochs = 0):
        FerRepository.save_model(model, output_path, save_as)
        FerRepository.save_label_binarizer(lb, output_path, save_as)
        if figure_epochs != 0:
            Helpers.save_figure(model.get_history(), figure_epochs, output_path, save_as)




    @staticmethod
    def predict(image_path):
        pass

    @staticmethod
    def estimate(test_dataset_path):
        pass


