"""Restored a house with a doorway above a complete pointing hand, including bent fingers and wrist.
Plan and comparison: The house has no doorway and the pointing hand has a floating mitten silhouette without a wrist.
Construction reference: hand: rounded finger caps and coherent thumb; supplied reference owns the pointing gesture and house
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='eb4e4433-41fd-4f9e-9779-df93d4b8c025'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__real-estate-search-house-2/20260929T043142Z-thuan-mac/reference/real estate search house 2_eb4e4433-41fd-4f9e-9779-df93d4b8c025.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='real-estate-search-house-2'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # Small house is separate above the pointing fingertip; the full hand keeps its wrist opening.
        self.add_polyline('roof',(26,12),(36,4),(46,12))
        self.add_polyline('house',(28,11),(28,18),(44,18),(44,11))
        self.relate('connect','roof','house')
        self.add_polyline('door',(33,18),(33,12),(39,12),(39,18)); self.relate('connect','door','house')
        self.path('hand',(14,44),[('L',(14,40)),('L',(7,31)),('A',(12,28),3,3,True),('L',(15,32)),('L',(15,21)),('A',(21,21),3,3,True),('L',(21,28)),('A',(27,28),3,3,True),('A',(33,29),3,3,True),('L',(33,36)),('A',(31,40),8,8,True),('L',(31,44))])
        self.add_line('fold-1',(21,28),(21,32)); self.relate('connect','fold-1','hand')
        self.add_line('fold-2',(27,28),(27,32)); self.relate('connect','fold-2','hand')
