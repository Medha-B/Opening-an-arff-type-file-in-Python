from scipy.io import arff
import pandas as pd
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile
from scipy.io.arff import loadarff

zfile = ZipFile(r"C:\Users\Subroto\Downloads\Breast.zip")
in_mem_fo = TextIOWrapper(BytesIO(zfile.read('Breast.arff')), encoding='utf-8')
data = loadarff(in_mem_fo)

df = pd.DataFrame(data[0])
df.head()
df.tail()
