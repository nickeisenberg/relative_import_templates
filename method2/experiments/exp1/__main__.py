import os
root = __file__
root = root.split(os.sep)
root = os.path.join(os.sep, os.path.join(*root[:-3]))
print(root)
from sys import path
path.append(root)

from src.run_exp import run_synth_100m_exp

if __name__ == "__main__":
    x = run_synth_100m_exp()
    print(x)

