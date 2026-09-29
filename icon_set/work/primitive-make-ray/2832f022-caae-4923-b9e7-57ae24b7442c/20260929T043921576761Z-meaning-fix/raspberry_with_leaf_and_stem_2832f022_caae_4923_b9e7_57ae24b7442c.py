"""Restored a layered tapered berry, a pointed side leaf and a curved stem.
Plan and comparison: The repeated bumps read as a cog or flower rather than a raspberry made of round drupelets.
Construction reference: grape: rounded drupelets and a distinct stem, with the supplied asymmetric leaf retained
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2832f022-caae-4923-b9e7-57ae24b7442c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__raspberry-with-leaf-and-stem/20260929T043142Z-thuan-mac/reference/raspberry_2832f022-caae-4923-b9e7-57ae24b7442c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='raspberry-with-leaf-and-stem'
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

        # Curved upright stem and one leaf retain the natural asymmetric crown.
        self.path('stem',(25,17),[('A',(33,4),18,18,True)])
        self.path('leaf',(24,15),[('A',(11,5),13,13,False),('A',(24,15),13,13,False)],True)

        # Berry is a tapered cluster of six visible drupelets, with no hidden overlapping outlines.
        self.circle('middle',24,24,6)
        self.path('left',(19,19),[('A',(13,29),7,7,False),('L',(19,29))])
        self.path('right',(29,19),[('A',(35,29),7,7,True),('L',(29,29))])
        self.path('lower-left',(13,29),[('A',(24,37),7,7,False)])
        self.path('lower-right',(35,29),[('A',(24,37),7,7,True)])
        self.path('tip',(18,38),[('A',(30,38),6,6,False)])
