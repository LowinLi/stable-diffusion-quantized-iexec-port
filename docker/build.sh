#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILDROOT=$DIR/..
 
cd $BUILDROOT
 
CONTAINER="lowinli98/stable-diffusion-quantized"
VERSION=v0.3
 
IMAGE_NAME="${CONTAINER}:${VERSION}"
cmd="docker build -t $IMAGE_NAME -f $DIR/dockerfile $BUILDROOT --build-arg HUGGINGFACE_TOKEN=$1"
echo $cmd
eval $cmd

docker push $IMAGE_NAME