"""Hand pinching an acupuncture needle with a rounded raised finger and smooth palm.
Plan: Hand pinching an acupuncture needle with a rounded raised finger and smooth palm.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Finger creases removed; pinching tip and straight needle retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '219024ce-9973-4736-8ba2-b73e81755a00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/acupuncture hand_219024ce-9973-4736-8ba2-b73e81755a00.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-pinching-acupuncture-needle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('hand', 'pinching', 'acupuncture', 'needle')

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
        path('finger',(42,26),[('L',(24,8)),('C',(18,6),(22,6),(20,6)),('A',(14,10),4,4,False),('C',(18,16),(14,12),(16,14)),('L',(26,24)),('C',(19,32),(28,26),(26,32))])
        circle('pin',16,32,3);join('pin','finger')
        path('palm',(16,35),[('C',(30,40),(20,38),(24,40)),('L',(42,40))]);join('palm','pin')
        line('needle',(16,35),(6,42));join('needle','pin');join('needle','palm')
