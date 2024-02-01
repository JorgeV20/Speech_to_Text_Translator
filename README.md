# Speech to Text Translator

Speech to Text Translator is an application developed in python and trained using AWS Sagemaker in a ml.t3.2xlarge instance. The goal of this application is to translate from english to spanish language using the voice as input. The model used was the mT5 trained with data from https://www.kaggle.com/datasets/lonnieqin/englishspanish-translation-dataset.

## Repository Structure
- [`README.md`](README.md): The file contais the description of the project.
- [`main.py`](main.py): Execute the Speech Translator.
- [`recording_audio.py`](recording_audio.py): The file records the audio using the computer's microphone. Then it saves the recorded audio as a .wav file.
- [`speech_to_text.py`](speech_to_text.py): The file takes a recorded audio in .wav format and brings its text representation. The speech to text recognition is done using the Google Speech Recognition API.
- [`load_finetuned_mt5_example.ipynb`](load_finetuned_mt5_example.ipynb): The notebook ilustrates how to load the finetuned mT5 model and some examples of the translation from english to spanish.
- [`training`](training): The folder contains the notebook trained in AWS Sagemaker instance and the dataset
    - [`flan_mt5_en_sp.ipynb`](training/flan_mt5_en_sp.ipynb): Notebook trained in AWS Sagemaker using a ml.t3.2xlarge instance. 10 000 samples where used for the training.
    - [`data/english_to_spanish/dataset`](training/data/english_to_spanish/dataset): The folder contains the dataset.

## Note
The mT5 model was finetuned using 10 000 samples and it took 3h 49min in a ml.t3.2xlarge instance.

## Future work
- Retrain the model with more samples in order to increase the performance.
