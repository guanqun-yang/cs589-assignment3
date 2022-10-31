import os
import shutil
import hashlib
import pathlib

save_path = pathlib.Path("submission")

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
    for filename in os.listdir(save_path):
        l.append({
            "name": filename,
            "sha256": sha256sum(save_path / filename)
        })

    pd.DataFrame(l).to_pickle(save_path / "fingerprint.pkl")

    # zipping submission/ directory
    shutil.make_archive("submission", "zip", save_path)