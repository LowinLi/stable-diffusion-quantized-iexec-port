import os
from datetime import datetime
import json
import logging
import sys

from optimum.onnxruntime import ORTStableDiffusionPipeline

from prepare.download_onnx import download_save
from prepare.quantization import quant

iexec_out = os.environ.get('IEXEC_OUT', './iexec_out')
iexec_in = os.environ.get('IEXEC_IN', './iexec_in')
model_path_root = os.environ.get('MODEL_PATH_ROOT', './model')


def infer(arg_prompt, arg_num_inference_steps, arg_height, arg_width, arg_model_id):
    
    output_dir = iexec_out
    model_dir = os.path.join(model_path_root, arg_model_id)
    
    if not os.path.exists(model_dir):
        model_dir = download_save(arg_model_id)
        quant(model_dir)

    with open("./config.json", "r") as f:
        config = json.load(f)
    if arg_prompt:
        config["prompt"] = arg_prompt
    if arg_num_inference_steps:
        config["num_inference_steps"] = arg_num_inference_steps
    if arg_height:
        config["height"] = arg_height
    if arg_width:
        config["width"] = arg_width


    quant_pipe = ORTStableDiffusionPipeline.from_pretrained(model_dir)
    image = quant_pipe(**config).images[0]
    os.makedirs(output_dir, exist_ok=True)
    image.save(
        os.path.join(output_dir, "final.png")
    )

    with open(iexec_out + '/computed.json', 'w+') as f:
        json.dump({"deterministic-output-path" : iexec_out + '/final.png'}, f)
