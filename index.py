from textblob import TextBlob
import json

with open('chatbot_data.json') as f:
    data = json.load(f)

mainList = []
negativeList = []
positiveList = []
negativeCount = 0;
positiveCount = 0;

for val in data:
    json_string = val['jsonValue']
    obj = json.loads(json_string)
    text = obj['userInput'].strip()
    if(text != 'hello' and text != ''):
        mainList.append(text)

for userInput in mainList:
    # print(userInput)
    analysis = TextBlob(userInput)
    # print(analysis.sentiment)
    if(analysis.sentiment.polarity <= -0.9):
        negativeCount += 1
        negativeList.append(userInput)
    elif(analysis.sentiment.polarity >= 0.9):
        positiveCount += 1
        positiveList.append(userInput)
        # print(userInput)
        # print(analysis.sentiment)

print(positiveCount)
print(*positiveList, sep='\n')

print(negativeCount)
print(*negativeList, sep='\n')

