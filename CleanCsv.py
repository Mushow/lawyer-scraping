import pandas as pd


def readCsv(file):
    return pd.read_csv(file)


def checkDupes(df, column):
    mask = df.loc[df[column].duplicated(keep=False), :]
    df.loc[mask, column] = ""


def toNumeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')


def nullToMean(df, column):
    df.loc[df[column].isnull(), column] = df[column].mean()


def defaultDateTime(df, column):
    df[column] = pd.to_datetime(df[column], format='%d/%m/%Y', errors='coerce')


def toCsv(df, name):
    df.to_csv(name, index=False)
