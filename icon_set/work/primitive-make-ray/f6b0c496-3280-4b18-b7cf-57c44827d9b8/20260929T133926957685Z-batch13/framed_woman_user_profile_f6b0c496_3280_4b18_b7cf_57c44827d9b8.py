"""Use a curved face, simple long-hair silhouette and rounded shoulders within the frame.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The shoulder triangle and hair overlap create a ribbon-like portrait instead of a woman.
Construction reference: Shared human_ref/user.svg: circular jaw and smooth shoulders; Lucide square: frame.
Omissions: Facial features omitted; long hair and rounded shoulders retained.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='f6b0c496-3280-4b18-b7cf-57c44827d9b8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__framed-woman-user-profile/20260929T132822Z-thuan-mac/reference/composition window woman_f6b0c496-3280-4b18-b7cf-57c44827d9b8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='framed-woman-user-profile'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('composition', 'window', 'woman')
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
        # Open lower frame behind shoulders avoids a narrow portrait/background strip.
        path('frame',(14,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(34,42))])
        path('crown',(18,22),[('A',(30,22),6,7,True)])
        path('jaw',(30,22),[('A',(18,22),6,6,True)]);join('crown','jaw')
        path('hair-left',(18,22),[('L',(14,34)),('L',(18,38))]);join('hair-left','jaw');join('hair-left','crown')
        path('hair-right',(30,22),[('L',(34,34)),('L',(30,38))]);join('hair-right','jaw');join('hair-right','crown')
        path('shoulders',(14,42),[('L',(18,38)),('L',(24,36)),('L',(30,38)),('L',(34,42))])
        join('shoulders','frame');join('shoulders','hair-left');join('shoulders','hair-right')
