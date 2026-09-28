"""A squat slug-like alien has a tall rounded head merging into a broad body and a tail curling upward on the left. Small bent arms flank the belly beneath narrowed eyes and a downturned mouth.

HRECT_XL visible bounds (2,6)-(46,42); tall head, broad slug belly and curled left tail. Arms and eye detail reduced to keep the silhouette open. No useful Lucide Hutt match; naturally asymmetric tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d9dbd78-bcd2-586d-9f37-3e76d77e8447'
SOURCE_PATH = 'pictographic-primitives/science/hutt_8d9dbd78-bcd2-586d-9f37-3e76d77e8447.svg'
AUTHOR = 'gpt-6'

class HuttCreature(Solo48):
    icon_id = 'hutt-creature'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('hutt', 'alien', 'slug', 'creature', 'tail', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('head',(20,24),(40,24),radius_x=10,radius_y=16)
        self.add_arc('back',(40,24),(44,32),radius_x=4,radius_y=8)
        self.add_arc('belly-corner',(44,32),(36,40),radius_x=8)
        self.add_line('belly',(36,40),(12,40))
        self.add_arc('tail-bottom',(12,40),(4,32),radius_x=8)
        self.add_line('tail-tip',(4,32),(4,28))
        self.add_arc('tail-curl',(4,28),(20,24),radius_x=9,sweep=False)
        self.add_contour('body','head','back','belly-corner','belly','tail-bottom','tail-tip','tail-curl',closed=True)
        self.add_line('eyes',(29,19),(31,19))
        self.add_line('mouth',(29,27),(31,27))
