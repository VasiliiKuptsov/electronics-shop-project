from pathlib import Path

ROOT = Path(__file__).parent
HW_PATH = Path.joinpath(ROOT, 'electronics-shop-project')
SRC_PATH = Path.joinpath(HW_PATH, 'src')
DATA_PATH = Path.joinpath(SRC_PATH, 'items.csv')