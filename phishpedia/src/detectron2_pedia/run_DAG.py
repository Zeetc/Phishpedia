import argparse

from detectron2.config import get_cfg
from detectron2 import model_zoo
from phishpedia.src.detectron2_pedia.detectron2_1.adv import DAGAttacker
from phishpedia.src.detectron2_pedia.detectron2_1.datasets import BenignMapper
# import newly registered backbone
from phishpedia.src.detectron2_pedia.detectron2_1.register_backbone import *


def main(args):
    print("Preparing config file...")
    cfg = get_cfg()
    cfg.merge_from_file(args.cfg_path)
    cfg.MODEL.WEIGHTS = args.weights_path
    cfg.MODEL.BACKBONE.NAME = 'build_resnet_fpn_backbone_quantize'
    print(cfg)
    print("Initializing attacker...")
    # Using custom DatasetMapper
    attacker = DAGAttacker(cfg, mapper=BenignMapper)

    print("Start the attack...")
    coco_instances_results = attacker.run_DAG(
        results_save_path=args.results_save_path, vis_save_dir=args.vis_save_dir
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cfg-path",
        required=True,
        help="Path to configuration file used to train the model",
    )
    parser.add_argument("--weights-path", required=True,
                        help="Path to model weights")
    parser.add_argument(
        "--results-save-path",
        required=True,
        help="Path to save the prediction results as a JSON file",
    )
    parser.add_argument(
        "--vis-save-dir",
        help="Directory to save visualized bbox prediction images",
    )

    args = parser.parse_args()

    main(args)
