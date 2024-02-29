from lib import *

PROMPTS = [
    'bridge',
    # 'structure',
    # 'mold',
    # 'defect',
    # 'building',
    # 'detail',
    # 'concrete',
    # 'beams',
]

all_img_paths = get_all_images()

model = LangSAM()

with torch.no_grad():
    while True:
        img_path = choice(all_img_paths)
        filename = os.path.basename(img_path)
        base_filename = filename.replace(EXT,'')

        # copying the image:

        img = Image.open(img_path).convert("RGB")

        # resize to half size:
        if RESIZE_FACTOR:
            img = img.resize((img.width//RESIZE_FACTOR, img.height//RESIZE_FACTOR))

        outfolderpath = os.path.join(ROOT_OUTFOLDERPATH,base_filename)
        create_folder(outfolderpath)

        # also copying the image:
        shutil.copy(img_path, outfolderpath)

        for prompt in tqdm(PROMPTS):
            prompt_folderpath = os.path.join(outfolderpath,prompt)
            create_folder(prompt_folderpath)
            
            masks, boxes, phrases, logits = model.predict(img, prompt)

            if logits.tolist():
                # folders for prompt detections:
                binary_masks_folderpath = os.path.join(prompt_folderpath,'binary_masks')
                clipped_detections_folderpath = os.path.join(prompt_folderpath,'clipped_detections')
                highlighted_detections_folderpath = os.path.join(prompt_folderpath,'highlighted_detections')

                create_folderlist([binary_masks_folderpath,clipped_detections_folderpath,highlighted_detections_folderpath])
                
                for i in range (len(logits)):
                    logit = logits[i].tolist()

                    out_img_name = f'{base_filename}_{i}.png'

                    outpath_highlighted = os.path.join(highlighted_detections_folderpath,out_img_name )
                    outpath_binary = os.path.join(binary_masks_folderpath, out_img_name)
                    outpath_clipped = os.path.join(clipped_detections_folderpath, out_img_name)

                    write_detection_img(img, masks[i], (), (), outpath_highlighted)
                    write_detection_img(img, masks[i], (), (), outpath_binary, binary=True)
                    write_detection_img(img, masks[i], (), (), outpath_clipped, clip=True)

                print(f'prompt: {prompt}, logit: {logit}')





