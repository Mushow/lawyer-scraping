import pandas as pd

file = 'lawyers.csv'
data = pd.read_csv(file)


def checkDupes(column):
    mask = data.loc[data[column].duplicated(keep=False), :]
    data.loc[mask, column] = ""


def toNumeric(column):
    data[column] = pd.to_numeric(data[column], errors='coerce')


def nullToMean(column):
    data.loc[data[column].isnull(), column] = data[column].mean()


def defaultDateTime(column):
    data[column] = pd.to_datetime(data[column], format='%d/%m/%Y', errors='coerce')


def toCsv(data_frame, name):
    data_frame.to_csv(name, index=False)
