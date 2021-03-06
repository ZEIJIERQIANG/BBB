# TODO 正确导入函数 generate_matrix, save_matrix, save_fig
from simplelayout.cli import get_options  # TODO: 保证不修改本行也可以正确导入
from simplelayout.generator.core import generate_matrix
from simplelayout.generator.utils import save_matrix, save_fig, make_dir
import sys


def main():
    args = get_options()
    if args.board_grid % args.unit_grid or len(args.positions) != args.unit_n:
        sys.exit("cannot divide exactly.")
    for position in args.positions:
        if position < 1 or position > (args.board_grid / args.unit_grid) ** 2:
            sys.exit("position is beyond boundary.")
    make_dir(args.outdir)
    path = args.outdir + '/' + args.file_name
    matrixa = generate_matrix(
        args.board_grid, args.unit_grid, args.unit_n, args.positions)
    save_matrix(matrixa, path)
    save_fig(matrixa, path)
    return
    raise NotImplementedError  # TODO 使用导入的函数按命令行参数生成数据，包括 mat 文件与 jpg 文件



if __name__ == "__main__":
    main()
