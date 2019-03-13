# Driver for ML component of MarkLogic Classifier.
import sys
import classifier as cfr

# Params: ontology = stuff passed by frontend
#         filepaths = list of filepaths to CSV files
# Returns: The classification metadata
# TODO: More clearly specify what metadata to return
def classify(ontology, filepaths):
    # Verify parameters
    if len(filepaths) == 0 or len(ontology) != 2:
        print_usage()
    my_classifier = cfr.Classifier(filepaths)
    results_json = my_classifier.classify_ontology(ontology)
    return results_json


# Print correct usage of application.
def print_usage():
    print("""Classification module requires two parameters:
             1) The given ontology as a JSON object.
                Ex: ("myCategory", ["val1", "val2"])
             2) One or more CSV filepaths.
                Ex: ["file1.csv", "file2.csv"]""")
