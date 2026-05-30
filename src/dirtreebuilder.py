import os
import logging
import argparse as ap

from dirtree import TreeBuilder, TreeRenderer

_logger = logging.getLogger(__name__)

def parse_args():
    parser = ap.ArgumentParser()

    parser.add_argument("--path", "-p",
        help = "Path of the folder you want to build the tree of. Default is \".\"",
        dest = "path",
        default = "."
    )

    parser.add_argument("--log-level", "-v",
        help = "Log level. Default is \"warning\"",
        default = "warning",
        choices = ["debug", "info", "warning", "error"],
        dest = "log_level"            
    )

    return parser.parse_args()


def main():
    args = parse_args()

    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }

    logging.basicConfig(level=levels[args.log_level])

    path = args.path


    if not os.path.exists(path):
        _logger.error(f"Path {path} does not exist")
        exit(1)

    if not os.path.isdir(path):
        _logger.error(f"{path} is not a folder, cannot build a tree out of it")
        exit(1)

    _logger.debug("Starting building tree")

    builder = TreeBuilder(path)
    tree = builder.build()

    _logger.debug(f"Finished building tree of directory {path}")

    _logger.debug("Start rendering dirtree")

    renderer = TreeRenderer(tree)
    renderer.render()

    _logger.debug("Finished rendering dirtree")


if __name__ == '__main__':
    main()