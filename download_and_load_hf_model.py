from dotenv import load_dotenv
load_dotenv()

import os
os.environ["HF_TOKEN"] = os.getenv("hf")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("hf")

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tok = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct")

# Model saved locally on your system at above mension path
tok.save_pretrained(r"D:\Innomatics Research lab\Agentic AI automation internship-Oct 2025\Langchain\HuggingFaceHub\deepseekmodel\Deep\deepseekmodeldow")
model.save_pretrained(r"D:\Innomatics Research lab\Agentic AI automation internship-Oct 2025\Langchain\HuggingFaceHub\deepseekmodel\Deep\deepseekmodeldow")

tok = AutoTokenizer.from_pretrained("D:\Innomatics Research lab\Agentic AI automation internship-Oct 2025\Langchain\HuggingFaceHub\deepseekmodel\Deep\deepseekmodeldow")
model = AutoModelForCausalLM.from_pretrained("D:\Innomatics Research lab\Agentic AI automation internship-Oct 2025\Langchain\HuggingFaceHub\deepseekmodel\Deep\deepseekmodeldow")
