# Project Title : Building and Deploying a Question Answering System with Hugging Face

## Introduction : 
This README provides an overview of a DistilBERT-based Question & Answering (Q&A) Application developed with Gradio which is Deployed on HuggingFace Spaces after training with customized SQuAD (Stanford Question Answering Dataset) standard dataset. This app is designed to provide interactive answers to user-provided questions based on a specific dataset. It leverages the lightweight DistilBERT "distilbert-base-cased-distilled-squad" model which is previously trained on SQuAD dataset for speed , efficiency and accuracy , suitable for deploying a robust Q&A system with limited computational resources.

## Table of Contents :

1.  Project Structure
2.  Requirements
3.  Dataset Preparation
4.  Customizing the Model
5.  Gradio Interface Customization
6.  How to Run
7.  Application Usage 
8.  Future Improvements
9.  Acknowledgements
10. Contributing
11. License
12. Contact
  


## 1. Project Structure :
##### ├── datasets/
######       └── train_customSquad-v1.1.json # Customized SQuAD dataset file for Train
######       └── validation_customSquad-v1.1.json # Customized SQuAD dataset file for Validation
##### ├── model/
######       └── customTrained_Distilbert_Squad # Trained and finetuned DistilBERT model checkpoint
##### ├── app.py # Main Gradio app script
##### ├── colabNotebook_CasedDisBert_CustomSquad_Train.ipynb # Script to fine-tune DistilBERT on the customized dataset
##### ├── requirements.txt # Required Python packages
##### └── README.md # Project documentation


## 2. Requirements :
##### torch==2.5.1
##### transformers==4.46.1
##### regex==2024.9.11
##### Strings2==0.0.4
##### py3collections==0.1.2
##### gradio==5.4.0


## 3. Dataset Preparation :
The 2 types of datasets are required one for training and another validating. 
an example of single unit of question which is represtented a s asingle row
{
  "data": [
    {
      "id": "<qid>",
      "title": "<Topic Title>",
      "context": "<Passage>",
      "question": "<question?>",
      "answers": {"<answer>": ["<Answer for the Question>"],"<answer_start>": ["<int value of the answer string index>"]}
    },(after this coma a ,similar question unit block follows,..)
        ]
}
This customized dataset using the structure same as SQuAD dataset is been customized with my own contextual topics such as News ,Movies , People 
on training set and Furturistic Technology and Places on Validation set with totsl of 125 rows adding both sets.


## 4. Customizing the Model :
The colabNotebook_CasedDisBert_CustomSquad_Train script  is used to fine-tunes the DistilBERT model"distilbert-base-cased-distilled-squad"  
already trained with Squad Dataset which is said to the best dataset for  Q & A Tasks , as this Dataset is being a supervised with the 
'gold answers' and accurate when it comes to the dataset evaluation , in addition to the original Squad Dataset , This model is finetuned with 
Customized Dataset with the default Training argument parameters. 


## 5. Gradio Interface Customization :
This Gradio Application is ment to Answer the Question from the given Passage and should be able to evaluate the Answer with the 'Exact Match' and 'F1' , 
so there should be a Human answer that is the Gold Answer in which the comparison will happen with the Actual Human Gold Answer and the Predicted Answer 
to calculate the 'F1' Formula and check for "Exact Match' ,'EM'  as well, to enable the Gradio App has 3 inputs 1.context Passage ,2.Question and 
3.Gold Answer and 4 output Text  Fields for 1.Answer ,2.Machiine Answer Vs Human Answer,3.Exact Match score and 4.F1 Score , the Title , Description and 
Article arethe  predefined Templated Text functions to show Title of the project and  Description of the Projectand text about thee Credits of the Developer. In addition to this the Functions for the Q&A Model , EM and F1 functions are included in the Application Script.


## 6. How to Run :
By adding all the files mentioned in the project Structure into the Hugging Face Spaces with the proper requirements as satisfied the application will be 
built and deployed as a webpage for enabling to share the Application Globally.As a result the Deployed Link is as follows.
### App Link :[https://huggingface.co/spaces/harishkumarkotte/QandA_ChatBot_with_AccuracyChecking](https://huggingface.co/spaces/harishkumarkotte/QandA_ChatBot_with_AccuracyChecking)


## 7. Application Usage :
The Application Interface is very simple , with Text Input Field for the 1. Context Passage ,2.Question and 3.Gold Answer where a paragraph or 2 can 
be Typed or Pasted from the External File in to the 'context' Text Field and frame the Question in the 'Question' Text Field and type the possible Answer 
in the 'Gold Answer' Text Field . The four results will be computed namely 'Answer','Machine Answer vs Human Answer','Exact Match' and 'F1' Score.
🎬 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗗𝗲𝗺𝗼 𝗩𝗶𝗱𝗲𝗼: [https://www.youtube.com/watch?v=IpunZ3T092g](https://www.youtube.com/watch?v=IpunZ3T092g)


## 8. Future Improvements :
The further Model training with various datasets can improve the Model's performance and enhance the Application capabilities. In addition even the application 
can be improved with further features like a Speach Bot.


## 9. Acknowledgements :
This project uses DistilBERT from Hugging Face and is inspired by the SQuAD Q&A challenge. Gradio provides the interactive web application framework.


## 10.Contributing :
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.Your Valuable Sugestions are always invited happily.


## 11.License :
This project is under the MIT License.


## 12. Contact :
📧 Email: harishk_kotte@rediffmail.com
🌐 LinkedIn: [https://www.linkedin.com/in/harish-kumar-k-p-67587a262/](https://www.linkedin.com/in/harish-kumar-k-p-67587a262/)
For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.

