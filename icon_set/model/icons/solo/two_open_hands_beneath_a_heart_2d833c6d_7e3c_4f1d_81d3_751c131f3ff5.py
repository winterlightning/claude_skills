"""Two open hands beneath a heart, with mirrored palms and smooth equal lobes.
Plan: Two open hands beneath a heart, with mirrored palms and smooth equal lobes.
Construction: Lucide heart and hand originals/atoms: circular lobes, smooth shoulders and mirrored palms.
Omissions: Finger creases omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '2d833c6d-7e3c-4f1d-81d3-751c131f3ff5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romance pride lgbt heart protect hand gesture_2d833c6d-7e3c-4f1d-81d3-751c131f3ff5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-open-hands-beneath-a-heart'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('two', 'open', 'hands', 'beneath', 'a', 'heart')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        for side in (-1,1):
         x=lambda a:24+side*a
         path('hand'+str(side),(x(7),42),[('C',(x(18),34),(x(7),38),(x(18),40)),('L',(x(18),24))])
         path('thumb'+str(side),(x(18),34),[('C',(x(10),31),(x(14),34),(x(12),31))]);join('hand'+str(side),'thumb'+str(side))

        path('heart',(24,11),[('A',(14,11),5,5,False),('C',(24,23),(14,16),(20,21)),('C',(34,11),(28,21),(34,16)),('A',(24,11),5,5,False)],True)
