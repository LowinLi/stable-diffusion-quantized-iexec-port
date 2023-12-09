# stable-diffusion-quantized


Inferencing the stable-diffusion model on CPU, through a compressed image of only 2.7G, which includes the necessary Python environment and UInt8 quantized onnxruntime model file. The docker image is built in github actions in this repo which is visible to everyone.

---
- [1.Getting Started](#1-getting-started)
- [2.Input prompt](#2-input-prompt)
- [3.Configuation](#3-configuation)

## 1. Getting Started
+ Start Docker service
```bash
docker run -it -v ./volume:/app/output lowinli98/stable-diffusion-quantized:v0.1 bash
```
+ Execute script in Docker service for graphing
```docker
/app/env/bin/python inference.py
```

## 2. Input prompt
+ Enter prompt to execute
```docker
/app/env/bin/python inference.py -p "portrait photo headshot by mucha, sharp focus, elegant, render, octane, detailed, award winning photography, masterpiece, rim lit"
```

## 3. Configuation

+ fix default config.json like this in docker image

```json
{
    "prompt": "portrait photo of a asia old warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes, 50mm portrait photography, hard rim lighting photography–beta –ar 2:3 –beta –upbeta –upbeta",
    "height": 512,
    "width": 512,
    "num_inference_steps": 50,
    "guidance_scale": 7.0,
    "eta": 0.0,
    "seed": 10
}
```
