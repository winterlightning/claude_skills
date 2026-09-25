"""Eel with raised tail.
Plan: VRECT_L gives the opposing S bends more vertical room; centerlines (8,4)-(40,44).
Design changes: Reoriented the broad eel into a taller S ribbon and shortened the crowded return at the tail. No defining feature omitted.
References: Lucide worm original and atomic-debug: coherent opposing curves with a broad ribbon. Deliberately asymmetric animal silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f644d4c1-b881-4092-96b4-a643877d65a5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/eel_f644d4c1-b881-4092-96b4-a643877d65a5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'eel-with-narrow-raised-tail'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('eel','fish','tail')
    def build(self):
        self.add_bezier('body',(12,8),((14,8),(18,4),(22,4)),((30,4),(36,8),(36,16)),((36,20),(28,23),(28,30)),((28,34),(30,34),(32,32)),((36,32),(38,30),(40,30)),((40,40),(34,44),(28,44)),((16,44),(12,38),(12,30)),((12,24),(18,22),(18,18)),((18,14),(16,16),(14,16)),((13,16),(13,16),(12,16)))
        self.add_arc('snout',(12,16),(12,8),radius_x=4)
        self.add_contour('eel','body','snout',closed=True)