import json
import sys
from datetime import datetime
import os
import keras

basePath = str(os.path.abspath(__file__))[:-13]

#Top level returns:
ret = {}
ret["output"] = "I have completed my assessment of your submission for lab 1."
ret["visibility"] = "visible"
ret["stdout_visibility"] = "visible"
max_score = 100

#Code Tests:
ret["tests"] = []
score = 0

startTime = datetime.now()

#================================
#================================
#QUESTION 1
#================================
#================================

print("\nCommencing assessment of code submitted for question 1 (Stop Sign Detection).")
question = {}
question["max_score"] = 20
question["name"] = "Stop Sign Detection"
question["output"] = ""
question["score"] = 0
mAcc = 0
#studentModel = keras.models.load_model("/autograder/submission/Q1.h5")
#dataGenerator = keras.preprocessing.image.ImageDataGenerator(samplewise_center=True)
#test = dataGenerator.flow_from_directory(imagePath, class_mode='categorical', batch_size=32, target_size=(64, 64))
#modelOutcome = studentModel.evaluate(test)

dataGenerator = keras.preprocessing.image.ImageDataGenerator(samplewise_center=True)
test = dataGenerator.flow_from_directory("./streetSigns", class_mode='categorical', batch_size=32, target_size=(64, 64))

try:
  print("Loading Model...")
  studentModel = keras.models.load_model("/autograder/submission/Q1.h5")
  dataGenerator = keras.preprocessing.image.ImageDataGenerator()
  print("Testing Model based on independent test set...")
  try:
    modelOutcome = studentModel.evaluate(test)
    print("Your model achieved an accuracy of " + str(round(modelOutcome[1]*100,4)) + " percent.")
    mAcc = modelOutcome[1] * 100
    question["score"] = round(min(1, modelOutcome[1]) * question["max_score"],2)
    print("Your score for this question is currently " + str(question["score"]) + " of a maximum possible " + str(question["max_score"]))
    
  except Exception as e:
    print("I was unable to run your model on my test dataset.")
    print("Exception: " + str(e))
    question["output"] = "Something went wrong!  Check the log."


except Exception as e:
  print("I was unable to load Q1.h5.  Please check your upload is correctly formatted.")
  print("Note that if you have not yet started on Question 1, you may see this error.")
  print("(i.e., if you have not yet started submitting a Q1.h5 file!)")
  print("Exception: " + str(e))
  question["output"] = "Something went wrong!  Check the log."

ret["tests"].append(question)

#================================
#================================
#QUESTION 2
#================================
#================================

print("\nCommencing assessment of code submitted for question 2 (Bug Classification).")
question = {}
question["max_score"] = 20
question["name"] = "Bug Classification"
question["output"] = ""
question["score"] = 0
Q2Acc = 0
#studentModel = keras.models.load_model("/autograder/submission/Q2.h5")
#dataGenerator = keras.preprocessing.image.ImageDataGenerator(samplewise_center=True)
#test = dataGenerator.flow_from_directory(imagePath, class_mode='categorical', batch_size=32, target_size=(64, 64))
#modelOutcome = studentModel.evaluate(test)

dataGenerator = keras.preprocessing.image.ImageDataGenerator(samplewise_center=True)
test = dataGenerator.flow_from_directory("./bugs", class_mode='categorical', batch_size=32, target_size=(64, 64))

try:
  print("Loading Model...")
  studentModel = keras.models.load_model("/autograder/submission/Q2.h5")
  dataGenerator = keras.preprocessing.image.ImageDataGenerator()
  print("Testing Model based on independent test set...")
  try:
    modelOutcome = studentModel.evaluate(test)
    print("Your model achieved an accuracy of " + str(round(modelOutcome[1]*100,4)) + " percent.")
    Q2Acc = modelOutcome[1] * 100
    question["score"] = round(min(1, modelOutcome[1]) * question["max_score"],2)
    print("Your score for this question is currently " + str(question["score"]) + " of a maximum possible " + str(question["max_score"]))
    
  except Exception as e:
    print("I was unable to run your model on my test dataset.")
    print("Exception: " + str(e))
    question["output"] = "Something went wrong!  Check the log."


except Exception as e:
  print("I was unable to load Q2.h5.  Please check your upload is correctly formatted.")
  print("Note that if you have not yet started on Question 2, you may see this error.")
  print("(i.e., if you have not yet started submitting a Q2.h5 file!)")
  print("Exception: " + str(e))
  question["output"] = "Something went wrong!  Check the log."

ret["tests"].append(question)


#================================
#================================
#QUESTION 3
#================================
#================================

print("\nCommencing assessment of code submitted for question 3 (Disaster Classification).")
question = {}
question["max_score"] = 20
question["name"] = "Disaster Identification & Discrimination"
question["output"] = ""
question["score"] = 0
Q3Acc = 0
#studentModel = keras.models.load_model("/autograder/submission/Q2.h5")
#dataGenerator = keras.preprocessing.image.ImageDataGenerator(samplewise_center=True)
#test = dataGenerator.flow_from_directory(imagePath, class_mode='categorical', batch_size=32, target_size=(64, 64))
#modelOutcome = studentModel.evaluate(test)

dataGenerator = keras.preprocessing.image.ImageDataGenerator(samplewise_center=True)
test = dataGenerator.flow_from_directory("./disaster", class_mode='categorical', batch_size=16, target_size=(256, 256))

try:
  print("Loading Model...")
  studentModel = keras.models.load_model("/autograder/submission/Q3.h5")
  dataGenerator = keras.preprocessing.image.ImageDataGenerator()
  print("Testing Model based on independent test set...")
  try:
    modelOutcome = studentModel.evaluate(test)
    print("Your model achieved an accuracy of " + str(round(modelOutcome[1]*100,4)) + " percent.")
    Q3Acc = modelOutcome[1] * 100
    question["score"] = round(min(1, modelOutcome[1]) * question["max_score"],2)
    print("Your score for this question is currently " + str(question["score"]) + " of a maximum possible " + str(question["max_score"]))
    
  except Exception as e:
    print("I was unable to run your model on my test dataset.")
    print("Exception: " + str(e))
    question["output"] = "Something went wrong!  Check the log."


except Exception as e:
  print("I was unable to load Q3.h5.  Please check your upload is correctly formatted.")
  print("Note that if you have not yet started on Question 3, you may see this error.")
  print("(i.e., if you have not yet started submitting a Q3.h5 file!)")
  print("Exception: " + str(e))
  question["output"] = "Something went wrong!  Check the log."

ret["tests"].append(question)

#LEADERBOARD
ret["leaderboard"] = []

tim = {}
tim["name"] = "Runtime (seconds)"
tim["value"] = str(datetime.now() - startTime)
tim["order"] = "asc"
ret["leaderboard"].append(tim)

acc = {}
acc["name"] = "Accuracy (Percentage) of Q1 Model"
acc["value"] = mAcc
ret["leaderboard"].append(acc)

acc = {}
acc["name"] = "Accuracy (Percentage) of Q2 Model"
acc["value"] = Q2Acc
ret["leaderboard"].append(acc)

acc = {}
acc["name"] = "Accuracy (Percentage) of Q2 Model"
acc["value"] = Q3Acc
ret["leaderboard"].append(acc)

json.dumps(ret)
outF = open("/autograder/results/results.json", "w")
json.dump(ret, outF)
outF.close()
