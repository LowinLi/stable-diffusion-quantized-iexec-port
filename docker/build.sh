#!/bin/bash
set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILDROOT=$DIR/..
 
cd $BUILDROOT
 
CONTAINER="lowinli98/stable-diffusion-quantized"
VERSION="0.0.5"
 
BASE_IMAGE_NAME="${CONTAINER}:${VERSION}"

cmd="docker build -t $BASE_IMAGE_NAME -f $DIR/dockerfile $BUILDROOT"
echo $cmd
eval $cmd

OPEN_MIDJOUNEY_IMAGE_NAME="${CONTAINER}:open-midjourney-${VERSION}"


MODEL_IDS=("prompthero/openjourney" "CompVis/stable-diffusion-v1-4" "runwayml/stable-diffusion-v1-5" "stabilityai/stable-diffusion-2" "stabilityai/stable-diffusion-2-1")
for MODEL_ID in "${MODEL_IDS[@]}"
do
    TAG=${VERSION}-"${MODEL_ID//\//-}"
    IMAGE_NAME_WITH_MODEL="${CONTAINER}:${TAG}"
    echo "Building... ${IMAGE_NAME_WITH_MODEL}"
    docker build -t $IMAGE_NAME_WITH_MODEL \
        -f $DIR/dockerfile-with-model-quantized \
        --build-arg MODEL_ID=${MODEL_ID} \
        --build-arg BASE_IMAGE=${BASE_IMAGE_NAME} \
        $BUILDROOT
    echo "Finished $name"
done