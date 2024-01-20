import logging
import sys
import os

from optimum.onnxruntime import ORTStableDiffusionPipeline

def download_save(model_id):
    """huggingface model_id like prompthero/openjourney"""

    model_path_root = os.environ.get('MODEL_PATH_ROOT', './model')
    model_dir = os.path.join(model_path_root, model_id)
    pipeline = ORTStableDiffusionPipeline.from_pretrained(model_id, export=True)
    pipeline.save_pretrained(model_dir)
    logging.info("Saved %s to %s" % (model_id, model_dir))
    return model_dir