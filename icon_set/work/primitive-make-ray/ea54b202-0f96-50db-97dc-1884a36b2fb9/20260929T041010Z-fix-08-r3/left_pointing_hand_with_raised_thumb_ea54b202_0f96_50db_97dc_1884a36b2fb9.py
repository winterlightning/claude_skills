"""Rejected hand has a tiny thumb bump and merged curled fingers. Restore a raised diagonal thumb, long left index and three clear curled-finger levels."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ea54b202-0f96-50db-97dc-1884a36b2fb9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__left-pointing-hand-with-raised-thumb/20260929T041010Z-thuan-mac/reference/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg'
AUTHOR='gpt-6'
PLAN='Rejected hand has a tiny thumb bump and merged curled fingers. Restore a raised diagonal thumb, long left index and three clear curled-finger levels.'
CONSTRUCTION_REFERENCE='Lucide hand original and atomic-debug: rounded finger ends and continuous palm.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='left-pointing-hand-with-raised-thumb'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('outline',(23,16),[('C',(24,8),(17,13),(19,8)),('C',(31,12),(27,8),(29,10)),('L',(39,20)),('C',(44,28),(43,24),(44,25)),('L',(44,31)),('A',(35,40),9,9,True),('L',(21,40)),('A',(21,32),4,4,True),('L',(27,32))])
        self.path('index',(23,16),[('L',(8,16)),('A',(8,24),4,4,False),('L',(25,24))])
        self.path('middle',(18,24),[('A',(18,32),4,4,False),('L',(23,32))])
        self.relate('connect','outline','index');self.relate('connect','index','middle');self.relate('connect','middle','outline')
