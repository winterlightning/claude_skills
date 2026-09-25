"""A tall oval alien head narrows sharply toward a rounded chin. Two upright leaf-shaped eyes lean outward beneath the domed forehead, with no visible nose or mouth.

VRECT_XL visible extremes (6,2)-(42,46); taller crown and narrow jaw. Leaf eyes reduced to outward-leaning strokes to keep face open. No useful Lucide alien match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ca0e155-12d6-555a-9068-ed2edc108abc'
SOURCE_PATH = 'pictographic-primitives/science/alien_5ca0e155-12d6-555a-9068-ed2edc108abc.svg'
AUTHOR = 'gpt-6'

class LongAlienHead(Solo48):
    icon_id = 'long-alien-head'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('alien', 'head', 'oval', 'extraterrestrial', 'eyes', 'face')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('crown',(8,22),(40,22),radius_x=16,radius_y=18)
        self.add_arc('jaw-right',(40,22),(24,44),radius_x=30)
        self.add_arc('jaw-left',(24,44),(8,22),radius_x=30)
        self.add_contour('head','crown','jaw-right','jaw-left',closed=True)
        for side in (-1,1):
            self.add_line(f'eye-{side}',(24+side*7,21),(24+side*4,28))
