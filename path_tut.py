from pathlib import Path
from time import strftime

print(Path(__file__).resolve().parent /
      "W4" / strftime("run_%Y_%m_%d_%H_%M_%S"))
