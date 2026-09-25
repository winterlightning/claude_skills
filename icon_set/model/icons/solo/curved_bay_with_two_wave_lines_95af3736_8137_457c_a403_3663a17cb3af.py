"""Curved bay enclosing two smooth water waves.
Plan: Curved bay enclosing two smooth water waves.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Wave lengths reduced to keep required shoreline clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '95af3736-8137-457c-a403-3663a17cb3af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bay_95af3736-8137-457c-a403-3663a17cb3af.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='curved-bay-with-two-wave-lines'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('curved', 'bay', 'with', 'two', 'wave', 'lines')

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
        path('coast',(44,10),[('A',(40,14),4,4,False),('L',(40,22)),('L',(33,22)),('C',(25,12),(27,22),(29,12)),('C',(12,10),(20,12),(19,10)),('L',(8,10)),('A',(4,14),4,4,False),('L',(4,24)),('A',(18,38),14,14,False),('L',(30,38)),('A',(44,24),14,14,False)])
        path('wave-upper',(13,20),[('C',(20,20),(15,18),(18,22))])
        path('wave-lower',(16,29),[('C',(26,29),(19,28),(23,30))])
