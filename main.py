from speech_to_text import get_audio

import os
import torch
import random
import evaluate
import transformers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional
from dataclasses import dataclass 
from time import perf_counter
from torch.utils.data import Dataset, DataLoader
from datasets import load_dataset, disable_progress_bar
from transformers import (
    AutoConfig,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    EarlyStoppingCallback
)


#Loading finetuned model
class finetuned_model():
    

    def __init__(self):
        self.fine_tuned_model_checkpoint = './training/data/english_to_spanish/mt5-small_en-sp/checkpoint-4500'
        self.tokenizer = AutoTokenizer.from_pretrained(self.fine_tuned_model_checkpoint)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.fine_tuned_model_checkpoint)
        print('Model loaded')

#Defining the generator for translations
def generate_translation(model, tokenizer, example):
    """print out the source, target and predicted raw text."""
    source = example
    print(source)
    input_ids = tokenizer(source)["input_ids"]
    input_ids = torch.LongTensor(input_ids).view(1, -1).to(model.device)
    print(input_ids)
    generated_ids = model.generate(inputs=input_ids, max_length=20)
    prediction = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    print('English source: ', source)
    print('Spanish prediction: ', prediction)


flan_model=finetuned_model()

var='y'

while var=='y':
    start=input('Are you ready to start? (Press y/n): ')
    text_audio=get_audio('test')
    generate_translation(flan_model.model, flan_model.tokenizer, text_audio)

    var=input('Do you want to translate another phrase? (Press y/n): ')


print('End of translation')
