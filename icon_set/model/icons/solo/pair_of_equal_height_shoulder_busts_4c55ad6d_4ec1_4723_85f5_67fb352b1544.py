"""Two equal-height human busts with equal circular heads and mirrored shoulders.
Plan: Two equal-height human busts with equal circular heads and mirrored shoulders.
Construction: human_ref/user.svg: circular heads and smooth shoulders; matching geometry reflected about x=24.
Omissions: Oval reference heads normalized to circles; no subject omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '4c55ad6d-4ec1-4723-85f5-67fb352b1544'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sibling_4c55ad6d-4ec1-4723-85f5-67fb352b1544.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pair-of-equal-height-shoulder-busts'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pair', 'of', 'equal', 'height', 'shoulder', 'busts')

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
        # Shared human_ref/user.svg vocabulary. Each head bottom=16, shoulder top=24: 8 centerline / 4 ink gap.
        for side,x in [('left',14),('right',34)]:circle('head-'+side,x,11,5)
        path('shoulders',(6,42),[('L',(6,32)),('A',(14,24),8,8,True),('C',(24,32),(19,24),(21,27)),('C',(34,24),(27,27),(29,24)),('A',(42,32),8,8,True),('L',(42,42)),('L',(24,42)),('L',(6,42))],True)
        line('divider',(24,32),(24,42));join('divider','shoulders')
