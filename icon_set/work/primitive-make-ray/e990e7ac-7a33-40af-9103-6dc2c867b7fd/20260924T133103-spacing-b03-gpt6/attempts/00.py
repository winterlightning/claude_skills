"""Two inward-facing head profiles beneath conflict burst. SQUARE extremes6,6,42,42; mirrored skull radius6 and open necks. Human reference inspected, connected necks preserve source."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e990e7ac-7a33-40af-9103-6dc2c867b7fd'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/people conflict 3_e990e7ac-7a33-40af-9103-6dc2c867b7fd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'people-conflict-3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Mirrored inward profiles with real necks; no detached-head construction.
        for name,sign in [('left',1),('right',-1)]:
            def p(x,y): return (x if sign==1 else 48-x,y)
            self.add_arc(name+'-skull',p(6,26),p(18,26),radius_x=6,sweep=sign==1)
            self.add_polyline(name+'-back',p(6,26),p(8,34),p(6,42))
            self.add_polyline(name+'-face',p(18,26),p(20,32),p(16,32),p(16,38),p(14,42))
            self.relate('connect',name+'-skull',name+'-back')
            self.relate('connect',name+'-skull',name+'-face')
        self.add_polyline('burst',(14,12),(14,8),(20,10),(24,6),(28,10),(34,8),(34,12))
