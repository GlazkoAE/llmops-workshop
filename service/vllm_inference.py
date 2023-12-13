from vllm import LLM, SamplingParams

sampling_params = SamplingParams(
    temperature=0.0,
    max_tokens=200,
)

llm = LLM(
    model="TheBloke/deepseek-coder-1.3b-base-AWQ",
    trust_remote_code=True,
    download_dir="data/hf/cache",
    gpu_memory_utilization=0.2,
    max_model_len=1024,
    quantization="awq",
)


def generate(prompt: str):
    outputs = llm.generate(prompt, sampling_params)
    generated_text = outputs[0].outputs[0].text
    return generated_text
