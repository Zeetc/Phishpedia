from phishpedia.phishpedia_main import test
import matplotlib.pyplot as plt
import torch

# 设置 PyTorch 在 CPU 模式下运行
torch.set_default_tensor_type(torch.FloatTensor)

# Global configuration
from phishpedia.src.siamese import *
from phishpedia.src.detectron2_pedia.inference import *
import phishpedia
import subprocess
from typing import Union
import yaml


def load_config(cfg_path: Union[str, None]):

    if cfg_path is None:
        with open(os.path.join(os.path.dirname(__file__), 'configs.yaml')) as file:
            configs = yaml.load(file, Loader=yaml.FullLoader)
    else:
        with open(cfg_path) as file:
            configs = yaml.load(file, Loader=yaml.FullLoader)

    ELE_CFG_PATH = "phishpedia" + configs['ELE_MODEL']['CFG_PATH'].replace('/', os.sep)
    ELE_WEIGHTS_PATH = "phishpedia" + configs['ELE_MODEL']['WEIGHTS_PATH'].replace('/', os.sep)
    ELE_CONFIG_THRE = configs['ELE_MODEL']['DETECT_THRE']
    ELE_MODEL = config_rcnn(ELE_CFG_PATH, ELE_WEIGHTS_PATH, conf_threshold=ELE_CONFIG_THRE)

    # siamese model
    SIAMESE_THRE = configs['SIAMESE_MODEL']['MATCH_THRE']

    print('Load protected logo list')
    # targetlist_zip_path = "phishpedia" + configs['SIAMESE_MODEL']['TARGETLIST_PATH']
    targetlist_zip_path = "/home/runner/work/Phishpedia/Phishpedia/phishpedia/src/detectron2_pedia/output/rcnn_2/phishpedia/src/siamese_pedia/expand_targetlist.zip"
    targetlist_dir = os.path.dirname(targetlist_zip_path)
    zip_file_name = os.path.basename(targetlist_zip_path)
    targetlist_folder = zip_file_name.split('.zip')[0]
    full_targetlist_folder_dir = os.path.join(targetlist_dir, targetlist_folder)

    if targetlist_zip_path.endswith('.zip') and not os.path.isdir(full_targetlist_folder_dir.replace('/', os.sep)):
        os.makedirs(full_targetlist_folder_dir, exist_ok=True)
        subprocess.run(f'unzip -o "{targetlist_zip_path}" -d "{full_targetlist_folder_dir}"', shell=True)

    weights_path = "phishpedia" + configs['SIAMESE_MODEL']['WEIGHTS_PATH'].replace('/', os.sep)
    weights_path = "/home/runner/work/Phishpedia/Phishpedia/phishpedia/src/detectron2_pedia/output/rcnn_2/phishpedia/src/siamese_pedia/resnetv2_rgb_new.pth.tar"
    SIAMESE_MODEL, LOGO_FEATS, LOGO_FILES = phishpedia_config(
                                                num_classes=configs['SIAMESE_MODEL']['NUM_CLASSES'],
                                                weights_path=weights_path,
                                                targetlist_path=full_targetlist_folder_dir.replace('/', os.sep))
    print('Finish loading protected logo list')

    # DOMAIN_MAP_PATH = "phishpedia" + configs['SIAMESE_MODEL']['DOMAIN_MAP_PATH'].replace('/', os.sep)
    DOMAIN_MAP_PATH = "/home/runner/work/Phishpedia/Phishpedia/phishpedia/src/detectron2_pedia/output/rcnn_2/phishpedia/src/siamese_pedia/domain_map.pkl"
    return ELE_MODEL, SIAMESE_THRE, SIAMESE_MODEL, LOGO_FEATS, LOGO_FILES, DOMAIN_MAP_PATH







url = open("phishpedia/datasets/test_sites/accounts.g.cdcde.com/info.txt").read().strip()
screenshot_path = "phishpedia/datasets/test_sites/accounts.g.cdcde.com/shot.png"
ELE_MODEL, SIAMESE_THRE, SIAMESE_MODEL, LOGO_FEATS, LOGO_FILES, DOMAIN_MAP_PATH = load_config(None)

phish_category, pred_target, plotvis, siamese_conf, pred_boxes = test(url=url, screenshot_path=screenshot_path,
                                                                       ELE_MODEL=ELE_MODEL,
                                                                       SIAMESE_THRE=SIAMESE_THRE,
                                                                       SIAMESE_MODEL=SIAMESE_MODEL,
                                                                       LOGO_FEATS=LOGO_FEATS,
                                                                       LOGO_FILES=LOGO_FILES,
                                                                       DOMAIN_MAP_PATH=DOMAIN_MAP_PATH
                                                                      )

print('Phishing (1) or Benign (0) ?', phish_category)
print('What is its targeted brand if it is a phishing ?', pred_target)
print('What is the siamese matching confidence ?', siamese_conf)
print('Where is the predicted logo (in [x_min, y_min, x_max, y_max])?', pred_boxes)
plt.imshow(plotvis[:, :, ::-1])
plt.title("Predicted screenshot with annotations")
plt.show()
