"""A small boat faces right with a broad curved hull, an angular raised bow, and a compact cabin topped by a short chimney. Two wavy waterlines pass beneath the hull.

SQUARE visible bounds (4,4)-(44,44); right-facing boat, cabin, chimney and two waterlines. First waterline meets the hull; chimney reduced to a stroke. Lucide ship informed water and hull hierarchy; directional bow retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5ee704a-fe51-550f-977a-8fdb2e527282'
SOURCE_PATH = 'pictographic-primitives/science/ship 1_a5ee704a-fe51-550f-977a-8fdb2e527282.svg'
AUTHOR = 'gpt-6'

class CabinBoatOnWaves(Solo48):
    icon_id = 'cabin-boat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('boat', 'ship', 'cabin', 'hull', 'wave', 'vessel')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_line('deck',(6,20),(14,20));self.add_line('deck-cabin',(14,20),(26,20))
        self.segments('bow-top',(26,20),(30,18),(42,18))
        self.add_arc('bow',(42,18),(30,30),radius_x=12,radius_y=12)
        self.add_arc('water-keel',(30,30),(18,30),radius_x=6,radius_y=2,sweep=False)
        self.add_arc('stern',(18,30),(6,20),radius_x=12,radius_y=10)
        self.add_contour('hull','deck','deck-cabin','bow-top-1','bow-top-2','bow','water-keel','stern',closed=True)
        self.add_polyline('cabin',(14,20),(14,12),(20,12),(26,12),(26,20))
        self.relate('connect','cabin','hull')
        self.add_line('chimney',(20,12),(20,6));self.relate('connect','chimney','cabin')
        self.add_arc('near-wave-left',(6,30),(18,30),radius_x=6,radius_y=2,sweep=False)
        self.add_arc('near-wave-right',(30,30),(42,30),radius_x=6,radius_y=2,sweep=False)
        self.relate('connect','near-wave-left','hull');self.relate('connect','near-wave-right','hull')
        for i,x in enumerate((6,18,30)):
            self.add_arc(f'far-wave-{i}',(x,40),(x+12,40),radius_x=6,radius_y=2,sweep=False)
        self.add_contour('far-wave',*(f'far-wave-{i}' for i in range(3)))
