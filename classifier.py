import headers as hdr
import json 

class Classifier:
    # Params: data_filepaths = paths to 1+ CSV files
    def __init__(self, data_filepaths):
        self.data_filepaths = data_filepaths

    # Params: ontology = JSON object passing 
    # Returns: classification metadata
    def classify_ontology(self, ontology):
        # Once I deconstruct the JSON object (the ontology) I get passed, 
        # I will use that for comparison. For now just compare based on
        # similarity between headers. 
        results = []
        for filepath in self.data_filepaths:
            results.append(hdr.find_similar(ontology, filepath))
        results_json = json.dumps(results)
        return results_json
