"""Use an irregular fried-egg outline, flowing bacon edges and sausage score.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: Egg is a plain circle, bacon is a rigid H-like strip and sausage has no scoring.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: One sausage score and a dot yolk retain readable spacing.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9cd5bf77-b0ca-4e59-86ca-62d4b29d41fd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__egg-bacon-and-sausage-breakfast/20260929T132621Z-thuan-mac/reference/breakfast english_9cd5bf77-b0ca-4e59-86ca-62d4b29d41fd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='egg-bacon-and-sausage-breakfast'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('breakfast', 'english')
    def build(self):

        def path(n,start,steps,closed=False):
            p=start; members=[]
            for i,step in enumerate(steps):
                k,end,*a=step; name=f'{n}-{i}'
                if k=='L': self.add_line(name,p,end)
                elif k=='A': self.add_arc(name,p,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif k=='B': self.add_bezier(name,p,(a[0],a[1],end))
                members.append(name);p=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=4):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        box('sausage',6,6,42,14,4)
        line('score',(24,6),(28,14));join('score','sausage')
        path('egg',(6,32),[('A',(16,23),10,9,True),('B',(24,32),(23,23),(24,26)),('A',(16,42),8,10,True),('A',(6,32),10,10,True)],True)
        self.add_dot('yolk',(15,32))
        path('bacon',(34,23),[('B',(34,42),(34,30),(32,34)),('L',(42,42)),('B',(42,23),(42,34),(42,30)),('L',(34,23))],True)
