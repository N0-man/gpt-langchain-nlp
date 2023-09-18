from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from constants import *

vectorIndex = VectorStoreIndexWrapper(vectorstore=myCassandraVStore)

print('Welcome to motivational hotline')
while True:
    query_text = input("\nEnter your problem (or type 'quit' to exit): ")
    if query_text.lower() == "quit":
        break

    print("QUESTION: \"%s\"" % query_text)
    # https://python.langchain.com/docs/get_started/quickstart#llms
    # There are two types of language models, which in LangChain are called
    answer_llm = vectorIndex.query(query_text, llm=llm).strip()
    answer_chat_model = vectorIndex.query(query_text, chat_model).strip()

    print("\n Response LLM: \"%s\"" % answer_llm)
    print("\n Response CHAT MODEL: \"%s\"\n" % answer_chat_model)

    print("Phrases BY RELEVANCE [similarity score]:")
    for doc, score in myCassandraVStore.similarity_search_with_score(query_text, k=4):
        print("  [ %0.4f] \"%s\"" % (score, doc.page_content))

