import argparse
import os
from datetime import datetime
import json
import logging

from diffusers import StableDiffusionOnnxPipeline


def main():
    parser = argparse.ArgumentParser(
        description="Runing stable-diffusion by excusing python script"
    )
    parser.add_argument(
        "-p", "--prompt", help="this is a prompt cover config.json", required=False, default=None
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        help="image output dir",
        required=False,
        default="./output",
    )
    args = parser.parse_args()
    prompt = args.prompt
    output_dir = args.output_dir
    with open("./config.json", "r") as f:
        config = json.load(f)
    if prompt:
        config["prompt"] = prompt
    logging.info(
        "generate %s, output png in %s"
        % (json.dumps(config, ensure_ascii=False), output_dir)
    )
    quant_pipe = StableDiffusionOnnxPipeline.from_pretrained(
        "./onnx", provider="CPUExecutionProvider", local_files_only=True
    )
    image = quant_pipe(**config)["sample"][0]
    os.makedirs(output_dir, exist_ok=True)
    image.save(
        os.path.join(output_dir, datetime.now().strftime("%Y%m%dT%H%M%S.%f.png"))
    )


if __name__ == "__main__":
    main()
