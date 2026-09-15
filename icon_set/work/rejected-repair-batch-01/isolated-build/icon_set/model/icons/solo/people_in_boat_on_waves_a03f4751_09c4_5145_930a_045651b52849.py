"""Two adults and a child sit in a boat with a scalloped waterline.

Construction: ship: hull meeting a wavy waterline; person-standing: heads and simplified torso strokes.
Reduction: Shoulder outlines reduced to seated torso strokes; waves integrated into the hull bottom. Adults mirror across the smaller child.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a03f4751-09c4-5145-930a-045651b52849'
SOURCE_PATH = 'pictographic-primitives/travel/refugee immigration sea boat_a03f4751-09c4-5145-930a-045651b52849.svg'
AUTHOR = 'gpt-6'


class PeopleInBoatOnWaves(Solo48):
    icon_id = 'people-in-boat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('refugee', 'immigration', 'boat', 'sea', 'family', 'people', 'waves', 'migration')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); circular child head uses the approved diameter4.
        for name,x,y,r,body_y in [('left',12,9,3,21),('child',24,15,2,26),('right',36,9,3,21)]:
         self.add_arc(f'{name}-head-a',(x,y-r),(x,y+r),radius_x=r)
         self.add_arc(f'{name}-head-b',(x,y+r),(x,y-r),radius_x=r)
         self.add_contour(f'{name}-head',f'{name}-head-a',f'{name}-head-b',closed=True)
         self.add_line(f'{name}-body',(x,body_y),(x,30))
        run('gunwale',(10,36),(6,30),(12,30),(24,30),(36,30),(42,30),(38,36))
        self.add_arc('water-right',(38,36),(24,36),radius_x=7,radius_y=6)
        self.add_arc('water-left',(24,36),(10,36),radius_x=7,radius_y=6)
        self.add_contour('hull',*runs['gunwale'],'water-right','water-left',closed=True)
        for name in ('left','child','right'):self.relate('connect',f'{name}-body','hull')
