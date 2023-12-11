import argparse
import os
from datetime import datetime
import json
import logging
import sys

from diffusers import StableDiffusionOnnxPipeline

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']

def main():
    
    output_dir = iexec_out

    arg_prompt = str(sys.argv[1])
    arg_num_inference_steps = int(sys.argv[2]) #should it be a string or a number?
    arg_height = int(sys.argv[3]) #should it be a string or a number?
    arg_width = int(sys.argv[4]) #should it be a string or a number?
    
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

    
    quant_pipe = StableDiffusionOnnxPipeline.from_pretrained(
        "./onnx", provider="CPUExecutionProvider", local_files_only=True
    )
    image = quant_pipe(**config)["sample"][0]
    os.makedirs(output_dir, exist_ok=True)
    image.save(
        os.path.join(output_dir, "final.png")
    )

    with open(iexec_out + '/computed.json', 'w+') as f:
        json.dump({"deterministic-output-path" : iexec_out + '/final.png'}, f)


if __name__ == "__main__":
    main()
