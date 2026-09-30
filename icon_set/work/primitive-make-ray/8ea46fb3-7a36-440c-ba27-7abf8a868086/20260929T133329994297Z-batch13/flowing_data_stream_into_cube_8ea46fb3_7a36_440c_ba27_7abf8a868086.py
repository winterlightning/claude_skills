"""Use three long converging stream curves beside a larger clean isometric cube.
Symbol plan: SQUARE on SOLO48; named shapes and source arrangement.
Before review: The stream curves bend away from the cube and are reduced to four disconnected hooks.
Construction reference: Lucide square: coherent contours and tangent quarter-circle corners.
Omissions: Four streams reduced to three; source rightward convergence preserved.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='8ea46fb3-7a36-440c-ba27-7abf8a868086'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__flowing-data-stream-into-cube/20260929T132621Z-thuan-mac/reference/amazon kinesis data stream_8ea46fb3-7a36-440c-ba27-7abf8a868086.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='flowing-data-stream-into-cube'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('amazon', 'kinesis', 'data', 'stream')
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
        path('upper',(6,6),[('B',(42,14),(12,14),(26,14))])
        path('middle',(6,22),[('B',(18,28),(8,26),(12,28))])
        path('lower',(6,42),[('B',(18,36),(8,38),(12,36))])
        poly('cube',(34,22),(42,27),(42,37),(34,42),(26,37),(26,27),closed=True)
        poly('top-seam',(26,27),(34,32),(42,27));line('stem',(34,32),(34,42));join('top-seam','cube');join('stem','top-seam');join('stem','cube')
