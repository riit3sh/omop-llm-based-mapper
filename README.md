# OMOP Clinical Mapper (LLN EDITION)

A local LLM-powered clinical term mapper for OMOP Common Data Model concepts using Mistral-7B. Maps medical terminology to standardized OMOP concept IDs with SNOMED CT, ICD-10, LOINC, and other vocabulary codes.

## Features

- 🏥 **Clinical Term Mapping**: Maps medical terms to standardized OMOP concept IDs
- 🤖 **Local LLM**: Uses Mistral-7B model running locally (no API calls)
- 📊 **Multiple Vocabularies**: Supports SNOMED CT, ICD-10-CM, LOINC, and other medical vocabularies
- 🔒 **Privacy-First**: All processing happens locally, no data sent to external services
- ⚡ **Fast**: Optimized for quick medical term lookups
- 📋 **JSON Output**: Structured output with concept ID, vocabulary code, name, and reasoning

## Installation

### Prerequisites

- Python 3.8+
- At least 8GB RAM (for running Mistral-7B model)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/omop-clinical-mapper.git
cd omop-clinical-mapper
```

2. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download the Mistral-7B model:**
```bash
mkdir models
cd models
# Download from Hugging Face or use provided script
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

## Usage

### Basic Usage

```python
from src.mapping import local_llm_map_clinical_term

# Map a clinical term
result = local_llm_map_clinical_term("chest pain")
print(result)
```

**Output:**
```json
{
  "CONCEPT_ID": "4154790",
  "CODE": "SNOMED",
  "NAME": "Chest pain",
  "REASON": "Direct match for chest pain symptoms in SNOMED CT vocabulary"
}
```

### Example Mappings

```python
# Test various medical terms
terms = ["diabetes", "hypertension", "headache", "pneumonia"]

for term in terms:
    result = local_llm_map_clinical_term(term)
    print(f"{term} -> {result['NAME']} (ID: {result['CONCEPT_ID']})")
```

### Batch Processing

```python
import json
from src.mapping import local_llm_map_clinical_term

def batch_map_terms(terms_list):
    results = []
    for term in terms_list:
        try:
            mapping = local_llm_map_clinical_term(term)
            results.append({"input": term, "mapping": mapping, "status": "success"})
        except Exception as e:
            results.append({"input": term, "error": str(e), "status": "failed"})
    return results

# Example usage
medical_terms = ["heart attack", "broken bone", "high fever", "anxiety"]
batch_results = batch_map_terms(medical_terms)

# Save results
with open("mapping_results.json", "w") as f:
    json.dump(batch_results, f, indent=2)
```

## Project Structure

```
omop-clinical-mapper/
├── src/
│   └── mapping.py          # Main mapping functionality
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf  # LLM model file
├── testing.py              # Test script
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .venv/                 # Virtual environment
```

## Configuration

### Model Parameters

You can adjust the LLM parameters in `src/mapping.py`:

```python
llm = LlamaCpp(
    model_path="path/to/your/model.gguf",
    temperature=0.1,        # Lower = more deterministic
    max_tokens=256,         # Response length limit
    n_ctx=512,             # Context window size
    n_batch=64,            # Batch size for processing
)
```

### Environment Variables

```bash
# Suppress LLAMA verbose logging
export LLAMA_LOG_LEVEL=0
```

## Supported Medical Vocabularies

- **SNOMED CT**: Clinical terminology
- **ICD-10-CM**: Disease classification
- **LOINC**: Laboratory data
- **RxNorm**: Medications
- **CPT4**: Procedures
- **HCPCS**: Healthcare procedures

## Example Output

```json
{
  "CONCEPT_ID": "201826",
  "CODE": "SNOMED",
  "NAME": "Type 2 diabetes mellitus",
  "REASON": "Mapped to SNOMED CT concept for Type 2 diabetes mellitus, the most common form of diabetes"
}
```

## Requirements

Create a `requirements.txt` file:

```txt
langchain-community>=0.0.20
llama-cpp-python>=0.2.0
```

## Performance

- **Model Size**: ~4GB (Q4_K_M quantization)
- **Memory Usage**: ~6-8GB RAM during inference
- **Speed**: ~2-5 seconds per mapping (depending on hardware)
- **Accuracy**: Depends on model training and prompt engineering

## Troubleshooting

### Common Issues

1. **Model Loading Errors**:
   ```bash
   # Ensure model file exists and path is correct
   ls -la models/mistral-7b-instruct-v0.1.Q4_K_M.gguf
   ```

2. **Memory Issues**:
   - Reduce `n_ctx` parameter
   - Use smaller model quantization (Q2_K vs Q4_K_M)

3. **JSON Parsing Errors**:
   - Check model output format
   - Adjust temperature settings
   - Verify prompt formatting

### Debug Mode

Enable debugging in `mapping.py`:

```python
def local_llm_map_clinical_term(term):
    # ... existing code ...
    print(f"DEBUG - Raw output: {result}")  # Add this line
    # ... rest of function ...
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OMOP Common Data Model](https://www.ohdsi.org/data-standardization/the-common-data-model/)
- [Mistral AI](https://mistral.ai/) for the base language model
- [LangChain](https://langchain.com/) for LLM integration
- [llama.cpp](https://github.com/ggerganov/llama.cpp) for efficient model inference

## Disclaimer

This tool is for research and educational purposes. Always validate medical mappings with qualified healthcare professionals before using in production systems.
