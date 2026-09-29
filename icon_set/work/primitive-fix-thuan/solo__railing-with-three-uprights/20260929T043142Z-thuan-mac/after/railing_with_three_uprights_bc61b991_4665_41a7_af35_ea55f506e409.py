"""Restored two rounded outlined rails with three evenly spaced upright supports.
Plan and comparison: The solid bars make a Roman numeral rather than the reference railing with broad outlined rails.
Construction reference: no useful exact Lucide match; coherent circular arcs and shared parameters
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bc61b991-4665-41a7-af35-ea55f506e409'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__railing-with-three-uprights/20260929T043142Z-thuan-mac/reference/railing_bc61b991-4665-41a7-af35-ea55f506e409.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='railing-with-three-uprights'
    keyshape=Keyshape.HRECT_L
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

        # Two identical rails and one evenly spaced upright series.
        self.box('top-rail',4,8,44,16,2)
        self.box('bottom-rail',4,32,44,40,2)
        for n,x in enumerate((12,24,36)):
            p=f'post-{n}'; self.add_line(p,(x,16),(x,32))
            self.relate('connect',p,'top-rail'); self.relate('connect',p,'bottom-rail')
