## /docker/Dockerfile LINE 28:

The docker image should have an entry point, when we call the docker image it needs to imidiatly call the inference.py and initiate rendereing. On Iexec you do not have control while the docker image is running. You call it whith your args, it executes, dumps everything to iexec_out and that's it. The inference script should stop when finished so IExec knows the results are finished.

## /src/stable-diffusion-quantized/model/inference

### Line 14

The output is constant in iexec and it is retrieved using os.environ['IEXEC_OUT']

### Line 15-24

There is no prompt on iexec. You call it with what are here system args. You can have many system args and the way yuo distinguesh beteen is the order.

    sys.argv[1] can be the prompt
    sys.argv[2] can be the inference step
    sys.argv[3] can be the hight of the image
    sys.argv[4] can be the width of the image

### Line 39-40

The way Iexec works is you can have your app executed by multiple workers at the same time. This is for apps that need result intergity, not for us. Because you can't trust one worker, he can be malicios, you run the app at once on +3 workers and iexec compares the final file, if all workers retrieve the same result it means there wasn't malicios activity. This is not for us as the images are not crucial, and even if we want we can't because Machine Learning models often use randoms and it is not deteremiistic. So running it on 3 computers will yield different results.

# How should you run it.

docker run \
 -v /Users/id/Documents/projects/stable-diffusion-quantized/io/iexec_in:/iexec_in \
 -v /Users/id/Documents/projects/stable-diffusion-quantized/io/iexec_out:/iexec_out \
 -e IEXEC_IN=/iexec_in \
 -e IEXEC_OUT=/iexec_out \
 lowinli98/stable-diffusion-quantized arg1 arg2 arg3 arg4
