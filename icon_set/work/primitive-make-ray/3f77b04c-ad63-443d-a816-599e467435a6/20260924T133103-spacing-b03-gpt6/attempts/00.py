"""Permafrost: six-arm snowflake in rounded square. SQUARE bounds6,6,42,42. Snowflake extrema15..33 leave9-unit border gaps; shared true branch nodes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3f77b04c-ad63-443d-a816-599e467435a6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'permafrost'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Rounded square and centered 3x3 hole series; solid marks represent small dark holes.
        pts=[(10,6),(38,6),(42,10),(42,38),(38,42),(10,42),(6,38),(6,10)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];name='frame-'+str(i);ids.append(name)
            if i%2:self.add_arc(name,a,b,radius_x=4)
            else:self.add_line(name,a,b)
        self.add_contour('frame',*ids,closed=True)
        # All six spokes share center; vertical branches attach at explicit nodes.
        self.add_polyline('vertical',(24,15),(24,19),(24,24),(24,29),(24,33))
        for name,end in [('ne',(33,19)),('se',(33,29)),('sw',(15,29)),('nw',(15,19))]:
            self.add_line(name,(24,24),end)
            self.relate('connect',name,'vertical')
        self.add_polyline('top-fork',(20,15),(24,19),(28,15))
        self.add_polyline('bottom-fork',(20,33),(24,29),(28,33))
        self.relate('connect','top-fork','vertical')
        self.relate('connect','bottom-fork','vertical')
