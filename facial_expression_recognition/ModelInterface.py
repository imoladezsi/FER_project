class ModelInterface(object):
    # required parameters
    def __init__(self,img_dim, depth, dropout, init_lr, nr_classes):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

