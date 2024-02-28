from lang_sam_importer import *
import os, glob, shutil
from random import choice
from tqdm import tqdm
import logging
import cv2

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',filemode='w',filename='global_log.log')

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

for folderpath in [ROOT_OUTFOLDERPATH]:
    create_folder(folderpath)

def get_all_images():
    return glob.glob(os.path.join(ROOTPATH,'**','*'+EXT),recursive=True)


def create_folderlist(folderlist):
    for folderpath in folderlist:
        create_folder(folderpath)