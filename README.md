# stable-diffusion-quantized

Inferencing the stable-diffusion model on CPU, through a compressed image of only 2.7G, which includes the necessary Python environment and UInt8 quantized onnxruntime model file. The docker image is built in github actions in this repo which is visible to everyone.

## Run and render an image

**1.** Change the -v path of /io/iexec_in/ and /io/iexec_out/ to the loaction on your machine (on vs_code right click copy path)

**2.** make sure it is the correct tag of the image

**3.** Run the model image directly
+ choose the correct model image in released assets, or build by `docker/build.sh` in this repo.
    + `lowinli98/stable-diffusion-quantized:0.0.5-stabilityai-stable-diffusion-2-1`
    + `lowinli98/stable-diffusion-quantized:0.0.5-stabilityai-stable-diffusion-2`
    + `lowinli98/stable-diffusion-quantized:0.0.5-runwayml-stable-diffusion-v1-5`
    + `lowinli98/stable-diffusion-quantized:0.0.5-CompVis-stable-diffusion-v1-4`
    + `lowinli98/stable-diffusion-quantized:0.0.5-prompthero-openjourney`
+ download docker image, and load by "docker load -i *.tar", may be need `docker tag it`.

    ```bash
    docker run \
    -v ./iexec_in:/iexec_in \
    -v ./iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    lowinli98/stable-diffusion-quantized:0.0.5-prompthero-openjourney "portrait photo of a asia old warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes, 50mm portrait photography, hard rim lighting photography–beta –ar 2:3 –beta –upbeta –upbeta" 50 512 512
    ```
#### Run the other image and quantized in realtime

+ input the any huggingface stable-diffusion model_id in the last arg like "prompthero/openjourney". container will cache and render the quantized onnx model by the docker volume `-v ./onnx_model` whick is no need to download and quantize the same model in twice time.

```bash
docker run \
 -v ./iexec_in:/iexec_in \
 -v ./iexec_out:/iexec_out \
 -v ./onnx_model:/app/model/onnx_model \
 -e IEXEC_IN=/iexec_in \
 -e IEXEC_OUT=/iexec_out \
 lowinli98/stable-diffusion-quantized:0.0.5 "portrait photo of a asia old warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes, 50mm portrait photography, hard rim lighting photography–beta –ar 2:3 –beta –upbeta –upbeta" 50 512 512 prompthero/openjourney
```


## the docker images:
1. base image: `lowinli98/stable-diffusion-quantized:0.0.5` build by dockerfile
2. model image build by dockerfile-with-model-quantized:
    + `lowinli98/stable-diffusion-quantized:0.0.5-stabilityai-stable-diffusion-2-1`
    + `lowinli98/stable-diffusion-quantized:0.0.5-stabilityai-stable-diffusion-2`
    + `lowinli98/stable-diffusion-quantized:0.0.5-runwayml-stable-diffusion-v1-5`
    + `lowinli98/stable-diffusion-quantized:0.0.5-CompVis-stable-diffusion-v1-4`
    + `lowinli98/stable-diffusion-quantized:0.0.5-prompthero-openjourney`

+ run build.sh can build all of these images above.

## the working step
1. How to set up the dev environment (python libraries to install etc..)

    + the dev environment is build in the image which can be found in [dockerfile](./docker/dockerfile)

2. steps to download the huggingface model && steps to transfer it to onnx && steps to quantise

    + download and quantize any stable-diffusion image during build docker image 
        + In `docker/build.sh` script, firstly build the base image which prepared python environment and python scripts. Secondly, based on the image, continue to build model image by downloading and quantizing the stable-diffusion model by input the model_id in `docker/build.sh` script.

    + download and quantize any stable-diffusion image by args in render realtime
        + When we run the docker image with a new stable-diffusion model_id in huggingface which is cannot found in cache dir. Firstly, the model will be download and transfer to onnx formate in the [source code](./src/stable-diffusion-quantized/prepare/download_onnx.py). Secondly, the model will be quantized in QUInt8 in the [source code](./src/stable-diffusion-quantized/prepare/quantization.py). Thirdly, the quantized model will be saved in cache directory, which is mounted on the host machine locally. So, if running the same model for the second time, there is no need to download and quantize it again, you can directly start the inference.
