"""Restored two separated raised fingers, two curled knuckles, and a thumb crossing the palm.
Plan and comparison: The folded fingers became edge bumps and the crossing thumb disappeared.
Construction reference: hand: connected rounded finger construction; asymmetry preserves the V gesture
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d445cb84-69cc-4534-88ca-0620e15e15d7'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__raised-peace-sign-hand/20260929T043142Z-thuan-mac/reference/peace sign_d445cb84-69cc-4534-88ca-0620e15e15d7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='raised-peace-sign-hand'
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

        # V fingers form the upper silhouette; folded fingers and thumb form the lower hand.
        self.path('hand',(16,25),[('L',(10,8)),('A',(16,6),3,3,True),('L',(23,23)),('L',(29,6)),('A',(35,8),3,3,True),('L',(30,26)),('L',(34,27)),('A',(37,31),4,4,True),('L',(37,34)),('A',(12,36),13,13,True),('L',(9,30)),('A',(15,28),3,3,True)])
        self.path('folded-fingers',(16,34),[('L',(13,26)),('A',(19,24),3,3,True),('L',(22,32))])
        self.path('thumb',(31,35),[('A',(26,31),5,5,False),('L',(20,29)),('A',(22,24),3,3,True),('L',(30,26))])
        self.relate('connect','thumb','hand')
