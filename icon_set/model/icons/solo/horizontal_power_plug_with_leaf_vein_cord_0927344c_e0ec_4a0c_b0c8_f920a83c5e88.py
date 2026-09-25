"""Horizontal plug with two pins; smooth looping cord merges into a pointed leaf and its vein.
Keyshape SQUARE. Lucide leaf: flowing leaf silhouette and integral vein.
Omissions: Minor secondary vein omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0927344c-e0ec-4a0c-b0c8-f920a83c5e88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/renewable energy charging_0927344c-e0ec-4a0c-b0c8-f920a83c5e88.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'horizontal-power-plug-with-leaf-vein-cord'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases=()
    keywords=('horizontal', 'power', 'plug', 'with', 'leaf', 'vein', 'cord')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('plug',(14,6),[('L',(20,6)),('A',(26,12),6,6,True),('A',(20,18),6,6,True),('L',(14,18)),('L',(14,16)),('L',(14,8)),('L',(14,6))],True)
        for y in (8,16):line(f'pin-{y}',(6,y),(14,y));join(f'pin-{y}','plug')
        path('cord',(26,12),[('L',(34,12)),('A',(42,20),8,8,True),('L',(42,34))]);join('cord','plug')
        path('leaf',(42,34),[('C',(20,26),(34,26),(27,24)),('C',(14,34),(16,27),(14,30)),('C',(25,42),(14,39),(19,42)),('C',(42,34),(33,42),(39,37))],True)
        path('vein',(42,34),[('L',(25,34))]);join('leaf','vein');join('leaf','cord');join('cord','vein')

