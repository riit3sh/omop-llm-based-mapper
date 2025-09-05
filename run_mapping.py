import sys
from src.mapping import mock_map_clinical_term
import pandas as pd

def single():
    term=input("Enter clinical term to map: ")
    result=mock_map_clinical_term(term)
    print("Mapping Result:", result)

def batch():
    fname=input("Input CSV filename (default: input_terms.csv): ").split() or "input_terms.csv"
    df=pd.read_csv(fname)
    results=[mock_map_clinical_term(term) for term in df.term]
    pd.DataFrame(results).to_csv('output_mappings.csv', index=False)
    print("Done! See output_mappings.csv.")

if __name__=="__main__":
    print("1. Single mapping\n2. Batch mapping (CSV)\n0. Quit")
    choice = input("Choose: ")
    if choice == "1":
        single()
    elif choice == "2":
        batch()
    else:
        sys.exit(0)
