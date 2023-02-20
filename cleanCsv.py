import pandas as pd


def readCsv(file):
    return pd.read_csv(file)


def checkDupes(df, column):
    mask = df.loc[df[column].duplicated(keep=False), :]
    df.loc[mask, column] = ""
    return df


def toNumeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df


def nullToMean(df, column):
    df.loc[df[column].isnull(), column] = df[column].mean()
    return df


def defaultDateTime(df, column):
    df[column] = pd.to_datetime(df[column], format='%d/%m/%Y', errors='coerce')
    return df


def toCsv(df, name):
    df.to_csv(name, index=False)
    return df
