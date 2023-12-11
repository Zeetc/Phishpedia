from phishpedia.phishpedia_main import test
import matplotlib.pyplot as plt
from phishpedia.phishpedia_config import load_config

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