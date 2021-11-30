import pandas as pd
import numpy as np

dadjokes_df = pd.read_csv('dadjokes.csv')
jokes_df = pd.read_csv('jokes.csv')
all_filenames = ["dadjokes.csv", "jokes.csv"]
# print(jokes_df.head())
# print("\n", dadjokes_df.head())

dadjokes_df["subreddit"].replace({"dadjokes": 0}, inplace = True)
jokes_df["subreddit"].replace({"Jokes": 1}, inplace = True)
print(jokes_df.head())
print("\n", dadjokes_df.head())

dadjokes_df.drop_duplicates()
jokes_df.drop_duplicates()
theFrames = pd.concat((jokes_df, dadjokes_df))
theFrames.to_csv("combinedData.csv", index = False)