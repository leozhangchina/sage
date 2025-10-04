<<<<<<< HEAD
import argparse
import json
import os
from argparse import ArgumentParser
from yacs.config import CfgNode as CN


def get_args():
    parser = ArgumentParser(description='Train Motion Capture Network')
    parser.add_argument('--cfg',
                        help='experiment configure file name',
                        default="",
                        type=str)
    args = parser.parse_args()
    return args


def merge_file(args):
    print(f"using config {args.cfg}")
    cfg = CN(new_allowed=True)
    cfg.merge_from_file(args.cfg)
    return cfg
=======
import argparse
import json
import os
from argparse import ArgumentParser
from yacs.config import CfgNode as CN


def get_args():
    parser = ArgumentParser(description='Train Motion Capture Network')
    parser.add_argument('--cfg',
                        help='experiment configure file name',
                        default="",
                        type=str)
    args = parser.parse_args()
    return args


def merge_file(args):
    print(f"using config {args.cfg}")
    cfg = CN(new_allowed=True)
    cfg.merge_from_file(args.cfg)
    return cfg
>>>>>>> 47a06f625edd4e367bc70dca13fbfab77a077565
