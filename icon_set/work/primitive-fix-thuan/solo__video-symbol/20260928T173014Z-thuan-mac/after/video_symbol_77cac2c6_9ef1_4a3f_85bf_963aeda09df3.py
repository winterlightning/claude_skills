"""Rejected body has kinked corners and is too tall. Restore a smooth rounded camera body and proportional right lens wedge.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: video.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='77cac2c6-9ef1-4a3f-85bf-963aeda09df3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__video-symbol/20260928T173014Z-thuan-mac/reference/video_77cac2c6-9ef1-4a3f-85bf-963aeda09df3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='video-symbol'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('video',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('camera',(8,10),[('L',(28,10)),('A',(32,14),4,True),('L',(32,22)),('L',(44,16)),('L',(44,32)),('L',(32,26)),('L',(32,34)),('A',(28,38),4,True),('L',(8,38)),('A',(4,34),4,True),('L',(4,14)),('A',(8,10),4,True)],True)
        line('lens-root',(32,22),(32,26));join('lens-root','camera')


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

