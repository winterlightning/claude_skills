"""A person with three targeting ticks integrated into the head outline. VRECT_L extremes (8,4)-(40,44). Lucide user-round informs circular head and shoulders; scan-face informs orderly focus marks. Retain all three ticks as attached strokes rather than a separate side modifier, with explicit head junctions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77a78a1e-7942-4955-a807-6a094b7b3a35'
SOURCE_PATH = 'pictographic-primitives/symbol/person 1_77a78a1e-7942-4955-a807-6a094b7b3a35.svg'
AUTHOR = 'gpt-6'


class PersonTargetHead(Solo48):
    icon_id = 'person-target-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('target', 'person', 'tracking', 'face-detection', 'focus', 'user', 'aim', 'surveillance')

    def build(self) -> None:
        points=[(24,8),(36,20),(24,32),(12,20)]
        for i,p in enumerate(points):
            self.add_arc(f'head-{i}',p,points[(i+1)%4],radius_x=12)
        self.add_contour('head',*(f'head-{i}' for i in range(4)),closed=True)
        self.add_polyline('tick-top',(24,4),(24,8),(24,12))
        self.add_polyline('tick-left',(8,20),(12,20),(16,20))
        self.add_polyline('tick-right',(32,20),(36,20),(40,20))
        for tick in ['tick-top','tick-left','tick-right']:
            self.relate('connect','head',tick)
        self.add_arc('shoulder-left',(8,44),(24,32),radius_x=16,radius_y=12)
        self.add_arc('shoulder-right',(24,32),(40,44),radius_x=16,radius_y=12)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','head','shoulders')
