from __future__ import print_function
# import
## batteries
import os
import sys
import argparse
import logging
## application
from DeepMAsED import Predict

# functions
def get_desc():
    desc = 'Predict values'
    return desc

def parse_args(test_args=None, subparsers=None):
    desc = get_desc()
    epi = """DESCRIPTION:
    Predicting misassemblies by used a model generated by `DeepMAsED train`.

    All feature tables must be labeled either "features.tsv" or "features.tsv.gz"
    (or "features.pkl" if already processed).
    """
    if subparsers:
        parser = subparsers.add_parser('predict', description=desc, epilog=epi,
                                       formatter_class=argparse.RawTextHelpFormatter)
    else:
        parser = argparse.ArgumentParser(description=desc, epilog=epi,
                                         formatter_class=argparse.RawTextHelpFormatter)

    # args
    parser.add_argument('data_path', metavar='data-path', type=str, 
                        help='Where to find feature table(s) (base directory for all tables)')
    parser.add_argument('--model-path',  default='.', type=str, 
                        help='Directory contining the model (default: %(default)s)')
    parser.add_argument('--model-name', default='deepmased_all-asmbl_model.h5', type=str, 
                        help='Model name in the model_path (default: %(default)s)')
    parser.add_argument('--mstd-name', default='deepmased_all-asmbl_mean_std.pkl', type=str, 
                        help='Data mean and std name in the model_path (default: %(default)s)') 
    parser.add_argument('--save-path', default='.', type=str, 
                        help='Directory where to save output (default: %(default)s)')
    parser.add_argument('--save-name', default='deepmased', type=str, 
                        help='Prefix for name in the save_path (default: %(default)s)')        
    parser.add_argument('--cpu-only', action='store_true', default=False,
                        help='Only use CPUs, and no GPUs (default: %(default)s)')
    parser.add_argument('--force-overwrite', action='store_true', default=False,
                        help='Force re-creation of pickle files (default: %(default)s)')
    
    # test args
    if test_args:
        args = parser.parse_args(test_args)
        return args

    return parser

def main(args=None):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    # Input
    if args is None:
        args = parse_args()
    # Main interface
    Predict.main(args)
    
# main
if __name__ == '__main__':
    pass


