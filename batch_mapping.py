import pandas as pd

from src.mapping import mock_map_clinical_term

df=pd.read_csv('input_terms.csv')  
results = []
for term in df.term:
    results.append(mock_map_clinical_term(term))
pd.DataFrame(results).to_csv('output_mapping.csv', index=False)
print("Done! See output_mappings.csv.")