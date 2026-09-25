"""Electric Shock Hazard.
Symbol plan: Partial person reaches toward jagged overhead wire; head and upper torso share x=18.
Reference construction: human_ref/full_body_ref.png.
SQUARE visible extremes: (4, 4, 44, 44); centerlines inset 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af634b87-e03b-46ea-80c0-7d215f7f1629'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/safety danger electricity_af634b87-e03b-46ea-80c0-7d215f7f1629.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'person-reaching-up-toward-jagged-overhead-wire'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('person', 'electric', 'shock', 'hazard', 'wire', 'hand', 'danger', 'safety')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        poly('wire',(6,6),(36,6),(28,14),(42,14))
        for i,(a,b) in enumerate((((18,20),(21,23)),((21,23),(18,26)),((18,26),(15,23)),((15,23),(18,20)))):arc('head'+str(i),a,b,3)
        contour('head','head0','head1','head2','head3',closed=True)
        line('torso',(18,34),(18,42))
        line('arm-left',(18,34),(6,40))
        line('arm-right',(18,34),(32,34))
        arc('elbow',(32,34),(40,26),8,sweep=False)
        line('forearm',(40,26),(40,24))
        contour('bent-forearm','elbow','forearm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only exact shared-endpoint contacts, not mere proximity.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
