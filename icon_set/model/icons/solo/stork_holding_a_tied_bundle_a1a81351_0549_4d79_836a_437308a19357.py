"""Stork holding a teardrop bundle, with smooth head and neck transitions.
Plan: Stork holding a teardrop bundle, with smooth head and neck transitions.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Eye and small bow loops omitted; carrying beak and tied bundle silhouette retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'a1a81351-0549-4d79-836a-437308a19357'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby stork_a1a81351-0549-4d79-836a-437308a19357.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stork-holding-a-tied-bundle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('stork', 'holding', 'a', 'tied', 'bundle')

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
        path('stork',(6,42),[('C',(10,34),(12,42),(11,38)),('C',(6,18),(9,29),(6,23)),('C',(17,6),(6,10),(9,6)),('C',(24,14),(23,6),(24,9)),('C',(19,26),(24,19),(19,22)),('C',(19,42),(19,34),(19,38))])
        line('beak',(24,14),(36,18));join('beak','stork')
        path('bundle',(36,18),[('C',(42,34),(39,23),(42,29)),('C',(36,42),(42,39),(40,42)),('C',(30,34),(32,42),(30,39)),('C',(36,18),(30,29),(33,23))],True);join('beak','bundle')
