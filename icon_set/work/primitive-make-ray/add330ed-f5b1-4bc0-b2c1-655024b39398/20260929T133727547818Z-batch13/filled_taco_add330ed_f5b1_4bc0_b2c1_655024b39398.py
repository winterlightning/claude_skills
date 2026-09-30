"""Replace the handle-like filling with a scalloped lettuce crest over a broad taco shell.
Symbol plan: HRECT_L on SOLO48; named shapes and source arrangement.
Before review: Rounded filling resembles a handbag handle.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Detached scalloped lettuce crest leaves explicit separation from the shell; tiny bumps omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='add330ed-f5b1-4bc0-b2c1-655024b39398'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__filled-taco/20260929T132621Z-thuan-mac/reference/taco_add330ed-f5b1-4bc0-b2c1-655024b39398.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='filled-taco'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('taco',)
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
        path('shell',(4,40),[('A',(44,40),20,20,True),('L',(4,40))],True)
        path('lettuce',(4,40),[('L',(4,24)),('A',(12,16),8,8,True),('A',(24,8),12,8,True),('A',(36,16),12,8,True),('A',(44,24),8,8,True),('L',(44,40))])
        join('lettuce','shell')
