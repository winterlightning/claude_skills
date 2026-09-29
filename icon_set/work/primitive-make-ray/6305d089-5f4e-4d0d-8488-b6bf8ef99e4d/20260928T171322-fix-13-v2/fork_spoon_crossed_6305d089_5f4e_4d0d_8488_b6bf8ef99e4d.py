"""Rejected fork is too heavy and its spoon bowl is small. Restore three distinct fork tines, a larger tilted oval spoon bowl, and balanced crossing handles.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: utensils-crossed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6305d089-5f4e-4d0d-8488-b6bf8ef99e4d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fork-spoon-crossed/20260928T171322Z-thuan-mac/reference/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='fork-spoon-crossed'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('spoon', 'and', 'fork')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('fork',(4,12),[('L',(12,20)),('C',(20,20),(14,22),(18,22)),('C',(20,12),(22,18),(22,14)),('L',(12,4))])
        line('middle-tine',(8,8),(20,20));join('middle-tine','fork')
        poly('fork-handle',(20,20),(24,24),(42,42));join('fork-handle','fork');join('fork-handle','middle-tine')
        path('spoon',(28,20),[('C',(29,7),(24,16),(25,11)),('C',(42,6),(33,3),(39,3)),('C',(41,19),(45,9),(45,15)),('C',(28,20),(37,23),(32,24))],True)
        poly('spoon-handle',(28,20),(24,24),(6,42));join('spoon-handle','spoon');join('spoon-handle','fork-handle')


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

