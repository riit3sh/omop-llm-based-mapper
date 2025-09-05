from langchain_community.llms import LlamaCpp
import os

# Suppress LLAMA verbose output
os.environ["LLAMA_LOG_LEVEL"] = "0"

llm = LlamaCpp(
    model_path = "/home/rit3sh/Downloads/omop-matcher-mcp/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    temperature=0.1,
    max_tokens=256,
    verbose=False,
    n_ctx=512,
    n_batch=64,
)

def local_llm_map_clinical_term(term):
    prompt = f"""[INST] You are an expert medical terminology mapper specializing in OMOP Common Data Model.

Your task: Map the clinical term '{term}' to its most appropriate OMOP concept.

Instructions:
- Analyze the term '{term}' carefully
- Find the best matching OMOP concept ID (8-digit number)
- Determine the correct vocabulary (SNOMED, ICD10CM, LOINC, etc.)
- Provide the official concept name
- Explain your reasoning

Output format (JSON only):
{{"CONCEPT_ID": "concept_id_here", "CODE": "vocabulary_here", "NAME": "concept_name_here", "REASON": "explanation_here"}}

Now map: {term}[/INST]"""
    result = llm.invoke(prompt)
    print(f"DEBUG - Raw output for '{term}': {result}")
    import json
    try:
        # Try to extract JSON from the response
        response = result.strip()
        # Find the first { and last } to extract just the JSON part
        start = response.find('{')
        end = response.rfind('}') + 1
        if start != -1 and end > start:
            json_str = response[start:end]
            return json.loads(json_str)
        else:
            raise ValueError("No JSON found in response")
    except Exception as e:
        print(f"JSON parsing error: {e}")
        return {"CONCEPT_ID": "", "CODE": "", "NAME": "", "REASON": f"Could not parse LLM output: {result}"}