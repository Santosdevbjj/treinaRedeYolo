#!/usr/bin/env python3
"""
Converte LabelMe JSONs -> arquivos .txt no formato YOLO
Uso:
  python labelme_to_yolo.py --json_dir ../data/labelme_json --out_labels_dir ../data/labels --classes ../data/classes.txt
"""
import os, json, argparse
import numpy as np

def bbox_from_points(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    return xmin, ymin, xmax, ymax

def convert(json_path, classes):
    with open(json_path, 'r', encoding='utf-8') as f:
        j = json.load(f)
    h = j.get('imageHeight')
    w = j.get('imageWidth')
    shapes = j.get('shapes', [])
    lines = []
    for s in shapes:
        label = s.get('label')
        if label not in classes: 
            # opcional: pular ou adicionar à lista
            continue
        cls_id = classes.index(label)
        pts = s.get('points')
        xmin, ymin, xmax, ymax = bbox_from_points(pts)
        x_center = (xmin + xmax) / 2.0 / w
        y_center = (ymin + ymax) / 2.0 / h
        width = (xmax - xmin) / w
        height = (ymax - ymin) / h
        lines.append(f"{cls_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    return lines

def main(args):
    with open(args.classes, 'r', encoding='utf-8') as f:
        classes = [l.strip() for l in f.readlines() if l.strip()]
    os.makedirs(args.out_labels_dir, exist_ok=True)
    for fname in os.listdir(args.json_dir):
        if not fname.lower().endswith('.json'):
            continue
        json_path = os.path.join(args.json_dir, fname)
        lines = convert(json_path, classes)
        if not lines:
            continue
        # assume image name equal (ex: img01.jpg -> img01.json)
        base = os.path.splitext(fname)[0]
        out_txt = os.path.join(args.out_labels_dir, base + '.txt')
        with open(out_txt, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines) + ("\n" if lines else ""))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--json_dir', required=True)
    p.add_argument('--out_labels_dir', required=True)
    p.add_argument('--classes', required=True)
    args = p.parse_args()
    main(args)
