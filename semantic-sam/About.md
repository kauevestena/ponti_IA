# Building:

    docker build --tag 'semantic-sam' .

# Running:

    docker run --name running_semantic_sam -v D:\segmentation_img_data\extras\Bridge:/workspace/data --gpus all -it 'semantic-sam'