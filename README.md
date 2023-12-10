# stable-diffusion-quantized

Inferencing the stable-diffusion model on CPU, through a compressed image of only 2.7G, which includes the necessary Python environment and UInt8 quantized onnxruntime model file. The docker image is built in github actions in this repo which is visible to everyone.

## Run and render an image

**1.** Change the -v path of /io/iexec_in/ and /io/iexec_out/ to the loaction on your machine (on vs_code right click copy path)

**2.** make sure it is the correct tag of the image

**3.** Seems you can't pass a sting with spaces as an arg, working on a fix

docker run \
 -v /Users/id/Projects/web3diffusion/repos/stable-diffusion-quantized/io/iexec_in:/iexec_in \
 -v /Users/id/Projects/web3diffusion/repos/stable-diffusion-quantized/io/iexec_out:/iexec_out \
 -e IEXEC_IN=/iexec_in \
 -e IEXEC_OUT=/iexec_out \
 lowinli98/stable-diffusion-quantized this_is_a_prompt 50 512 512
