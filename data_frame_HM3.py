import csv
import pandas as pd
import numpy as np


fforner = pd.read_csv("FForner.csv")
gscalzott = pd.read_csv("GSscalzot.csv")
kevin = pd.read_csv("Kevin.csv")
goel = pd.read_csv("Goel.csv")

#
fforner = fforner[["NAME_company", "PURPOSE_company"]]
fforner = fforner.rename(columns = {'NAME_company': 'Name', "PURPOSE_company" :"Purpose"})

#
goel = goel[["0","1"]]
goel = goel.rename(columns = {'0': 'Name', "1" :"Purpose"})

#
kevin = kevin[["Name", "Purpose"]]



frames = [fforner, gscalzott, kevin, goel]
df = pd.concat(frames, ignore_index=True)
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth= 100
#print(df)
