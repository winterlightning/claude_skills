"""Measure stroke geometry in an isolated combination-engine process."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'vendor/combination'))
from box_combine import bbox, parse_segments
if __name__=='__main__':
    try:
        print(json.dumps({'bounds':bbox(parse_segments(sys.argv[1]))}))
    except Exception:
        print(json.dumps({'error':'No supported stroke geometry. Upload an SVG with stroked paths or shapes.'}))
        sys.exit(1)
