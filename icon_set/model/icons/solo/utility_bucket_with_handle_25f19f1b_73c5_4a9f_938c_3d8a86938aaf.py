'Symmetric utility pail with elliptical opening, straight tapered sides, smooth base and semicircular bail handle. Bounds (8,4)-(40,44).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: None'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25f19f1b-73c5-4a9f-938c-3d8a86938aaf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/11-25f19f1b-73c5-4a9f-938c-3d8a86938aaf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'utility-bucket-with-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives-generate", "other")
    aliases = ()
    keywords = ('utility', 'bucket', 'with', 'handle')

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
        path('rim',(8,24),[('A',(40,24),16,5,True),('A',(8,24),16,5,True)],True)
        path('pail',(8,24),[('L',(12,40)),('C',(24,44),(13,44),(18,44)),('C',(36,40),(30,44),(35,44)),('L',(40,24))]);join('pail','rim')
        path('handle',(8,24),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,24))]);join('handle','rim')
