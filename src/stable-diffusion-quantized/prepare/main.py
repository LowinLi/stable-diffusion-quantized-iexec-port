import sys
from download_onnx import download_save
from quantization import quant


if __name__ == "__main__":
    """
    example:
    python main.py prompthero/openjourney
    """
    model_id = str(sys.argv[1])

    model_dir = download_save(model_id)
    quant(model_dir)
