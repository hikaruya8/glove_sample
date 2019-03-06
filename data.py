import re
import urllib.request
import zipfile

# zipファイルのダウンロード
urllib.request.urlretrieve('https://www.aozora.gr.jp/cards/001029/files/43291_ruby_20925.zip', '43291_ruby_20925.zip')
with zipfile.ZipFile('./43291_ruby_20925.zip') as zip_file:
    zip_file.extractall('.')
    
# テキストファイルから文字列を抽出
with open('./meditationes.txt', 'r', encoding='shift_jis') as f:
    text = f.read()

# 本文を抽出 (ヘッダとフッタを削除)
text = ''.join(text.split('\n')[23:346]).replace('　', '')
# 注釈 (［］) とルビ (《》) を削除
text = re.sub(r'(［.*?］)|(《.*?》)', '', text)
# 神の存在、及び人間の霊魂と肉体との区別を論証する、第一哲学についての省察 ...

# pip install Janome
from janome.analyzer import Analyzer
from janome.charfilter import UnicodeNormalizeCharFilter
from janome.tokenizer import Tokenizer
from janome.tokenfilter import POSKeepFilter, ExtractAttributeFilter

analyzer = Analyzer(
    [UnicodeNormalizeCharFilter()],
    Tokenizer(),
    [POSKeepFilter(['名詞', '動詞', '形容詞', '副詞']), ExtractAttributeFilter('base_form')]
)

tokens = [token for token in analyzer.analyze(text)]
# ['神', '存在', '人間', '霊魂', '肉体', ... ]

with open('./input.txt', 'w') as f:
    f.write(' '.join(tokens))

    with open('./vectors.txt', 'r') as original, open('./gensim_vectors.txt', 'w') as transformed:
    vocab_count = vectors.shape[0]  # 単語数
    size = vectors.shape[1]  # 次元数
    
    transformed.write(f'{vocab_count} {size}\n')
    transformed.write(original.read())  # 2行目以降はそのまま出力

from gensim.models import KeyedVectors

glove_vectors = KeyedVectors.load_word2vec_format('./gensim_vectors.txt', binary=False)