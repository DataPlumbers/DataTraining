import spacys_mom as spm
from dateparser.search import search_dates


nlp = spm.SpacyWrapper()


class ColumnEntityIdentifier:
    def __init__(self, column):
        self.column = column

    def execute(self):
        # Loop over each value in the column
        col_ents = []
        for value in self.column:
            valstr = str(value)
            # Evaluate each value in spaCy
            # NOTE: a "value" can be anything (number, sentence, etc.)
            doc = nlp.process(valstr)
            val_ents = [e.label_ for e in doc.ents]
            if len(val_ents) != 0:
                # Get most common entity type
                most_common_ent = max(set(val_ents), key=val_ents.count)
                col_ents.append(most_common_ent)
            # TODO: Override Cardinal pretty often...
            try:
                float(valstr)
            except ValueError:
                if search_dates(valstr) != None:
                    col_ents.append("DATE")

        return col_ents
