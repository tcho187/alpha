# Fraud Service
# Author: Thomas Cho

## Extracting the model
I saved the model using pickle. I also saved the test dataset as JSON. Here's the code that I ran:
```
import pickle
pickle.dump(clf, open("../model.pkl","wb"))
X_test_te.to_json("../test_set.json", orient="split")
```


## How to run the API
Download Docker Desktop if you don't have it. https://www.docker.com/

Run the following commands in the command line:
```
docker build -t rubberduck .
docker run -p 5000:5000 rubberduck
```

Go to http://localhost:5000/ and you will see "Machine Learning Inference".

## How to send a request
post_example.py is an example. I load the test.json file. I take the first row and make a POST request to /inference with the first record of features. I return a JSON object with either the label Fraud or Not Fraud.