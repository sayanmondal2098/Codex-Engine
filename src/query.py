#!/usr/bin/env
import sys
import os
import re
import psutil

import logging

from pathlib import Path
from util import time

def detect_shell():
    global SHELL
    global PROMPT_CONTENT
    parent_process_name = psutil.Process(os.getppid()).name()
    POWERSHELLMODE = bool(re.fullmatch('powershell.*', parent_process_name, re.IGNORECASE))
    BASHMODE = bool(re.fullmatch('bash.*', parent_process_name, re.IGNORECASE)) 
    ZSHMODE = bool(re.fullmatch('zsh.*', parent_process_name, re.IGNORECASE))
    
    SHELL = 'powershell' if POWERSHELLMODE else 'bash' if BASHMODE else 'zsh' if ZSHMODE else "unknown shell"
    #print(SHELL)
    
    shell_prompt = Path(os.path.join(os.path.dirname(__file__), "..", "context", "{}-prompt.txt".format(SHELL)))

    if shell_prompt.is_file():
        PROMPT_CONTENT = shell_prompt

    return SHELL


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.BASIC_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.debug("Starting up")
    logging.debug("Current time: {}".format(time.RequestTimefromNtp()))
    logging.debug("Current shell: {}".format(detect_shell()))
#    logging.debug("Current prompt: {}".format(PROMPT_CONTENT))
    
    print(time.RequestTimefromNtp())
    #detect_shell()