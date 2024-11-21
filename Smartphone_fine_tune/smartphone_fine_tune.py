import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
client.files.create(
    file=open("content/test.jsonl", "rb"), purpose="fine-tune")

file_list = client.files.list()

for file in file_list.data:
    if (file.filename == "test.jsonl"):
        file_id = file.id


def create_jobs(file_id):
    client.fine_tuning.jobs.create(
        model="gpt-3.5-turbo", training_file=file_id)


def get_status():
    job_list = client.fine_tuning.jobs.list()
    job_id = job_list.data[0].id
    fine_tuned_model = job_list.data[0].fine_tuned_model
    return (job_id, fine_tuned_model)


job_id, model_id = get_status()

if model_id:
    print(model_id)
else:
    print("Fine tuning process not completed")
