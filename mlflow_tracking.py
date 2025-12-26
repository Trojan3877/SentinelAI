import mlflow

mlflow.set_experiment("AegisAI-Inference")

def log_inference(prompt, response):
    with mlflow.start_run():
        mlflow.log_param("prompt", prompt)
        mlflow.log_text(response, "response.txt")
