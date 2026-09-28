"""Two adults and a child sit in a boat with a scalloped waterline.

Construction: ship: hull meeting a wavy waterline; person-standing: heads and simplified torso strokes.
Reduction: Shoulder outlines reduced to seated torso strokes; waves integrated into the hull bottom. Adults mirror across the smaller child.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a03f4751-09c4-5145-930a-045651b52849'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__people-in-boat-on-waves/20260927T145836Z-thuan-mac-1/reference/refugee immigration sea boat_a03f4751-09c4-5145-930a-045651b52849.svg'
AUTHOR = 'gpt-6'


class PeopleInBoatOnWaves(Solo48):
    icon_id = 'people-in-boat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
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
        for name,x,y,r,body_y in [('left',11,9,3,20),('child',24,15,3,26),('right',37,9,3,20)]:
         self.add_arc(f'{name}-head-a',(x,y-r),(x,y+r),radius_x=r)
         self.add_arc(f'{name}-head-b',(x,y+r),(x,y-r),radius_x=r)
         self.add_contour(f'{name}-head',f'{name}-head-a',f'{name}-head-b',closed=True)
         self.add_line(f'{name}-body',(x,body_y),(x,30))
        run('gunwale',(10,36),(6,30),(11,30),(12,30),(24,30),(36,30),(37,30),(42,30),(38,36))
        self.add_arc('water-right',(38,36),(24,36),radius_x=7,radius_y=6)
        self.add_arc('water-left',(24,36),(10,36),radius_x=7,radius_y=6)
        self.add_contour('hull',*runs['gunwale'],'water-right','water-left',closed=True)
        for name in ('left','child','right'):
         self.relate('connect',f'{name}-body','hull')
         self.mark_human_figure(name,head=f'{name}-head',torso=f'{name}-body',torso_junction='start')
