from lang_sam_importer import *

prompt = 'bridge'

model = LangSAM()

with torch.no_grad():
    for img_path in tqdm(get_all_images()):

        filename = os.path.basename(img_path)
        base_filename = filename.replace(EXT,'')

        # copying the image:

        img = Image.open(img_path).convert("RGB")
        original_image = img
        original_size = (img.width, img.height)

        # resize to half size:
        if RESIZE_FACTOR:
            original_image = img.copy()
            img = img.resize((img.width//RESIZE_FACTOR, img.height//RESIZE_FACTOR))

        outfolderpath = os.path.join(ROOT_OUTFOLDERPATH,base_filename)
        create_folder(outfolderpath)

        # # also copying the image:
        # shutil.copy(img_path, outfolderpath)
       
        masks, boxes, phrases, logits = model.predict(img, prompt)

        if logits.tolist():
            # find index of the highest logit:
            max_index = logits.tolist().index(max(logits.tolist()))

            sel_mask = masks[max_index]

            if RESIZE_FACTOR:
                sel_mask = sel_mask.to('cpu').numpy()
                sel_mask = sel_mask * 255
                sel_mask = cv2.resize(sel_mask, original_size, interpolation=cv2.INTER_NEAREST)
                sel_mask = torch.from_numpy(sel_mask.astype(bool)).to(DEVICE)


            outpath_clipped = os.path.join(outfolderpath, filename)

            write_detection_img(original_image, sel_mask, (), (), outpath_clipped, clip=True)

        # writing metadata:
        metadata = {
            'original_path': img_path,
            'filename' : filename,
            'prompt': prompt,
            'original_size': original_size,
        }

        metadata_path = os.path.join(outfolderpath, 'metadata.json')
        dump_json(metadata, metadata_path)




