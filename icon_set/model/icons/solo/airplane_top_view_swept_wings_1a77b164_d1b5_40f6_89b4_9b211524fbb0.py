'plane. Nose top-to-wing-root height increases from 6 to 8 units (one to three units of straight neck below the round nose). Upright VRECT_L layout preserves swept wings and paired tail planes; both sides derive from x=24. Wing/tail tips remain angular to meet clearance. Construction reference: local Lucide plane.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1a77b164-d1b5-40f6-89b4-9b211524fbb0'
SOURCE_PATH = 'pictographic-primitives/travel/plane_1a77b164-d1b5-40f6-89b4-9b211524fbb0.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/airplane_top_view_swept_wings_1a77b164_d1b5_40f6_89b4_9b211524fbb0.py'
class Drawing(Solo48):
    icon_id = 'airplane-top-view-swept-wings'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('plane',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        # Mirrored fuselage: three-unit straight nose before swept wings.
        right=[(29,9),(29,12),(40,18),(40,28),(29,22),(29,32),(35,35),(35,44),(24,40)]
        points=right+[(48-x,y) for x,y in reversed(right[:-1])]
        self.path('plane',points[0],[('L',p) for p in points[1:]]+[('A',points[0],5,5,True)],True)

    icon_id = 'airplane-top-view-swept-wings'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('airplane', 'plane', 'aircraft', 'top-view', 'flight', 'aviation', 'airport', 'travel')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
