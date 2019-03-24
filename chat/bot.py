import os
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def extract_messages(filename):
    with open(filename, encoding='utf8') as json_file:
        data = json.load(json_file)
        message = ""
        flag = 0
        for x in data['messages']:
            if flag == 0:
                if x["sender"]=='user' :
                    message += x["message"]
                    flag = 1
                if x["sender"]=='support':
                    flag = 0
            

        #message.append(filename)
        return message

def read_directory(directory, res_list):
    for filename in os.listdir(directory):
        messages = ""
        try:
            messages += extract_messages('{0}/{1}'.format(directory,filename))
            res_list.append(messages) 
            res_list.append(directory)
            print(res_list)
            print("---------------------")
        except Exception as e:
            print(e)

def upd_ds(dir):
    for filename in os.listdir(dir):
        #print(os.listdir(dir))
        #with open(f"/Users/kirill/Documents/GitHub/directum-chat-bot/{}", 'r+', encoding='utf8') as json_file:
        with open(f"/Users/kirill/Documents/GitHub/directum-chat-bot/{dir}{filename}", 'r+') as json_file:
            data = json.load(json_file)
            for x in data['messages']:
                if x["sender"]=='support':
                    x["message"] = dir 
                    json_file.seek(0)        # <--- should reset file position to the beginning.
                    json.dump(data, json_file, indent=4)
                    json_file.truncate()     # remove remaining part
    
           

def learn():
    # dir1 = "small_dataset/SupportMKDO/"
    # dir2 = "small_dataset/SupportNPO/"
    # dir3 = "small_dataset/SupportOIR/"
    # dir4 = "small_dataset/SupportOPR/"
    # dir5 = "small_dataset/SupportORPB/"
    # dir6 = "small_dataset/SupportReception/"
    # dir7 = "small_dataset/SupportSPD/"
    # dir8 = "small_dataset/SupportSynerdocs/"

    dir9 = "manual_dataset/SupportNPO/"
    dir10 = "manual_dataset/SupportReception/"

    # upd_ds(dir1)
    # upd_ds(dir2)
    # upd_ds(dir3)
    # upd_ds(dir4)
    # upd_ds(dir5)
    # upd_ds(dir6)
    # upd_ds(dir7)
    # upd_ds(dir8)

    upd_ds(dir9)
    upd_ds(dir10)

    # conversation1 = []
    # conversation2 = []
    # conversation3 = []
    # conversation4 = []
    # conversation5 = []
    # conversation6 = []
    # conversation7 = []
    # conversation8 = []

    conversation9 = []
    conversation10 = []

    # read_directory(dir1, conversation1)
    # read_directory(dir2, conversation2)
    # read_directory(dir3, conversation3)
    # read_directory(dir4, conversation4)
    # read_directory(dir5, conversation5)
    # read_directory(dir6, conversation6)
    # read_directory(dir7, conversation7)
    # read_directory(dir8, conversation8)

    read_directory(dir9, conversation9)
    read_directory(dir10, conversation10)

    #print(conversation1)

    chatbot = ChatBot("Jimmy")

    trainer = ListTrainer(chatbot)

    # trainer.train(conversation1)
    # trainer.train(conversation2)
    # trainer.train(conversation3)
    # trainer.train(conversation4)
    # trainer.train(conversation5)
    # trainer.train(conversation6)
    # trainer.train(conversation7)
    # trainer.train(conversation8)

    trainer.train(conversation9)
    trainer.train(conversation10)

    return chatbot
