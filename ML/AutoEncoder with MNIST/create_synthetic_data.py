import tensorflow as tf
import matplotlib.pyplot as plt


(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()


def show_image(image, label):

    plt.imshow(image, cmap='gray_r')
    plt.title('Label: {}'.format(label))
    plt.show()


for i in range(20):
    show_image(X_train[i], y_train[i])