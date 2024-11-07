from preprocessing import preprocess_text, clean_text

from summarization import generate_summary, summarize_sentences



def main():

    # Example long text

    long_text = """

    Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. 

    The ultimate objective of NLP is to enable computers to understand, interpret, and generate human language in a valuable way. 

    NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models. 

    The field has grown significantly in recent years, driven by the increasing availability of data and advances in machine learning algorithms. 

    Applications of NLP include sentiment analysis, language translation, chatbots, and information extraction, among others.

    """



    # Clean and preprocess the text

    cleaned_text = clean_text(long_text)

    sentences = preprocess_text(cleaned_text)



    print("Original Text:")

    print(long_text)

    

    # Generate summary

    summary = summarize_sentences(sentences, ratio=0.3)

    print("\nGenerated Summary:")

    print(summary)



if __name__ == "__main__":

    main()



