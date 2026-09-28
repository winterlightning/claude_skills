'Grenade with rounded body, central meridian, horizontal groove and safety ring. Cap and ring share exact nodes. Bounds (8,4)-(40,44).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: Dense segmentation reduced to one meridian and one cross groove.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd7a56ae2-766c-4e0e-9092-08ce21ae1d13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grenade_d7a56ae2-766c-4e0e-9092-08ce21ae1d13.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-hand-grenade-with-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('segmented', 'hand', 'grenade', 'with', 'ring')

    def build(self):

        def path(n,p,steps,closed=False):
            members=[]
            for i,s in enumerate(steps):
                k,q,*a=s; m=f'{n}-{i}'
                if k=='L': self.add_line(m,p,q)
                elif k=='A': self.add_arc(m,p,q,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='C': self.add_bezier(m,p,(a[0],a[1],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        path('body',(20,16),[('A',(32,30),12,14,True),('A',(20,44),12,14,True),('A',(8,30),12,14,True),('A',(20,16),12,14,True)],True)
        poly('cap',(20,16),(12,16),(12,4),(28,4),(28,6),(28,16),closed=True);join('cap','body')
        line('meridian',(20,16),(20,44));join('meridian','body')
        poly('groove',(8,30),(20,30),(32,30));join('groove','body');join('groove','meridian')
        path('ring',(28,6),[('A',(40,18),12,12,True),('A',(32,30),8,12,True)]);join('ring','cap');join('ring','body')
