import re
import json
from .html_format import *
from cuda_fmt import get_config_filename

def format(text):

    fn = get_config_filename('HTML Beautify')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)
    d = json.loads(s)
    return do_html_format(text, d)
