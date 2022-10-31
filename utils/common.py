import os
import shutil
import hashlib
import pathlib

import pandas as pd

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def post_processing():    
    # hashing each data file
    l = list()
    for filename in os.listdir("submission"):
        l.append({
            "name": filename,
            "sha256": sha256sum(f"submission/{filename}")
        })

    pd.DataFrame(l).to_pickle("submission/fingerprint.pkl")

    # zipping submission/ directory
    shutil.make_archive("submission", "zip", "submission")