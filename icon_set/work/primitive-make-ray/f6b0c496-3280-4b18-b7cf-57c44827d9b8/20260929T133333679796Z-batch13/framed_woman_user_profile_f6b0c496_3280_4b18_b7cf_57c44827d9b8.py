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
        box('frame',6,6,42,42,4)
        path('hair',(15,32),[('L',(15,23)),('A',(33,23),9,9,True),('L',(33,32))])
        path('jaw',(18,23),[('A',(30,23),6,6,False)])
        path('shoulders',(14,42),[('L',(14,39)),('A',(24,33),10,6,True),('A',(34,39),10,6,True),('L',(34,42))])
        join('shoulders','frame');join('jaw','hair')
