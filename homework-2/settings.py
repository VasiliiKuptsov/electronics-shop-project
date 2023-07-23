from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_FATH = Path.joinpath(ROOT, 'src')
DATA_PATH = Path.joinpath(SRC_FATH, 'items.csv')