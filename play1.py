
import pandas as pd
import time
from googletrans import Translator

translator = Translator()

df = pd.read_csv("tapaco_paraphrases_dataset.csv", sep="\t")

start_index = 25000
end_index = 35000

for i in range(start_index, end_index):
    df["Text"][i] = translator.translate(df["Text"][i], src="en", dest="vi").text
    df["Paraphrase"][i] = translator.translate(df["Paraphrase"][i], src="en", dest="vi").text
    print(i)

df.to_csv("tapaco_paraphrases_dataset_vi5.csv", sep="\t", index=False)