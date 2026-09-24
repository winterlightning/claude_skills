"""Permafrost: six-arm snowflake in a tall rounded frame. VRECT_L centerlines8,4,40,44; nine-unit border gaps. Tall shape separates the true branch nodes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3f77b04c-ad63-443d-a816-599e467435a6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'permafrost'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.VRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        # Rounded tall frame and centered six-arm snowflake, mirrored about x24 and y24.
        pts=[(12,4),(36,4),(40,8),(40,40),(36,44),(12,44),(8,40),(8,8)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];name='frame-'+str(i);ids.append(name)
            if i%2:self.add_arc(name,a,b,radius_x=4)
            else:self.add_line(name,a,b)
        self.add_contour('frame',*ids,closed=True)
        # All six spokes share center; vertical branches attach at explicit nodes.
        self.add_polyline('vertical',(24,13),(24,15),(24,24),(24,33),(24,35))
        for name,end in [('ne',(31,21)),('se',(31,27)),('sw',(17,27)),('nw',(17,21))]:
            self.add_line(name,(24,24),end)
            self.relate('connect',name,'vertical')
        self.add_polyline('top-fork',(20,13),(24,15),(28,13))
        self.add_polyline('bottom-fork',(20,35),(24,33),(28,35))
        self.relate('connect','top-fork','vertical')
        self.relate('connect','bottom-fork','vertical')
