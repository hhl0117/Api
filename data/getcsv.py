import pandas
import json
from common import getroot

rootpath = getroot.root_path

csvpath = rootpath + "data/post01.csv"

datacsv = pandas.read_csv(csvpath, sep='\t')

datajson = pandas.DataFrame.to_json(self=datacsv,orient='records')

datalist = json.loads(datajson)

print(datalist)