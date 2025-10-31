
"""This module loads a pre-trained machine learning pipeline from a binary file.
It uses the pickle library to deserialize the pipeline object for further use.
"""

import pickle



#load the pipeline
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

#make predictions
data = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

result = pipeline.predict_proba(data)[0,1]
print(result)