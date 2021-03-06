# -*- coding: utf-8 -*-
__author__ = "Likun Liu"

import logging
import logging.config
import json
import os
import sys
import click
import time
import itertools
import pandas as pd
import Const
from Const import datapath

# import CommandModelRisk
import CommandAnalysis

from util import ProgressBar
from util.xdebug import dd
from db import *


logger = logging.getLogger(__name__)

def setup_logging(
    default_path = './shell/logging.json',
    default_level = logging.INFO,
    env_key = 'LOG_CFG'):

    """Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


@click.group(invoke_without_command=True)
@click.pass_context
def roboadvisor(ctx):
    default_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(default_dir, "logging.json")

    setup_logging(default_path=path)

    # pd.set_option('display.height', 1000)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    #config.load()


if __name__=='__main__':
    roboadvisor.add_command(CommandAnalysis.analysis)
    roboadvisor(obj={})
