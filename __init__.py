import os
import json
import cudatext
from .jsoncomment import JsonComment
from .html_format import *
from cuda_fmt import get_config_filename

def format(text):
    fn = get_config_filename('HTML Beautify')
    with open(fn) as f:
        parser = JsonComment(json)
        d = parser.loads(f.read())
    return do_html_format(text, d)
