#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excute code
Creating a network and excute
"""


import mnist_loader
import Network

# load data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

# set up a Network with 30 (try 100) hidden neurons
net = Network.Network([784, 100, 10])

# use SGD to learn from the MNIST training_data over 30 epochs
# with a mini-batch size of 10, and a learning rate of η=3.0 (try 1.0),
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)


