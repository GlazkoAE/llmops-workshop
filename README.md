# AI Talent Camp 2023: LLMOps - Ускоряем инференс

## Что делали
1. Написали сервис для генерации кода на FastAPI с LLM DeepSeek Coder.
2. Написали клиент для тестирования скорости работы модели, который посылает N асинхронных запросов на сервис и фиксирует RPS (requests per second).
3. Замерили скорость работы DeepSeek Coder (1.3b и 6.7b) из коробки.
4. Ускориили инференс модели с помощью vLLM.
5. Использовали квантованные веса модели (AWQ).

## Ответы на вопросы
Q: Какие еще есть инструменты для ускорения LLM?\
A: OpenLLM, Infery-LLM, Databricks LLM Serving, DeepSpeed

Q: Какие есть инструменты для версионирования промптов?\
A: PromptFlow (Microsoft), Galileo, GenAIOps (Nvidia), PromptWatch.io

## Референсы
DeepSeek Coder: https://github.com/deepseek-ai/DeepSeek-Coder \
vLLM: https://github.com/vllm-project/vllm \
Квантованные веса для DeepSeek Coder: https://huggingface.co/TheBloke/deepseek-coder-1.3b-base-AWQ \
Как добавить свою модель (не из списка поддерживаемых) в vLLM: https://docs.vllm.ai/en/latest/models/adding_model.html
