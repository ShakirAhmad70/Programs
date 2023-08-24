import difflib
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk
nltk.download('punkt')

def summarize_sentence(sentence):
    parser = PlaintextParser.from_string(sentence, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count=1)
    return str(summary[0])

# Example usage
user_sentence = input("Enter a message to summarize")
summary = summarize_sentence(user_sentence)
print("Summary:", summary)



def generate_tone(user_input):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    result = classifier(user_input)[0]
    return result["label"]

# Example usage
user_input = input("Write a messege: ")
tone = generate_tone(user_input)
print("Generated tone:", tone)



# Sample conversation history
conversation = [
    "Hello, how are you?",
    "I'm doing great! How about you?"
]

def suggest_words(user_input, conversation):
    all_words = ' '.join(conversation).lower().split()
    suggestions = difflib.get_close_matches(user_input.lower(), all_words)
    return suggestions

# Example usage
user_input = input("Enter a message: ")
suggested_words = suggest_words(user_input, conversation)
print("Suggested words:", suggested_words)
