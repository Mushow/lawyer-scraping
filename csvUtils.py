import pandas as pd
import messages


def sanitise_dupes(df, column):
    messages.dupes(column)
    return df.drop_duplicates(subset=column, keep='first')


def dropNull(df, columnsArray):
    return df.dropna(subset=columnsArray, how='all')


def nullToUnknown(df, column):
    df[column] = df[column].fillna(value="Unknown")
    return df
