import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Configure the model ID. Change this to your model ID.
drug_fine_tune_llm = 'ft:gpt-3.5-turbo-0125:college::AVWObtTY'

# Let's use a drug from each class
drugs = [
    "A CN Gel(Topical) 20gmA CN Soap 75gm",  # Class 0
    "Addnok Tablet 20'S",                    # Class 1
    "ABICET M Tablet 10's",                  # Class 2
]


def test_run(drug_name):
    # Returns a drug class for each drug
    prompt = "Drug: {}\nMalady:".format(drug_name)

    response = client.chat.completions.create(
        model=drug_fine_tune_llm,
        messages=[{"role": "system", "content": "You are a medical assistant specializing in drug and malady classification. You help classify drugs and match them with possible ailments."},
                  {"role": "user", "content": prompt}],
    )
    # Print the generated text
    drug_class = response.choices[0].message.content.strip()  # type: ignore
    # The result should be 0, 1, and 2
    return (drug_class)


demo = gr.Interface(
    fn=test_run,
    inputs=["text"],
    outputs=["text"],
)

demo.launch()
