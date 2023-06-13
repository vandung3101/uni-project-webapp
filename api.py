# translate tapaco_paraphrases_dataset.csv from english to vietnamese
# save to tapaco_paraphrases_dataset_vi.csv
# using google translate api

import pandas as pd
import time
from googletrans import Translator

translator = Translator()

df = pd.read_csv("tapaco_paraphrases_dataset.csv", sep="\t")
# only translate the first 1000 rows
df = df[:1000]
df["Text"] = df["Text"].apply(lambda x: translator.translate(x, src="en", dest="vi").text)
df["Paraphrase"] = df["Paraphrase"].apply(lambda x: translator.translate(x, src="en", dest="vi").text)