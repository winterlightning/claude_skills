"""Rejected razor loses the outlined curved handle. Restore the broad blade, diagonal shank and hollow curved handle.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: No exact local Lucide match; pen-line curved construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ee682589-6a41-5314-b057-2d2077e1ed8e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__open-straight-razor-with-curved-handle/20260928T173014Z-thuan-mac/reference/razor_ee682589-6a41-5314-b057-2d2077e1ed8e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-straight-razor-with-curved-handle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('razor',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('blade',(4,10),(7,4),(27,15),(23,22),closed=True)
        line('shank',(27,15),(38,22));join('blade','shank')
        path('handle',(40,18),[('C',(42,22),(42,18),(43,19)),('C',(8,44),(37,34),(23,44)),('C',(8,36),(2,44),(2,36)),('C',(38,22),(22,36),(32,30)),('C',(40,18),(39,20),(39,19))],True);join('shank','handle')


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

