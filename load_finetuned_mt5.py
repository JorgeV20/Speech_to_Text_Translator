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

fine_tuned_model_checkpoint='./training/data/english_to_spanish/mt5-small_en-sp/checkpoint-4500'


tokenizer = AutoTokenizer.from_pretrained(fine_tuned_model_checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(fine_tuned_model_checkpoint)

print('model loaded')