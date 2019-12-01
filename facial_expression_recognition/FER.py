import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

class FER(object):
    def __init__(self):
        pass


    def load_model(self,path):
        return None

    def save_model(self, path):
        pass

    @staticmethod
    def train(data, labels, model, params):

        # use numpy
        data = np.array(data)
        labels = np.array(labels)

        # randomize them


        # manually split them
        training_data, test_data = data[:80, :], data[80:, :]
        training_labels, test_labels = labels[:80, :], labels[80:, :]

        # transform labels
        mlb = MultiLabelBinarizer()
        training_labels = mlb.fit_transform(training_labels)
        testing_labels = mlb.fit_transform(test_labels)

        # train model
        model.fit()
        # save


    def predict(self, image_path):
        pass

    def estimate(self, test_dataset_path):
        pass

