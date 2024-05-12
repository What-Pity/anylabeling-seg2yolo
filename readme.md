# anylabeling-seg2yolo

Deprecation Notice: This tool is no longer maintained. Please use [the `python` version](https://github.com/What-Pity/anylabeling-seg2yolo/tree/main) instead.

This is a tool for converting segmentation masks to YOLO format.

I found it quite convenient to use [X-Anylabeling](https://github.com/CVHub520/X-AnyLabeling) for labeling my segmentation masks, but I needed to convert the labels in json format to Ultralytics-YOLO format for training a YOLOv8 model. So I wrote this tool to automate the process.

## Usage

There is only a `MATLAB` version of the tool, and I will develop a `python` version later.

To use the tool, you need to:
1. Gather all the labels in a folder.
2. Open `anylabeling_seg2YOLO.mlx`  with `MATLAB`.
3. Set variable `root_dir` to the folder containing all the labels.
4. Set the variable `labels` to the list of labels you want to convert. Note that the key-value pairs in labels should match the ones in your `train.yaml` (or whatever it calls, for mine is [`train_config.yaml`](train_config.yaml)).

For example, my `train_config.yaml` has the following labels:
```  yaml
0: pomelo
```

So my `labels` variable should be:

``` matlab
labels=struct("pomelo",0); 
```

5. Run the `anylabeling_seg2YOLO.mlx` file, and it will create a new folder called `yolo_annotation` containing the YOLO format labels.

## Limitations

1. It seems that it didn't work well on `MATLAB 2023b`, but it should work on `MATLAB 2024a`.
2. There is only a `MATLAB` version of the tool, and I will develop a `python` version as soon as possible.