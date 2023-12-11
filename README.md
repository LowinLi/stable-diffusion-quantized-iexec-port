# stable-diffusion-quantized

Inferencing the stable-diffusion model on CPU, through a compressed image of only 2.7G, which includes the necessary Python environment and UInt8 quantized onnxruntime model file. The docker image is built in github actions in this repo which is visible to everyone.

## Run and render an image

**1.** Change the -v path of /io/iexec_in/ and /io/iexec_out/ to the loaction on your machine (on vs_code right click copy path)

**2.** make sure it is the correct tag of the image

**3.** Seems you can't pass a sting with spaces as an arg, working on a fix

docker run \
 -v ./iexec_in:/iexec_in \
 -v ./iexec_out:/iexec_out \
 -e IEXEC_IN=/iexec_in \
 -e IEXEC_OUT=/iexec_out \
 lowinli98/stable-diffusion-quantized:port-to-iexec-v0.1 "portrait photo of a asia old warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes, 50mm portrait photography, hard rim lighting photography–beta –ar 2:3 –beta –upbeta –upbeta" 50 512 512
