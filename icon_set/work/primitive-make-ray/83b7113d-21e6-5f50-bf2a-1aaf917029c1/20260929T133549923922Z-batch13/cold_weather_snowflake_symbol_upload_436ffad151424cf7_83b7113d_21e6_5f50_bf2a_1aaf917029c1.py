"""Rebuild six evenly arranged branches with shared mirrored fork geometry.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The snowflake has five irregular branches and inconsistent fork directions. No separate original is available.
Construction reference: Lucide snowflake: sixfold branching, shared fork parameters; integer geometry mirrored.
Omissions: 
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='83b7113d-21e6-5f50-bf2a-1aaf917029c1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cold-weather-snowflake-symbol-upload-436ffad151424cf7/20260929T132621Z-thuan-mac/reference/cold-weather-snowflake-symbol-upload-436ffad151424cf7_83b7113d-21e6-5f50-bf2a-1aaf917029c1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cold-weather-snowflake-symbol-upload-436ffad151424cf7'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('cold-weather-snowflake-symbol-upload-436ffad151424cf7',)
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
        nodes=[((24,24),(24,6)),((24,24),(42,14)),((24,24),(42,34)),((24,24),(24,42)),((24,24),(6,34)),((24,24),(6,14))]
        for i,(p,q) in enumerate(nodes): line(f'ray-{i}',p,q)
        for i in range(6):
            for j in range(i):join(f'ray-{i}',f'ray-{j}')
        for n,p in [('top',[(17,7),(24,14),(31,7)]),('bottom',[(17,41),(24,34),(31,41)]),('ul',[(6,23),(15,19),(15,11)]),('ur',[(33,11),(33,19),(42,23)]),('ll',[(6,25),(15,29),(15,37)]),('lr',[(33,37),(33,29),(42,25)])]:poly(n,*p)
        for x,y in [('top','ray-0'),('bottom','ray-3'),('ul','ray-5'),('ur','ray-1'),('ll','ray-4'),('lr','ray-2')]:join(x,y)
