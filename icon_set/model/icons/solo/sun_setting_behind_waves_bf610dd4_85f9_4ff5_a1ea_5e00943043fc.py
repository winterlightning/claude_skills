'Sun setting over three horizontal water waves. All waves share one smooth cubic pattern and a 10-unit vertical step. Bounds (4,8)-(44,40).\nConstruction: No useful exact Lucide match; shared geometric construction.\nOmissions: None; wave amplitude kept shallow for spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf610dd4-85f9-4ff5-a1ea-5e00943043fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fen_bf610dd4-85f9-4ff5-a1ea-5e00943043fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-setting-behind-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('sun', 'setting', 'behind', 'waves')

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
        for i,y in enumerate((20,30,40)):
         path(f'wave-{i}',(4,y),[('C',(14,y-2),(8,y),(8,y-2)),('C',(24,y),(20,y-2),(20,y)),('C',(34,y-2),(28,y),(28,y-2)),('C',(44,y),(40,y-2),(40,y))])
        path('sun',(14,18),[('A',(24,8),10,10,True),('A',(34,18),10,10,True)]);join('sun','wave-0')
