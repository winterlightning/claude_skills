"""Nine-hole pegboard. SQUARE exact centerline bounds6,6,42,42; grid pitch9 and edge margin9. Hole count and arrangement retained."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '5ae49a1e-1226-441e-91e1-428676a4faba'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pegboard_5ae49a1e-1226-441e-91e1-428676a4faba.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pegboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Rounded square and centered 3x3 hole series; solid marks represent small dark holes.
        pts=[(10,6),(38,6),(42,10),(42,38),(38,42),(10,42),(6,38),(6,10)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];name='board-'+str(i);ids.append(name)
            if i%2:self.add_arc(name,a,b,radius_x=4)
            else:self.add_line(name,a,b)
        self.add_contour('board',*ids,closed=True)
        for y in (15,24,33):
            for x in (15,24,33):self.add_dot(f'hole-{x}-{y}',(x,y))
