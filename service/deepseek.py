from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "deepseek-ai/deepseek-coder-1.3b-base",
    trust_remote_code=True,
    cache_dir="data/hf/cache"
)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-coder-1.3b-base",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    cache_dir="data/hf/cache"
).cuda()


def generate(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)[len(prompt):]
