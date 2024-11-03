import streamlit as st
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

#/model/customTrained_Distilbert_Squad
#modelName='model/customTrained_Distilbert_Squad'
modelName='distilbert-base-cased-distilled-squad'
# Load pre-trained model and tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(modelName)  # Update with your model path
tokenizer = AutoTokenizer.from_pretrained(modelName)

# Function to predict answer from question
def predict_answer(question,passage):
    inputs = tokenizer.encode_plus(question, passage, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    # Get the model's outputs (start and end logits)
    outputs = model(**inputs)
    start_scores = outputs.start_logits
    end_scores = outputs.end_logits

    # Get the most likely start and end tokens
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores) + 1

    # Decode the tokens into the answer string
    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(input_ids[start_index:end_index])
    )
    return answer

# Streamlit app interface
st.title("DistilBERT Question Answering System")
passage = st.text_area("Topic Context for Questions' ",height=180)
st.write("Ask a question and get an answer based on a pre-trained model!")

# Input question
question = st.text_input("Enter your question:")

# Display predicted answer when question is asked
if st.button("Get Answer"):
    if question:
        answer = predict_answer(question,passage)
        st.write(f"**Answer**: {answer}")
    else:
        st.write("Please enter a question.")
