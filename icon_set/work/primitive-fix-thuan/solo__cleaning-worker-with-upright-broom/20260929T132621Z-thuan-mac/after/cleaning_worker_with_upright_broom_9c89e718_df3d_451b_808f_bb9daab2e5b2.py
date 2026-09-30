"""Give the worker a curved jaw beneath a cap and broad shoulders, beside a clean broom.
Symbol plan: HRECT_L on SOLO48; named shapes and source arrangement.
Before review: Cap brim cuts the face in half and the bust has an excessive detached gap.
Construction reference: Shared human_ref/user.svg: round jaw and broad smooth shoulders; source cap and broom.
Omissions: Facial features and collar omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9c89e718-df3d-451b-808f-bb9daab2e5b2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cleaning-worker-with-upright-broom/20260929T132621Z-thuan-mac/reference/janitor_9c89e718-df3d-451b-808f-bb9daab2e5b2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cleaning-worker-with-upright-broom'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('janitor',)
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
        path('cap',(8,16),[('A',(20,16),6,8,True)])
        path('jaw',(20,16),[('A',(8,16),6,6,True)])
        join('cap','jaw')
        line('brim',(8,16),(22,16));join('brim','cap');join('brim','jaw')
        path('shoulders',(4,40),[('A',(14,30),10,10,True),('A',(24,40),10,10,True)])
        line('handle',(38,8),(38,30))
        poly('broom',(38,30),(42,30),(44,40),(32,40),(34,30),(38,30),closed=True);join('handle','broom')
