"""A side-view alien has a long arched head projecting left above a narrow jaw and curved torso. Its lower body curls into a hooked tail, while two short spines project from the upper-right back.

SQUARE visible bounds (4,4)-(44,44). Side-view alien with an elongated domed skull, curved torso and hooked tail. Narrow jaw detail and short dorsal spines omitted for clearance. No useful exact Lucide Xenomorph match; asymmetric profile and curl retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cce42f7-9a4b-47ca-8564-c6162d026735'
SOURCE_PATH = 'pictographic-primitives/science/xenomorph_4cce42f7-9a4b-47ca-8564-c6162d026735.svg'
AUTHOR = 'gpt-6'

class XenomorphCreature(Solo48):
    icon_id = 'xenomorph-creature'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('xenomorph', 'alien', 'creature', 'head', 'tail', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('skull-top',(6,20),(30,6),radius_x=24,radius_y=14)
        self.add_arc('skull-end',(30,6),(30,14),radius_x=4)
        self.add_arc('skull-under',(30,14),(14,22),radius_x=16,radius_y=8,sweep=False)
        self.add_arc('snout',(14,22),(6,20),radius_x=8,radius_y=2)
        self.add_contour('skull','skull-top','skull-end','skull-under','snout',closed=True)
        self.add_arc('back',(30,14),(42,28),radius_x=12,radius_y=14)
        self.add_arc('tail-outer',(42,28),(28,42),radius_x=14)
        self.add_arc('tail-tip',(28,42),(14,34),radius_x=14,radius_y=8)
        self.add_arc('tail-inner',(14,34),(30,34),radius_x=8,radius_y=3,sweep=False)
        self.segments('torso',(30,34),(30,28),(18,26))
        self.add_contour('body','back','tail-outer','tail-tip','tail-inner','torso-1','torso-2')
        self.relate('connect','body','skull')
