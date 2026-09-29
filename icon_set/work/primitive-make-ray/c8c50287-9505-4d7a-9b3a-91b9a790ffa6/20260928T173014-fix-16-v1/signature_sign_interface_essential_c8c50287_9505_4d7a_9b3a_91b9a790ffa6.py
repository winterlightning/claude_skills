"""Rejected signature crowns are flat and kinked. Restore a tall smooth first arch and smaller second arch, with continuous flowing stroke.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: signature.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c8c50287-9505-4d7a-9b3a-91b9a790ffa6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__signature-sign-interface-essential/20260928T173014Z-thuan-mac/reference/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='signature-sign-interface-essential'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('signature', 'sign')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('signature',(4,40),[('L',(14,16)),('C',(23,8),(17,10),(20,8)),('C',(27,14),(28,8),(29,9)),('L',(20,32)),('C',(22,38),(18,37),(18,40)),('C',(33,24),(26,36),(29,28)),('C',(40,19),(37,20),(40,16)),('C',(38,31),(40,23),(38,28)),('C',(42,37),(38,35),(38,40)),('C',(44,34),(43,36),(44,35))])


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

