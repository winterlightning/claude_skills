"""The rejected flytrap reads as a chunky crown on a zigzag stalk. Restore its rounded trap bowl, three clearly separated teeth, gently curved stem and a distinct pointed leaf.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: sprout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b27bfeed-a105-4ab7-9c64-52d85a0abb70'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__venus-flytrap-with-leaf/20260928T171322Z-thuan-mac/reference/flytrap_b27bfeed-a105-4ab7-9c64-52d85a0abb70.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='venus-flytrap-with-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('flytrap',)
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('trap',(20,4),[('C',(8,15),(13,5),(8,9)),('C',(14,25),(8,19),(10,22)),('C',(30,29),(20,31),(25,32)),('C',(39,17),(35,27),(38,22)),('L',(30,21)),('L',(33,12)),('L',(24,17)),('L',(27,8)),('L',(18,12)),('L',(20,4))],True)
        path('stem',(14,25),[('C',(14,34),(10,28),(11,30)),('C',(20,40),(17,38),(19,38)),('L',(20,44))]);join('stem','trap')
        path('leaf',(20,40),[('C',(38,34),(24,30),(31,31)),('C',(20,40),(34,44),(26,44))],True);join('leaf','stem')


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

