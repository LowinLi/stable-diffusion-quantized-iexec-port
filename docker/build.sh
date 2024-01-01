#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILDROOT=$DIR/..
 
cd $BUILDROOT
 
CONTAINER="lowinli98/stable-diffusion-quantized"
VERSION="0.0.4"
 
IMAGE_NAME="${CONTAINER}:${VERSION}"

cmd="docker build -t $IMAGE_NAME -f $DIR/dockerfile $BUILDROOT"
echo $cmd
eval $cmd

# docker push $IMAGE_NAME