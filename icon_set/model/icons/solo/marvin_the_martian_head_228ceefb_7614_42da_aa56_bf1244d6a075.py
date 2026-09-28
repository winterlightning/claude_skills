"""A round smiling face wears a domed helmet with a broad curved brim and a tall flat-topped crest. Angular cheek guards hang at either side, framing two tiny vertical eyes and a curved mouth.

SQUARE visible bounds (4,4)-(44,44); domed helmet, flat crest, brim, cheek guards and a small smile. Crest border reduced to cap and stem; eyes omitted to retain a clear face. No useful exact Lucide match. Symmetric construction with exact face/guard junctions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '228ceefb-7614-42da-aa56-bf1244d6a075'
SOURCE_PATH = 'pictographic-primitives/science/marvin the martian_228ceefb-7614-42da-aa56-bf1244d6a075.svg'
AUTHOR = 'gpt-6'

class MarvinTheMartianHead(Solo48):
    icon_id = 'marvin-the-martian-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('marvin', 'martian', 'helmet', 'head', 'cartoon', 'alien')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('dome-left',(6,22),(18,14),radius_x=12,radius_y=8)
        self.segments('dome-top',(18,14),(24,14),(30,14))
        self.add_arc('dome-right',(30,14),(42,22),radius_x=12,radius_y=8)
        self.segments('brim',(42,22),(40,22),(36,22),(12,22),(8,22),(6,22))
        self.add_contour('helmet','dome-left','dome-top-1','dome-top-2','dome-right',*(f'brim-{i}' for i in range(1,6)),closed=True)
        self.add_polyline('crest-cap',(18,6),(24,6),(30,6))
        self.add_line('crest-stem',(24,6),(24,14))
        self.relate('connect','crest-cap','crest-stem');self.relate('connect','crest-stem','helmet')
        self.add_arc('face-right',(36,22),(24,42),radius_x=12,radius_y=20)
        self.add_arc('face-left',(24,42),(12,22),radius_x=12,radius_y=20)
        self.add_contour('face','face-right','face-left')
        self.relate('connect','face','helmet')
        self.add_polyline('guard-left',(8,22),(6,34),(10,42),(24,42))
        self.add_polyline('guard-right',(40,22),(42,34),(38,42),(24,42))
        self.relate('connect','guard-left','helmet');self.relate('connect','guard-right','helmet')
        self.relate('connect','guard-left','face');self.relate('connect','guard-right','face')
        self.add_arc('smile',(22,31),(26,31),radius_x=3,sweep=False)
