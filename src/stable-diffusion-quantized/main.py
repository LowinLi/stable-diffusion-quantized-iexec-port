import sys
from inference import infer
import os


if __name__ == "__main__":
    arg_prompt = str(sys.argv[1])
    arg_num_inference_steps = int(sys.argv[2]) #should be number
    arg_height = int(sys.argv[3]) #should be number
    arg_width = int(sys.argv[4]) #should be number
    if len(sys.argv) > 5:
        arg_model_id = sys.argv[5]
    elif os.environ.get("MODEL_ID"):
        arg_model_id = os.environ.get("MODEL_ID")
    else:
        raise ValueError("No model id provided as argument or environment variable")
    infer(arg_prompt, arg_num_inference_steps, arg_height, arg_width, arg_model_id)
