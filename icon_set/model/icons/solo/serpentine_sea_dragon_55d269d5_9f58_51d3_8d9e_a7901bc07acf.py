'Sea dragon sigil with long swept horn, projecting jaw and coiled body. Smooth neck and tail; intentional directional asymmetry. Bounds (6,6)-(42,42).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: Double neck outline reduced to one smooth S-shaped stroke to keep the coil open at 48px.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '55d269d5-9f58-51d3-8d9e-a7901bc07acf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/43-55d269d5-9f58-51d3-8d9e-a7901bc07acf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'serpentine-sea-dragon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('serpentine', 'sea', 'dragon')

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
        path('dragon',(15,20),[('L',(9,23)),('L',(6,17)),('L',(18,12)),('L',(38,6)),('L',(30,14)),('C',(42,24),(38,16),(42,20)),('C',(12,34),(42,31),(12,25)),('C',(27,42),(12,40),(19,42)),('C',(42,32),(36,42),(42,38))])
