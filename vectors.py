import pandas as pd
import numpy as np

# 単語ラベルをインデックスにしてDataFrameで読み込む
vectors = pd.read_csv('./vectors.txt', delimiter=' ', index_col=0, header=None)

vector = vectors.loc['人間',:].values

with open('./vectors.txt', 'r') as original, open('./gensim_vectors.txt', 'w') as transformed:
	vocab_count = vectors.shape[0]  # 単語数
	size = vectors.shape[1]  # 次元数
	transformed.write(f'{vocab_count} {size}\n')
	transformed.write(original.read())  # 2行目以降はそのまま出力

from gensim.models import KeyedVectors

glove_vectors = KeyedVectors.load_word2vec_format('./gensim_vectors.txt', binary=False)

print(glove_vectors.most_similar("精神"))