import pytest
from ai_engine import generate_responses

def test_generate_responses():
    query = "Explain blockchain"
    casual, formal = generate_responses(query)
    assert isinstance(casual, str) and len(casual) > 0
    assert isinstance(formal, str) and len(formal) > 0
    # Optionally test for presence of expected keywords
    assert "blockchain" in casual.lower()
    assert "blockchain" in formal.lower()
