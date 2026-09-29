"""The rejected headset is a tall rounded rectangle with a sharp nose notch. Restore the broad, low goggle silhouette, gently domed top and smooth paired eye lobes.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: headset.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vr-headset-video-games/20260928T171322Z-thuan-mac/reference/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vr-headset-video-games'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('vr', 'headset')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('goggles',(4,23),[('C',(12,14),(4,17),(6,14)),('C',(36,14),(19,13),(29,13)),('C',(44,23),(42,14),(44,17)),('C',(36,34),(44,30),(41,34)),('C',(24,28),(30,34),(29,28)),('C',(12,34),(19,28),(18,34)),('C',(4,23),(7,34),(4,30))],True)


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

