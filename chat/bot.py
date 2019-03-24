import os
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def extract_messages(filename):
    with open(filename, encoding='utf8') as json_file:
        data = json.load(json_file)
        return [x['message'] for x in data['messages']]

def read_directory(directory, res_list):
    for filename in os.listdir(directory):
        try:
            res_list.extend(extract_messages('{0}/{1}'.format(directory,filename)))
        except Exception as e:
            print(e)

def learn():
    dir1 = "small_dataset/SupportMKDO/"
    dir2 = "small_dataset/SupportNPO/"
    dir3 = "small_dataset/SupportOIR/"
    dir4 = "small_dataset/SupportOPR/"
    dir5 = "small_dataset/SupportORPB/"
    dir6 = "small_dataset/SupportReception/"
    dir7 = "small_dataset/SupportSPD/"
    dir8 = "small_dataset/SupportSynerdocs/"

    conversation1 = []
    conversation2 = []
    conversation3 = []
    conversation4 = []
    conversation5 = []
    conversation6 = []
    conversation7 = []
    conversation8 = []

    read_directory(dir1, conversation1)
    read_directory(dir2, conversation2)
    read_directory(dir3, conversation3)
    read_directory(dir4, conversation4)
    read_directory(dir5, conversation5)
    read_directory(dir6, conversation6)
    read_directory(dir7, conversation7)
    read_directory(dir8, conversation8)

    chatbot = ChatBot("Jimmy")

    trainer = ListTrainer(chatbot)

    trainer.train(conversation1)
    trainer.train(conversation2)
    trainer.train(conversation3)
    trainer.train(conversation4)
    trainer.train(conversation5)
    trainer.train(conversation6)
    trainer.train(conversation7)
    trainer.train(conversation8)
