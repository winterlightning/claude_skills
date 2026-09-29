"""The rejected cube is squashed into a layered hexagon with heavy node joints. Restore three visible cube faces and three equal endpoint nodes with distinct connecting stems.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: box.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0d0d1025-1418-574d-b291-75e0e612531c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cube-with-three-connected-nodes-batch-018-14/20260928T171322Z-thuan-mac/reference/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cube-with-three-connected-nodes-batch-018-14'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rotate', 'd')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('cube-outline',(24,15),(35,21),(35,32),(24,38),(13,32),(13,21),(24,15))
        poly('cube-y',(13,21),(24,27),(35,21));line('cube-center',(24,27),(24,38))
        join('cube-outline','cube-y');join('cube-outline','cube-center');join('cube-y','cube-center')
        for n,x,y,a,b in [('top',24,8,(24,12),(24,15)),('left',8,40,(8,36),(13,32)),('right',40,40,(40,36),(35,32))]:
            circle(n+'-node',x,y,4);line(n+'-stem',a,b);join(n+'-node',n+'-stem');join(n+'-stem','cube-outline')


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

