"""An angled whistle sounds toward a dog profile at lower right.
SQUARE (6,6)-(42,42). Source identifies dog, not the older thumbs-down label.
Whistle owns a smooth chamber and mouthpiece; sound rays are spaced above dog.
Dog is a companion in a training scene, not a reusable state badge. Lucide dog
and whistle were inspected for contour simplification and round chamber flow.
Omit whistle hole, eye and third sound ray to preserve clear negative space.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID="4fc4ae7d-865e-46ed-a947-3bffc16d3c51"
SOURCE_PATH="pictographic-primitives/_uncategorized_15/dog whistle 1_4fc4ae7d-865e-46ed-a947-3bffc16d3c51.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id="whistle-sounding-beside-dog-profile"
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=("Dog Whistle",)
    keywords=("whistle","dog","sound","training","pet","muzzle","signal")
    def build(self):
        self.add_bezier("chamber",(10,12),((6,16),(6,18),(6,20)),((6,25),(10,28),(14,28)),((19,28),(22,25),(22,21)),((22,21),(21,21),(20,20)))
        pts=[(20,20),(28,14),(24,6),(10,12)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])): self.add_line(f"mouth-{i}",a,b)
        self.add_contour("whistle","chamber","mouth-0","mouth-1","mouth-2",closed=True)
        self.add_line("ray-top",(36,6),(40,6))
        self.add_line("ray-right",(38,16),(42,16))
        self.add_bezier("dog-muzzle",(38,26),((35,30),(28,29),(28,34)),((28,36),(30,36),(32,36)))
        pts=[(32,36),(32,42),(42,42),(42,36),(38,26)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])): self.add_line(f"dog-outline-{i}",a,b)
        self.add_contour("dog","dog-muzzle",*[f"dog-outline-{i}" for i in range(4)],closed=True)
