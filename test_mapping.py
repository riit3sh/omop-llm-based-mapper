from src.mapping import mock_map_clinical_term

def test_mock():
    term="Blood Pressure"
    result=mock_map_clinical_term(term)
    assert result["CONCEPT_ID"]=="12345"
    assert  "Blood Pressure" in result["REASON"]
    print("Test passed.")

if __name__ == "__main__":
    test_mock()