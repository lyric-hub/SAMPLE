from config_loader import CONFIG
from transformers import AutoTokenizer, AutoModel

model_name = CONFIG['model']['name']
TOKENIZER = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
MODEL=model.eval()