from ai_engine import generate_responses

def test():
    query = "What is artificial intelligence?"
    casual, formal = generate_responses(query)

    print("\n🟢 Casual Response:\n", casual)
    print("\n🔵 Formal Response:\n", formal)

if __name__ == "__main__":
    test()
