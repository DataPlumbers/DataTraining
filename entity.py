# Reference: https://spacy.io/usage/linguistic-features
import pandas as pd
import entity_columns as ec
from dateparser.search import search_dates


def get_entities_file(filepath):
    # Get CSV file as a Data Frame (df)
    df = pd.read_csv(filepath, delimiter=',', encoding='utf-8-sig')
    # print(df)
    # Iterate over each column in Data Frame
    ent_dict = {}
    for column in df:
        ent = get_entities_col(df[column])
        ent_dict[column] = ent
    return ent_dict


def get_entities_col(column):
    identifier = ec.ColumnEntityIdentifier(column)
    col_ents = identifier.execute()

    # Wrap results in panda DataFrame so that we can operate on it
    df = pd.DataFrame(col_ents)

    # Hacky fix for cases when there isn't an entity associated with a header
    # We can do something more elegant here...
    try:
        res = df.mode()[0][0]
        return res
    except KeyError:
        pass
