from fastapi import APIRouter
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

router = APIRouter(prefix="/infer", tags=["Inference"])

model_name = "meta-llama/Meta-Llama-3-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

class Prompt(BaseModel):
    text: str

@router.post("/")
def run_inference(prompt: Prompt):
    inputs = tokenizer(prompt.text, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=128)
    return {"response": tokenizer.decode(output[0], skip_special_tokens=True)}
