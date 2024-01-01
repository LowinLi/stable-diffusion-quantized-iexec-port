import sys
from inference import infer


if __name__ == "__main__":
    arg_prompt = str(sys.argv[1])
    arg_num_inference_steps = int(sys.argv[2]) #should it be a string or a number?
    arg_height = int(sys.argv[3]) #should it be a string or a number?
    arg_width = int(sys.argv[4]) #should it be a string or a number?
    arg_model_id = sys.argv[5] or "prompthero/openjourney"
    infer(arg_prompt, arg_num_inference_steps, arg_height, arg_width, arg_model_id)
