"""Author fresh local SOLO48 revisions from the saved primitive fix references.

This batch script is kept with the review evidence. Each emitted icon module
stores its own source ID, source path, and author.
"""

from __future__ import annotations

import importlib.util
import inspect
import json
from pathlib import Path
import sys

import cairosvg

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from icon_set.model.icons.solo._base import Solo48
from icon_set.scripts import build_gate

SOURCE_ICON_ID = None  # Multiple source icons are processed below.
SOURCE_PATH = None
AUTHOR = "gpt-6"


def replace_once(source: str, old: str, new: str, icon_id: str) -> str:
    count = source.count(old)
    if count != 1:
        raise ValueError(f"{icon_id}: expected one occurrence, got {count}: {old}")
    return source.replace(old, new, 1)


def revise(icon_id: str, source: str) -> str:
    if icon_id == "hand-pinching-chip":
        source = replace_once(source,
            "self.add_polyline('thumb-arm',(10,27),(26,42))",
            "self.add_arc('thumb-arm',(10,27),(26,42),radius_x=22,sweep=False)", icon_id)
    elif icon_id == "hand-touching-payment-kiosk":
        source = replace_once(source,
            "self.add_line('finger-left',(32,40),(32,28))",
            "self.add_line('finger-left',(30,40),(30,28))", icon_id)
        source = replace_once(source,
            "self.add_arc('finger-tip',(32,28),(40,28),radius_x=4)",
            "self.add_arc('finger-tip',(30,28),(38,28),radius_x=4)", icon_id)
        source = replace_once(source,
            "self.add_line('hand-right',(40,28),(40,44))",
            "self.add_line('hand-right',(38,28),(38,44))", icon_id)
    elif icon_id == "hand-under-automatic-dryer":
        source = replace_once(source,
            "self.add_line('hand-top-3', (24, 28), (30, 25))",
            "self.add_line('hand-top-3', (24, 28), (30, 27))", icon_id)
        source = replace_once(source,
            "self.add_line('hand-top-4', (30, 25), (35, 25))",
            "self.add_line('hand-top-4', (30, 27), (35, 25))", icon_id)
    elif icon_id == "hands-cupping-sphere":
        source = replace_once(source,
            "self.add_polyline(name+'-thumb',point(16,28),point(4,36),point(4,44))",
            "self.add_arc(name+'-thumb-curve',point(16,28),point(4,36),radius_x=16,sweep=side < 0)\n"
            "         self.add_line(name+'-thumb-stem',point(4,36),point(4,44))\n"
            "         self.add_contour(name+'-thumb',name+'-thumb-curve',name+'-thumb-stem')", icon_id)
    elif icon_id == "hands-exchanging-bitcoin":
        source = replace_once(source,
            "self.add_arc(name,(20,y),(20,y+8),radius_x=8,radius_y=4)",
            "self.add_arc(name,(20,y),(20,y+8),radius_x=7,radius_y=4)", icon_id)
    elif icon_id == "hands-holding-clipboard":
        source = replace_once(source,
            "self.add_line('text', (21, 18), (27, 18))",
            "self.add_line('text', (21, 17), (27, 17))\n"
            "        self.add_line('text-lower', (21, 26), (27, 26))", icon_id)
    elif icon_id == "hang-glider-rider":
        source = replace_once(source,
            "self.add_arc('trail',(4,36),(20,34),radius_x=24,radius_y=8,sweep=False)",
            "self.add_arc('trail',(4,36),(20,34),radius_x=20,radius_y=8,sweep=False)", icon_id)
    elif icon_id == "hanging-toilet-paper-roll":
        source = replace_once(source,
            "self.add_contour('core', 'core-top', 'core-bottom', closed=True)",
            "self.add_contour('core', 'core-top', 'core-bottom', closed=True)\n"
            "        self.add_line('perforation', (17, 32), (20, 32))", icon_id)
    elif icon_id == "hatchet":
        source = replace_once(source,
            "self.add_arc('edge',(26,38),(42,22),radius_x=16,sweep=False)",
            "self.add_arc('edge',(26,38),(42,22),radius_x=14,sweep=False)", icon_id)
    elif icon_id == "havana-cathedral":
        source = replace_once(source,
            "self.relate('connect','door','outline')",
            "self.relate('connect','door','outline')\n"
            "        self.add_line('cross-stem',(24,22),(24,28))\n"
            "        self.add_line('cross-bar',(21,25),(27,25))\n"
            "        self.relate('connect','cross-stem','cross-bar')", icon_id)
    elif icon_id == "head-field-of-view-top":
        source = replace_once(source,
            "line('ray-left',(6,6),(12,12))",
            "line('ray-left',(6,6),(13,13))", icon_id)
        source = replace_once(source,
            "line('ray-right',(42,6),(36,12))",
            "line('ray-right',(42,6),(35,13))", icon_id)
    elif icon_id == "head-profiles-with-heart":
        source = replace_once(source,
            "self.add_line('heart-left-tip',(18,23),(24,29))",
            "self.add_line('heart-left-tip',(18,23),(24,30))", icon_id)
        source = replace_once(source,
            "self.add_line('heart-right-tip',(24,29),(30,23))",
            "self.add_line('heart-right-tip',(24,30),(30,23))", icon_id)
    elif icon_id == "head-with-monocle":
        source = replace_once(source,
            "self.add_line(\"cord\",(31,24),(31,32))",
            "self.add_arc(\"cord\",(31,24),(34,32),radius_x=8,sweep=False)", icon_id)
    elif icon_id == "heart-balloon":
        source = replace_once(source,
            "self.add_arc('string-a',(24,30),(22,37),radius_x=10,sweep=False)",
            "self.add_arc('string-a',(24,30),(21,37),radius_x=11,sweep=False)", icon_id)
        source = replace_once(source,
            "self.add_arc('string-b',(22,37),(24,44),radius_x=10)",
            "self.add_arc('string-b',(21,37),(24,44),radius_x=11)", icon_id)
    elif icon_id == "heart-eyes-face":
        source = replace_once(source,
            "self.add_arc(\"smile\",(20,33),(28,33),radius_x=5,sweep=False)",
            "self.add_arc(\"smile\",(18,33),(30,33),radius_x=7,sweep=False)", icon_id)
    elif icon_id == "heavy-rain-cloud":
        source = replace_once(source,
            "self.add_line('rain-0', (14, 35), (9, 40))",
            "self.add_line('rain-0', (15, 34), (9, 40))", icon_id)
        source = replace_once(source,
            "self.add_line('rain-1', (26, 35), (21, 40))",
            "self.add_line('rain-1', (27, 34), (21, 40))", icon_id)
        source = replace_once(source,
            "self.add_line('rain-2', (38, 35), (33, 40))",
            "self.add_line('rain-2', (39, 34), (33, 40))", icon_id)
    elif icon_id == "hex-nut-cluster":
        source = replace_once(source,
            "(('upper',13,12),('lower',13,36),('right',35,24))",
            "(('upper',14,12),('lower',14,36),('right',34,24))", icon_id)
        source = replace_once(source,
            "(x-7,y),(x-3,y-6),(x+3,y-6),(x+7,y),(x+3,y+6),(x-3,y+6)",
            "(x-8,y),(x-4,y-6),(x+4,y-6),(x+8,y),(x+4,y+6),(x-4,y+6)", icon_id)
    elif icon_id == "hierarchy-arched-branches":
        source = replace_once(source,
            "self.add_arc('left-arch',(24,16),(8,32),radius_x=16,sweep=False)",
            "self.add_arc('left-arch',(24,16),(8,32),radius_x=15,sweep=False)", icon_id)
        source = replace_once(source,
            "self.add_arc('right-arch',(24,16),(40,32),radius_x=16)",
            "self.add_arc('right-arch',(24,16),(40,32),radius_x=15)", icon_id)
    elif icon_id == "hierarchy-bracket-list":
        source = replace_once(source, "ys=(16,28,40)", "ys=(14,27,40)", icon_id)
    else:
        raise ValueError(f"No revision planned for {icon_id}")
    return source


def main(manifest_path: Path, *, revise_source: bool = True) -> None:
    for item in json.loads(manifest_path.read_text()):
        module_path = Path(item["module"])
        if revise_source:
            source = revise(item["icon_id"], module_path.read_text())
            module_path.write_text(source)
        spec = importlib.util.spec_from_file_location("redraw_" + item["uuid"].replace("-", "_"), module_path)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        classes = [value for value in vars(module).values() if inspect.isclass(value)
                   and issubclass(value, Solo48) and value is not Solo48 and value.__module__ == module.__name__]
        if len(classes) != 1:
            raise ValueError(f"{item['icon_id']}: {len(classes)} icon classes")
        icon = classes[0]()
        report = icon.validate_icon()
        gate = build_gate.gate(module_path)
        output = Path(item["result_dir"])
        (output / "validation.txt").write_text(report.describe() + "\n\nbuild gate: " + gate["status"] + "\n" + "\n".join(gate["errors"] + gate["warnings"]) + "\n")
        svg = icon.to_svg()
        (output / f"{item['icon_id']}.svg").write_text(svg)
        for theme, ink, background in (("light", "#141413", "#ffffff"), ("dark", "#f5f4ef", "#1c1c19")):
            themed = svg.replace("currentColor", ink)
            for size in (48, 384):
                cairosvg.svg2png(bytestring=themed.encode(), write_to=str(output / f"preview-{theme}-{size}.png"),
                                 output_width=size, output_height=size, background_color=background)
        print(item["icon_id"], report.status, len(report.errors), len(report.warnings), gate["status"], len(gate["errors"]), len(gate["warnings"]))


if __name__ == "__main__":
    main(Path(sys.argv[1]), revise_source="--validate-only" not in sys.argv[2:])
