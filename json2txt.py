from pathlib import Path
import json
from ruamel.yaml import YAML
import numpy as np


class json2txt:
    def __init__(self, config_path):
        """
        initialize the class with config file and txt output directory
        :param config_path: path to the config file, should be a pathlib.Path object
        """
        yaml = YAML()
        with open(str(config_path), 'r', encoding='utf-8') as file:
            config = yaml.load(file)
        self.labels = {v: k for k, v in config["names"].items()}

    def read_json(self, json_path):
        with open(str(json_path), 'r', encoding='utf-8') as file:
            data = json.load(file)
        h = data["imageHeight"]
        w = data["imageWidth"]
        self.shapes = [(shape["label"], np.array(shape["points"])/np.array([w, h]))
                       for shape in data["shapes"]]

    def write_txt(self, target_path):
        for label, points in self.shapes:
            temp = points.reshape((1, -1))
            try:
                with open(str(target_path), 'a', encoding='utf-8') as file:
                    file.write(str(self.labels[label]) + ' ')
                    np.savetxt(file, temp, fmt='%f', delimiter=' ')
            except FileNotFoundError:
                with open(str(target_path), 'w', encoding='utf-8') as file:
                    np.savetxt(file, temp, fmt='%f', delimiter=' ')
