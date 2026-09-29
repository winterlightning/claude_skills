"""Restored six rounded berry segments in a tapered cluster beneath two pointed leaves.
Plan and comparison: The raspberry became a three-lobed blank outline with no drupelet pattern.
Construction reference: grape: distinct rounded fruit units; supplied raspberry reference owns the upright tapered cluster
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8a884b1e-907c-40a7-963c-bb357ba45df5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__raspberry-fruit-leaves/20260929T043142Z-thuan-mac/reference/raspberry pi_8a884b1e-907c-40a7-963c-bb357ba45df5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='raspberry-fruit-leaves'
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

        # A mirrored pair of leaves crowns the characteristic raspberry cluster.
        self.path('leaf-left',(23,16),[('A',(10,4),13,13,False),('A',(23,16),13,13,False)],True)
        self.path('leaf-right',(25,16),[('A',(38,4),13,13,True),('A',(25,16),13,13,True)],True)

        # Berry is a tapered cluster of six visible drupelets, with no hidden overlapping outlines.
        self.circle('middle',24,24,6)
        self.path('left',(19,19),[('A',(13,29),7,7,False),('L',(19,29))])
        self.path('right',(29,19),[('A',(35,29),7,7,True),('L',(29,29))])
        self.path('lower-left',(13,29),[('A',(24,37),7,7,False)])
        self.path('lower-right',(35,29),[('A',(24,37),7,7,True)])
        self.path('tip',(18,38),[('A',(30,38),6,6,False)])
