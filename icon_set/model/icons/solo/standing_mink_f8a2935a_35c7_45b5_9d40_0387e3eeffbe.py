"""Standing mink with a smooth long back, rounded head, muzzle and curved foreleg.
Plan: Standing mink with a smooth long back, rounded head, muzzle and curved foreleg.
Construction: Lucide turtle: simplified coherent animal silhouette; mink source controls long torso and raised head.
Omissions: Eye and far-side legs omitted; tail and two standing legs retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'f8a2935a-35c7-45b5-9d40-0387e3eeffbe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mink_f8a2935a-35c7-45b5-9d40-0387e3eeffbe.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='standing-mink'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('standing', 'mink')

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
        path('mink',(6,33),[('C',(18,22),(6,25),(10,22)),('L',(25,22)),('C',(34,10),(31,22),(29,10)),('C',(44,17),(39,10),(40,15)),('C',(38,22),(44,20),(39,19)),('C',(37,32),(37,26),(35,30)),('L',(42,38)),('L',(31,38)),('L',(26,30)),('L',(16,30)),('L',(16,38)),('L',(4,38))])
