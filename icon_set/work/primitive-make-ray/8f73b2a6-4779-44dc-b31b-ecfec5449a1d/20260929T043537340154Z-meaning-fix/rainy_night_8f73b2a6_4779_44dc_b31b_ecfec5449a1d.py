"""Restored a closed crescent behind a rounded cloud and three diagonal precipitation strokes.
Plan and comparison: The moon is an open C stroke and the cloud silhouette is angular.
Construction reference: cloud-rain: smooth cloud shoulders and separated weather marks
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8f73b2a6-4779-44dc-b31b-ecfec5449a1d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rainy-night/20260929T043142Z-thuan-mac/reference/weather night snow_8f73b2a6-4779-44dc-b31b-ecfec5449a1d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rainy-night'
    keyshape=Keyshape.SQUARE
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

        # The cloud occludes the lower left moon; the visible crescent retains two edges.
        self.path('moon',(39,4),[('A',(43,24),12,12,False),('A',(39,4),10,10,True)])
        self.path('cloud',(12,32),[('A',(12,18),7,7,True),('A',(30,18),9,9,True),('A',(34,32),7,7,True),('L',(12,32))],True)
        for n,x in enumerate((14,24,34)):
            self.add_line(f'rain-{n}',(x,39),(x-3,44))
