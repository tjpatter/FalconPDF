import os
os.system(f"git lfs install")
os.system(f"pip install torch torchvision torchaudio torchtext torchdata --extra-index-url https://download.pytorch.org/whl/cu118 -U")
os.system(f"pip install bitsandbytes sentencepiece fsspec gradio langchain einops -U")
os.system(f"pip install git+https://github.com/huggingface/transformers.git -U")
# os.system(f"pip install git+https://github.com/huggingface/peft.git -U")
os.system(f"pip install git+https://github.com/huggingface/accelerate.git -U")
os.system(f"cp /home/demo/venv/lib/python3.8/site-packages/bitsandbytes/libbitsandbytes_cuda118.so /home/demo/venv/lib/python3.8/site-packages/bitsandbytes/libbitsandbytes_cpu.so")
os.system(f"python run.py")
os.chdir(f"/home/demo/source")
# os.system(f"pip install -r requirements.txt")
os.system(f"python run.py")