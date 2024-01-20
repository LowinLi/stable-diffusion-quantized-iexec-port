import os
import logging
from onnxruntime.quantization import quantize_dynamic, QuantType


def quant(model_dir):
    for root, dirs, filenames in os.walk(model_dir):
        if "model.onnx" in filenames:
            if "weights.pb" in filenames or "model.onnx_data" in filenames:
                external_data = True
            else:
                external_data = False
            quantize_dynamic(
                model_input=os.path.join(root, "model.onnx"),
                model_output=os.path.join(root, "model.onnx"),  # Quantize and directly overwrite the original onnx file
                per_channel=True,
                reduce_range=True,
                weight_type=QuantType.QUInt8,
                use_external_data_format=external_data
            )
            logging.info("Quantized model saved at: ", os.path.join(root, "model.onnx"))
            for data_file in ["weights.pb", "model.onnx_data"]: # Delete the onnx_data file and the weights.pb file
                if data_file in filenames:
                    os.remove(os.path.join(root, data_file))
                    logging.info("Removed %s" % data_file)
            

if __name__ == "__main__":
    quant()