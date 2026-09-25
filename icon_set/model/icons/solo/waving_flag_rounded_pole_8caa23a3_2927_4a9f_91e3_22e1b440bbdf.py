"""Flag with matching single-cubic cloth waves translated vertically by20. Pole is exactly straight; upper and lower edges have no intermediate kinks.
Construction: Lucide flag original/atomic-debug: matching flowing cloth edges and vertical pole.
Omissions: No defining feature omitted; intentional rightward asymmetry.
Keyshape VRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8caa23a3-2927-4a9f-91e3-22e1b440bbdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nation_8caa23a3-2927-4a9f-91e3-22e1b440bbdf.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='waving-flag-rounded-pole'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('waving', 'flag', 'rounded', 'pole')
    def build(self):
        self.poly('pole',(8,4),(8,8),(8,28),(8,44))
        self.path('flag',(8,8),[('C',(40,8),(19,0),(29,16)),('L',(40,28)),('C',(8,28),(29,36),(19,20))]);self.join('pole','flag')

    def path(self,n,p,steps,closed=False):
        ids=[]
        for j,step in enumerate(steps):
            k,q,*v=step; uid=f'{n}-{j}'
            if k=='L': self.add_line(uid,p,q)
            elif k=='A': self.add_arc(uid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif k=='C': self.add_bezier(uid,p,(v[0],v[1],q))
            ids.append(uid);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=2):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def line(self,n,a,b): self.add_line(n,a,b)
    def poly(self,n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
    def join(self,a,b): self.relate('connect',a,b)
