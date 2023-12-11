# Group 3: Building a Chatbot with Deep Natural Language Processing


# Importing the libraries
import numpy as np
import tensorflow as tf
import re # This helps in cleaning the data
import time

######## PART 1: DATA PREPROCESSING #############

# Importing the dataset
lines = open('movie_dialog/movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n') 
conversations = open('movie_dialog/movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

# Creating a dictionary that maps each line and its id
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ') # _ specifies that it is a temporary variable
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]
        
        
# Creating a list of all of the conversations
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
    conversations_ids.append(_conversation.split(','))
    
    
# Getting separately the questions and the answers
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        

# Performing data cleaning of the texts (Reusable function)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"that ' s", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"doesn't", "does not", text)
    text = re.sub(r"there's", "there is", text)
    text = re.sub(r"don't", "do not", text)
    text = re.sub(r"don ' t", "do not", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"didn't", "did not", text)
    text = re.sub(r"you're", "you are", text)
    text = re.sub(r"you ' re", "you are", text)
    text = re.sub(r"wasn't", "was not", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"haven't", "have not", text)
    text = re.sub(r"weren't", "were not", text)
    text = re.sub(r"woudn't", "would not", text)
    text = re.sub(r"isn't", "is not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"can ' t", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]", "", text)
    return text

# Cleaning the questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))
 
# Cleaning the answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))




    
