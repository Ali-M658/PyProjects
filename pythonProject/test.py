import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x0 = np.random.randn(100,2) - np.array([2,2])
y0 = np.zeros(100)

x1 = np.random.randn(100,2) + np.array([2,2])
y1 = np.ones(100)


class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):

        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros(hidden_size)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def backward(self, X, Y, learning_rate):
        m = Y.shape[0]
        dz2 = self.a2 - Y.reshape(-1, 1)
        dw2 = np.dot(self.a1.T, dz2) / m
        db2 = np.sum(dz2, axis=0) / m
        dz1 = np.sum(dz2, self.W2.T) * self.sigmoid_derivative(self.z1)
        dw1 = np.dot(dz2, self.W2.T) * self.sigmoid_derivative(self.z1)
        dW1 = np.dot(X.T, dz1) / m
        db1 = np.sum(dz1, axis=0) / m

        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        self.W2 -= learning_rate * dw2
        self.b2 -= learning_rate * db2

    def train(self, X, Y, epochs, learning_rate):
        for _ in range(epochs):
            self.forward(X)
            self.backward(X, Y, learning_rate)

    def predict(self, X):
        return self.forward(X).flatten() > 0.5

nn = SimpleNN(input_size=2, hidden_size=3, output_size=1)
nn.train(X, Y, epochs=1000, learning_rate=0.1)

def plot_decision_boundary(nn, X, Y):
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    z = nn.predict(np.c_[xx.ravel(), yy.ravel()])

    z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
    plt.show()

plot_decision_boundary(nn, X, Y)