# About

    This was a test for this specific project with very specific requirements.
    Didn't worked as spected.

## Building

    docker build --tag 'semantic-sam' .

## Running

    docker run --name running_semantic_sam -v D:\segmentation_img_data\extras\Bridge:/workspace/data --gpus all -it 'semantic-sam'