# ponti

A repo for experimenting on photos of bridges using AI.

## Running the docker image

first, buid:

    docker build --tag 'ponti_ia' .

then run (on Windows use PowerShell): 

    docker run --name running_ponti -v D:\segmentation_img_data\extras\Bridge:/workspace/data --gpus all -it 'ponti_ia' 

replace "D:\segmentation_img_data\extras\Bridge" with the desired path for mounting a volume where the input data must be put and the outputs will be generated. If you want to run more than one running container, you can remove "--name running_deep_pavements".

include "--detach" to run in background and "--rm" to remove on exit

### Using VSCode for edit as developer container:

 Click on the "><" blue button at the corner (or call commands with ctrl+shift+P), select "(Dev Containers:) Attach to Running Container", select "Open Folder" and "Ponti IA", and have fun from outside of dependency hell!

#### Monitoring GPU usage:

execute gpustat:

    gpustat -cp --watch

or for different intervals, 3 seconds in the example:

    watch -n 3 -c gpustat -cp --color