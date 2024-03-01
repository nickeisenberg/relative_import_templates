from sys import path
path.append("/home/local/DEVNET/eisenbergn/Tmp/relimports/method1")
from src.run_exp import run_synth_100m_exp

if __name__ == "__main__":
    x = run_synth_100m_exp()
    print(x)
