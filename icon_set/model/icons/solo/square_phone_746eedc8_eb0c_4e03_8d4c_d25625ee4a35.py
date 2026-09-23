from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '746eedc8-eb0c-4e03-8d4c-d25625ee4a35'
SOURCE_PATH = 'icon_set/work/todo-references/square phone_746eedc8-eb0c-4e03-8d4c-d25625ee4a35.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square with a curved telephone handset; handset orientation follows the source.
# References: phone: continuous curved handset with shaped grips. The hangup source has no slash.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'phone')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_bezier('handset',(17,15),
            ((19,13),(20,15),(21,18)),
            ((23,21),(20,21),(19,24)),
            ((20,27),(24,30),(27,29)),
            ((29,26),(29,25),(32,27)),
            ((33,28),(35,29),(33,32)),
            ((29,37),(18,29),(15,22)),
            ((13,18),(15,16),(17,15)))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
