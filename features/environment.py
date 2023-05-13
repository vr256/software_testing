import os
import sys

ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
sys.path.insert(1, ROOT)

from src.api_request import *


def before_feature(context, feature):
    '''Will be called each time a new feature is being tested'''
    context.builder = APIRequestBuilderFactory.get_builder(feature.name)