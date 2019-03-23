import os
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def create_np_array_from_vector(vector):
    vec_arr = vector.toarray()
    vec_list = []

    for i in range(0, vector.shape[1]):
        vec_list.append(vec_arr[0,i])

    return np.array(vec_list)

def extract_messages(filename):
    with open(filename, encoding='utf8') as json_file:
        data = json.load(json_file)
        return [x['message'] for x in data['messages'] if x["sender"]=='user']

def read_directory(directory, res_list):
    for filename in os.listdir(directory):
        try:
            res_list.extend(extract_messages('{0}/{1}'.format(directory,filename)))
        except:
            print('Some error in extracting')

def vectorize(common_list):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(common_list)
    return vectorizer


reception_msg = []
npo_msg = []

reception_directory = "small_dataset/SupportReception/"
npo_directory = "small_dataset/SupportNpO/"

read_directory(reception_directory, reception_msg)
read_directory(npo_directory, npo_msg)

common_list = reception_msg + npo_msg
vector_obj = vectorize(common_list)
print(vector_obj.vocabulary_)

message='ключи занести или идете? А то я переживаю что уйду и никого не будет'
vector = vector_obj.transform([message])

print(vector)
print(vector.shape)
