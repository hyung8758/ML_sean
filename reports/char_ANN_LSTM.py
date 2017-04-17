'''
Word prediction training with two methods: ANN and LSTM(RNN)

                                                                    Written by Hyungwon Yang
                                                                                2017. 04. 17
                                                                                    EMCS Lab
'''
import numpy as np
import main.setvalues as set
import main.networkmodels as net


# import data.
ann_data = np.load('train_data/pg8800_ann_char_data.npz')
train_input = ann_data['train_input']
train_output = ann_data['train_output']
test_input = ann_data['test_input']
test_output = ann_data['test_output']

vocab_size = train_input.shape[1]
train_data_size = train_input.shape[0]
test_data_size = test_input.shape[0]

### ANN
# parameter setting.

fineTrainEpoch = 200
fineLearningRate = 0.001
learningRateDecay = 'off' # on, off
batchSize = 100
hiddenLayers = [200]
problem = 'classification' # classification, regression
hiddenFunction= 'tanh'
costFunction = 'adam' # gradient, adam
validationCheck = 'on' # if validationCheck is on, then 20% of train data will be taken for validation.
PlotGraph = 'off'

DNN_values = set.setParam(inputData=train_input,
                    targetData=train_output,
                    hiddenUnits=hiddenLayers
                    )

# Setting hidden layers: weightMatrix and biasMatrix
weightMatrix = DNN_values.genWeight()
biasMatrix = DNN_values.genBias()
# Generating input symbols.
input_x, input_y = DNN_values.genSymbol()

dnn = net.DNNmodel(inputSymbol=input_x,
                   outputSymbol=input_y,
                   problem=problem,
                   fineTrainEpoch=fineTrainEpoch,
                   fineLearningRate=fineLearningRate,
                   learningRateDecay=learningRateDecay,
                   batchSize=batchSize,
                   hiddenFunction=hiddenFunction,
                   costFunction=costFunction,
                   validationCheck=validationCheck,
                   weightMatrix=weightMatrix,
                   biasMatrix=biasMatrix
                   )

# Generate a DNN network.
dnn.genDNN()
# Train the DNN network.
dnn.trainDNN(train_input,train_output)
# Test the trained DNN network.
dnn.testDNN(test_input,test_output)
# Save the trained parameters.
vars = dnn.getVariables()
# Terminate the session.
dnn.closeDNN()

####################################################################################################
### LSTM

import numpy as np
import main.setvalues as set
import main.lstmnetworkmodels as net

# import data.
ann_data = np.load('train_data/pg8800_lstm_char_data.npz')
train_input = ann_data['train_input']
train_output = ann_data['train_output']
test_input = ann_data['test_input']
test_output = ann_data['test_output']

# parameters
trainEpoch = 200
learningRate = 0.001
learningRateDecay = 'off' # on, off
batchSize = 100
hiddenLayers = [200]
timeStep = 20
problem = 'classification' # classification, regression
costFunction = 'adam' # gradient, adam
plotOption = 'off'
validationCheck = 'on' # if validationCheck is on, then 20% of train data will be taken for validation.

lstm_values = set.simpleLSTMParam(inputData=train_input,
                           targetData=train_output,
                           timeStep=timeStep,
                           hiddenUnits=hiddenLayers
                           )

# Setting hidden layers: weightMatrix and biasMatrix
lstm_weightMatrix = lstm_values.genWeight()
lstm_biasMatrix = lstm_values.genBias()
lstm_input_x,lstm_input_y = lstm_values.genSymbol()

lstm_net = net.simpleLSTMmodel(inputSymbol=lstm_input_x,
                               outputSymbol=lstm_input_y,
                               problem=problem,
                               trainEpoch=trainEpoch,
                               learningRate=learningRate,
                               timeStep=timeStep,
                               batchSize=batchSize,
                               validationCheck=validationCheck,
                               weightMatrix=lstm_weightMatrix,
                               biasMatrix=lstm_biasMatrix)

# Generate a RNN(lstm) network.
lstm_net.genLSTM()
# Train the RNN(lstm) network.
lstm_net.trainLSTM(train_input,train_output)
# Test the trained RNN(lstm) network.
lstm_net.testLSTM(test_input,test_output)
# Save the trained parameters.
vars = lstm_net.getVariables()
# Terminate the session.
lstm_net.closeLSTM()