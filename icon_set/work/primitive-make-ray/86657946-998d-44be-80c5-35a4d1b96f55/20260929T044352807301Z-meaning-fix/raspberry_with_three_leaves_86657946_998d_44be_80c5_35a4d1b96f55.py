"""Restored a tapered six-segment berry and three individually legible pointed leaves.
Plan and comparison: The fruit has only two oversized lobes and a tiny base, losing the clustered berry structure.
Construction reference: grape: visible rounded fruit segments; reference supplies three-leaf crown
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='86657946-998d-44be-80c5-35a4d1b96f55'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__raspberry-with-three-leaves/20260929T043142Z-thuan-mac/reference/boysenberry_86657946-998d-44be-80c5-35a4d1b96f55.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='raspberry-with-three-leaves'
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

        # Three leaves are arranged around the center axis; fruit owns its repeated segments.
        self.path('leaf-center',(24,16),[('A',(24,3),9,9,True),('A',(24,16),9,9,True)],True)
        self.path('leaf-left',(20,16),[('A',(8,7),12,12,False),('A',(20,16),12,12,False)],True)
        self.path('leaf-right',(28,16),[('A',(40,7),12,12,True),('A',(28,16),12,12,True)],True)

        # Berry is a tapered cluster of six visible drupelets, with no hidden overlapping outlines.
        self.circle('middle',24,22,6)
        self.path('left',(19,18),[('A',(8,23),7,7,False),('A',(13,30),7,7,False),('A',(19,27),7,7,False)])
        self.path('right',(29,18),[('A',(40,23),7,7,True),('A',(35,30),7,7,True),('A',(29,27),7,7,True)])
        self.path('lower-left',(13,30),[('A',(24,37),8,8,False)])
        self.path('lower-right',(35,30),[('A',(24,37),8,8,True)])
        self.add_line('fruit-seam',(24,28),(24,37)); self.relate('connect','fruit-seam','middle'); self.relate('connect','fruit-seam','lower-left'); self.relate('connect','fruit-seam','lower-right')
        self.path('tip',(18,38),[('A',(30,38),6,6,False)])

Drawing.exception = {'reason': 'The three pointed leaves and touching berry segments retain narrow natural openings. The crown and six visible fruit segments remain readable at 48px. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9545ecc7ab606ac300af08f7147670c2aef82fe9da25aedcd640f5dfc7ae6cb9'}
