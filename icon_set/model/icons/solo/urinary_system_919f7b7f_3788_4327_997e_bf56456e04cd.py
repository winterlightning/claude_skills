"""Symmetric kidneys, gently curved ureters and a round bladder.
Plan: Symmetric kidneys, gently curved ureters and a round bladder.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Small internal kidney detail omitted; paired organs and ducts retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '919f7b7f-3788-4327-997e-bf56456e04cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/urinary system_919f7b7f-3788-4327-997e-bf56456e04cd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='urinary-system'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/health'
    aliases=()
    keywords=('urinary', 'system')

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
        for n,side in [('left',-1),('right',1)]:
         x=lambda a:24+side*a
         path(n+'-kidney',(x(11),4),[('C',(x(16),14),(x(15),4),(x(16),9)),('C',(x(11),24),(x(16),19),(x(15),24)),('C',(x(5),18),(x(7),24),(x(3),22)),('C',(x(5),10),(x(7),16),(x(7),12)),('C',(x(11),4),(x(3),6),(x(7),4))],True)
         path(n+'-ureter',(x(5),18),[('L',(x(5),24)),('C',(24,30),(x(5),28),(x(2),30))]);join(n+'-kidney',n+'-ureter')
        circle('bladder',24,36,6)
        for n in ('left','right'):join(n+'-ureter','bladder')
        join('left-ureter','right-ureter');line('outlet',(24,42),(24,44));join('outlet','bladder')
