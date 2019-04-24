# THIS IS Tensorflow 2.0 Logger Utils

import pandas as pd
import tensorflow as tf

class SimpleLogger(tf.keras.callbacks.Callback):

    def __init__(self):
        super(SimpleLogger, self).__init__()
        self.logs = []

    def on_train_begin(self, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        self.logs.append([epoch, logs.get("loss")])

    def on_train_end(self, logs=None):
        pass
    
    def show(self, metric="loss"):
        df = pd.DataFrame(logger.logs, columns=["epoch", "loss"])
        df.set_index("epoch", inplace=True)
        return df.plot()

