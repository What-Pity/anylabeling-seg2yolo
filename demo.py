import tqdm
from json2txt import json2txt
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Convert json to txt')
parser.add_argument('--config_path', type=str, required=True,
                    help='path to config file in yaml format')
parser.add_argument('--target_root', type=str, default='./output',
                    help='directory to save output txt files')
parser.add_argument('--json_dir', type=str, required=True,
                    help='path to directory containing json files')
args = parser.parse_args()

config_path = Path(args.config_path)
target_root = Path(args.target_root)
json_dir = Path(args.json_dir)

if not config_path.exists():
    raise FileNotFoundError(f"Config file not found at {str(config_path)}")
if not json_dir.exists():
    raise FileNotFoundError(
        f"Directory containing json files not found at {str(json_dir)}")
if not target_root.exists():
    target_root.mkdir(parents=True)


converter = json2txt(config_path)
for json_file in tqdm.tqdm(Path(json_dir).glob('*.json'), desc='Converting json to txt'):
    converter.read_json(json_file)
    target_path = target_root / (json_file.stem + ".txt")
    if target_path.exists():
        target_path.unlink()
    converter.write_txt(target_path)
