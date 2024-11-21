import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Configure the model ID. Change this to your model ID.
my_llm = "ft:gpt-3.5-turbo-0125:college::AVRgTcit"


def smartphone_test_run(question):

    response = client.chat.completions.create(
        model=my_llm,
        messages=[{"role": "system", "content": "You are a customer support agent for a smartphone company whose primary goal is to help users with issues they are experiencing with their smartphones. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to smartphones."},
                  {"role": "user", "content": question}]
    )
    # Print the generated text
    drug_class = response.choices[0].message.content.strip()  # type: ignore
    # The result should be 0, 1, and 2
    return (drug_class)


demo = gr.Interface(
    fn=smartphone_test_run,
    inputs=["text"],
    outputs=["text"],
)

demo.launch()
