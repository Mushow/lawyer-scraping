import pandas as pd


def readCsv(file):
    return pd.read_csv(file)


def sanitiseDupes(df, column):
    mask = df.loc[df[column].duplicated(keep=False), :]
    df.loc[mask, column] = ""
    return df


def sanitiseHeight(df, column):
    df = df[column].str[:-1]
    pd.to_numeric(df[column], errors='coerce')
    return df


def sanitiseEmails(df, column):
    df[column] = df[column].str.split(',', n=1, expand=True)[0]
    return df


def toNumeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df


def nullToMean(df, column):
    df[column] = pd.to_numeric(df[column], downcast='integer', errors='coerce')
    df[column] = df[column].fillna(value=df[column].mean())
    return df


def nullToZero(df, column):
    df[column] = df[column].fillna(value=0)
    return df


def dropNull(df, columnsArray):
    df = df.dropna(subset=columnsArray)
    return df


def nullToUnknown(df, column):
    df[column] = df[column].fillna(value="Unknown")
    return df


def defaultDateTime(df, column):
    return pd.to_datetime(df[column], format='%d/%m/%Y', errors='coerce')


def toCsv(df, name):
    df.to_csv(name, index=False)
    return df
