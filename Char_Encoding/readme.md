This a simple way of embedding a character down from a one hot vector of size 26 to a smaller vector

The model does this through having a network architure that bottlenecks the input vector down to a small layerand then re expands it.

The model is able to be trained by passing any character through it and checking how well it was decoded.

It's also a personal experiment on how small of a vector can a character be encoded to.

Given a network size of two 64 node hidden layers, it can be compressed to a 3 node layer.