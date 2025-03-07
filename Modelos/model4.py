# Definición de la arquitectura U-Net
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dropout, UpSampling2D, concatenate, BatchNormalization, Activation, ReLU, Conv2DTranspose

def unet_model(input_shape=(112, 112, 1), n_classes=1, kernel_out=1, activation='sigmoid'):
    inputs = Input(shape=input_shape)

    conv1 = Conv2D(64, 3, padding='same')(inputs)
    conv1 = BatchNormalization()(conv1)
    conv1 = ReLU()(conv1)
    conv1 = Conv2D(64, 3, padding='same')(conv1)
    conv1 = BatchNormalization()(conv1)
    conv1 = ReLU()(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = Conv2D(128, 3, padding='same')(pool1)
    conv2 = BatchNormalization()(conv2)
    conv2 = ReLU()(conv2)
    conv2 = Conv2D(128, 3, padding='same')(conv2)
    conv2 = BatchNormalization()(conv2)
    conv2 = ReLU()(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = Conv2D(256, 3, padding='same')(pool2)
    conv3 = BatchNormalization()(conv3)
    conv3 = ReLU()(conv3)
    conv3 = Conv2D(256, 3, padding='same')(conv3)
    conv3 = BatchNormalization()(conv3)
    conv3 = ReLU()(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = Conv2D(512, 3, padding='same')(pool3)
    conv4 = BatchNormalization()(conv4)
    conv4 = ReLU()(conv4)
    conv4 = Conv2D(512, 3, padding='same')(conv4)
    conv4 = BatchNormalization()(conv4)
    conv4 = ReLU()(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

    conv5 = Conv2D(1024, 3, padding='same')(pool4)
    conv5 = BatchNormalization()(conv5)
    conv5 = ReLU()(conv5)
    conv5 = Conv2D(1024, 3, padding='same')(conv5)
    conv5 = BatchNormalization()(conv5)
    conv5 = ReLU()(conv5)
    drop5 = Dropout(0.5)(conv5)
    pool5 = MaxPooling2D(pool_size=(2, 2))(drop5)

    conv6 = Conv2D(2048, 3, padding='same')(pool5)
    conv6 = BatchNormalization()(conv6)
    conv6 = ReLU()(conv6)
    conv6 = Conv2D(2048, 3, padding='same')(conv6)
    conv6 = BatchNormalization()(conv6)
    conv6 = ReLU()(conv6)
    drop6 = Dropout(0.5)(conv6)

    up7 = Conv2DTranspose(1024, 2, strides=(2, 2), padding='same')(drop6)
    up7 = concatenate([up7, drop5])
    conv7 = Conv2D(1024, 3, padding='same')(up7)
    conv7 = BatchNormalization()(conv7)
    conv7 = ReLU()(conv7)
    conv7 = Conv2D(1024, 3, padding='same')(conv7)
    conv7 = BatchNormalization()(conv7)
    conv7 = ReLU()(conv7)

    up8 = Conv2DTranspose(512, 2, strides=(2, 2), padding='same')(conv7)
    up8 = concatenate([up8, drop4])
    conv8 = Conv2D(512, 3, padding='same')(up8)
    conv8 = BatchNormalization()(conv8)
    conv8 = ReLU()(conv8)
    conv8 = Conv2D(512, 3, padding='same')(conv8)
    conv8 = BatchNormalization()(conv8)
    conv8 = ReLU()(conv8)

    up9 = Conv2DTranspose(256, 2, strides=(2, 2), padding='same')(conv8)
    up9 = concatenate([up9, conv3])
    conv9 = Conv2D(256, 3, padding='same')(up9)
    conv9 = BatchNormalization()(conv9)
    conv9 = ReLU()(conv9)
    conv9 = Conv2D(256, 3, padding='same')(conv9)
    conv9 = BatchNormalization()(conv9)
    conv9 = ReLU()(conv9)

    up10 = Conv2DTranspose(128, 2, strides=(2, 2), padding='same')(conv9)
    up10 = concatenate([up10, conv2])
    conv10 = Conv2D(128, 3, padding='same')(up10)
    conv10 = BatchNormalization()(conv10)
    conv10 = ReLU()(conv10)
    conv10 = Conv2D(128, 3, padding='same')(conv10)
    conv10 = BatchNormalization()(conv10)
    conv10 = ReLU()(conv10)

    up11 = Conv2DTranspose(64, 2, strides=(2, 2), padding='same')(conv10)
    up11 = concatenate([up11, conv1])
    conv11 = Conv2D(64, 3, padding='same')(up11)
    conv11 = BatchNormalization()(conv11)
    conv11 = ReLU()(conv11)
    conv11 = Conv2D(64, 3, padding='same')(conv11)
    conv11 = BatchNormalization()(conv11)
    conv11 = ReLU()(conv11)

    conv12 = Conv2D(n_classes, kernel_out, activation=activation)(conv11)

    conv13 = Conv2D(n_classes, kernel_out, activation=activation)(conv12)

    model = tf.keras.Model(inputs=inputs, outputs=conv13, name='U-Net_2')
    
    return model