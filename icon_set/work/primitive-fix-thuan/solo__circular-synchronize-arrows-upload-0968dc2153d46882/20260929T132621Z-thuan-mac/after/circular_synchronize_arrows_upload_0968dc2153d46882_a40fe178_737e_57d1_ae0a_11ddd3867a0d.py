"""Balance two opposing round sweeps and equal open arrowheads.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: Short uneven arrowheads and a tilted uneven loop weaken the synchronize symbol. No separate original is available.
Construction reference: Lucide refresh-cw: two opposing sweeps with matching open arrowheads.
Omissions: 
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='a40fe178-737e-57d1-ae0a-11ddd3867a0d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__circular-synchronize-arrows-upload-0968dc2153d46882/20260929T132621Z-thuan-mac/reference/circular-synchronize-arrows-upload-0968dc2153d46882_a40fe178-737e-57d1-ae0a-11ddd3867a0d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circular-synchronize-arrows-upload-0968dc2153d46882'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('circular-synchronize-arrows-upload-0968dc2153d46882',)
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
        path('upper',(6,15),[('A',(24,6),18,9,True),('A',(42,24),18,18,True)])
        poly('upper-head',(32,24),(42,24),(42,14));join('upper-head','upper')
        path('lower',(42,33),[('A',(24,42),18,9,True),('A',(6,24),18,18,True)])
        poly('lower-head',(16,24),(6,24),(6,34));join('lower-head','lower')
