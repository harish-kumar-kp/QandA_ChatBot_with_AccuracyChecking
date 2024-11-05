import gradio as gr
from transformers import pipeline , AutoTokenizer ,AutoModelForQuestionAnswering
import string
import re
from collections import Counter
# Path to your custom-trained model
model_path = "model/customTrained_Distilbert_Squad"

# Load the tokenizer and model
bert_model = AutoModelForQuestionAnswering.from_pretrained(model_path)
bert_tokenizer = AutoTokenizer.from_pretrained(model_path)
                                              
qa_pipeline = pipeline('question-answering', model=model_path,tokenizer=model_path)
                                               
# Function to normalize answers (remove articles, punctuation, etc.)
def normalize_answer(s):
    """Lowercase, remove punctuation, articles, and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punctuation(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punctuation(lower(s))))

# Exact Match calculation
def exact_match_score(prediction, ground_truth):
    return normalize_answer(prediction) == normalize_answer(ground_truth)

def f1_score(prediction, ground_truth):
    pred_tokens = normalize_answer(prediction).split()
    truth_tokens = normalize_answer(ground_truth).split()

    common_tokens = Counter(pred_tokens) & Counter(truth_tokens)
    num_common = sum(common_tokens.values())

    if num_common == 0:
        return 0.0

    precision = num_common / len(pred_tokens)
    recall = num_common / len(truth_tokens)

    f1 = 2 * (precision * recall) / (precision + recall)
    return f1

def EM_ScoreF1(context,question,goldAnswer=""):
  # Perform question-answering
  predicted_result = qa_pipeline({
      'question': question,
      'context': context
  })
  # Ground truth (the correct answer)
  if goldAnswer=="":
    ground_truth = "Answer Unavailable"
  else:
    ground_truth = goldAnswer

  # Get the predicted answer
  predicted_answer = predicted_result['answer']
  # Compute Exact Match and F1 Score
  em_score = exact_match_score(predicted_answer, ground_truth)
  f1 = f1_score(predicted_answer, ground_truth)
  return(f"Machine Answer: {predicted_result['answer']}"+" Vs 'Human Answer':"+ground_truth), (f"Exact Match: {em_score}"), (f"F1 Score: {f1}")
def EM_ScoreF1(context,question,goldAnswer=""):
  # Perform question-answering
  predicted_result = qa_pipeline({
      'question': question,
      'context': context
  })
  # Ground truth (the correct answer)
  if goldAnswer=="":
    ground_truth = "Answer Unavailable"
  else:
    ground_truth = goldAnswer
  # Get the predicted answer
  predicted_answer = predicted_result['answer']
  # Compute Exact Match and F1 Score
  em_score = exact_match_score(predicted_answer, ground_truth)
  f1 = f1_score(predicted_answer, ground_truth)
  return(f"'Answer': {predicted_result['answer']}"),(f"'Machine Answer': {predicted_result['answer']}"+"   Vs  'Human Answer':"+ground_truth), (f"Exact Match: {em_score}"), (f"F1 Score: {f1}")

demo = gr.Interface(
    fn=EM_ScoreF1,
    inputs=["text", "text","text"],
    outputs=["text","text","text","text"],
    
    title="Question and Answering Chat Bot with Hugging Faces Pretrained Model",
    description="Using Distil Bert Cased Pretrained Model with Squad Dataset and Finetuned with Customized Dataset in Squad Format.",
    article="A Project by Harish Kumar K P , email: harishk_kotte@rediffmail.com \n Note : Here Gold Answer Should be Choosen by Humans"
)

demo.launch()
