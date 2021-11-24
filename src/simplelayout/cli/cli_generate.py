import argparse


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", nargs='+', type=int)
    parser.add_argument("-o", "--outdir", type=str)
    parser.add_argument("--file_name", type=str)
    args = parser.parse_args()
    return args
