from constants import *
import os, glob, shutil, json
from random import choice
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',filemode='w',filename='global_log.log')

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

for folderpath in [ROOT_OUTFOLDERPATH]:
    create_folder(folderpath)

def get_all_images(rootpath=ROOTPATH_INPUT):
    return glob.glob(os.path.join(rootpath,'**','*'+EXT),recursive=True)


def create_folderlist(folderlist):
    for folderpath in folderlist:
        create_folder(folderpath)

def dump_json(json_obj, outpath):
    with open(outpath, 'w', encoding='utf-8') as outfile:
        json.dump(json_obj, outfile, indent=4, ensure_ascii=False)