import numpy as np

def sigmoid(x):
    return 1/ (1+ np.exp(-x))

training_input = np.array([[1,1,1],
                           [0,0,0],
                           [0,1,0],
                           [1,0,0]])

desired = np.array([[1,0,0,1]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1))-1

print("Random starting weight(s): ")
print(synaptic_weights)

def sigderivative(x):
    return sigmoid(x) * (1-sigmoid(x))

for repeat in range(200000):
    T_inputs = training_input

    outputs = sigmoid(np.dot(T_inputs, synaptic_weights))

    error = desired - outputs

    adjustments = error * sigderivative(outputs)

    synaptic_weights += np.dot(T_inputs.T, adjustments)
print('Synaptic weights after learning: ')
print(synaptic_weights)

print('Outputs after learning: ')
print(outputs)


