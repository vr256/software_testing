import os
import sys

ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
sys.path.insert(1, ROOT)

from behave import given, when, then
from src.api_request import *

