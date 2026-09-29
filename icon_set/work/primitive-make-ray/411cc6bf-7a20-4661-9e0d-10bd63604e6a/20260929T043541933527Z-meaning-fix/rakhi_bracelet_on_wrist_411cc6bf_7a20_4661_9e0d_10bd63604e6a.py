"""Rebuilt a diagonal closed hand, a continuous wrist band and a central circular rakhi ornament.
Plan and comparison: The wrist ornament sits outside the arm and the palm became a jagged outline.
Construction reference: hand: rounded knuckle silhouettes; intentional diagonal wrist arrangement
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='411cc6bf-7a20-4661-9e0d-10bd63604e6a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rakhi-bracelet-on-wrist/20260929T043142Z-thuan-mac/reference/raksha bandhan_411cc6bf-7a20-4661-9e0d-10bd63604e6a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rakhi-bracelet-on-wrist'
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

        # The arm runs diagonally; the bracelet crosses it at the wrist.
        self.path('outer',(27,4),[('L',(36,12)),('L',(43,17)),('L',(34,27)),('A',(32,36),10,10,True),('L',(25,43)),('A',(20,39),3,3,True)])
        self.path('lower',(20,39),[('A',(15,40),3,3,True),('L',(10,35)),('A',(6,30),4,4,True),('L',(16,18)),('L',(23,10))])
        self.add_line('finger-1',(15,32),(11,36)); self.relate('connect','finger-1','lower')
        self.add_line('finger-2',(22,33),(18,38))
        self.circle('rakhi',29,16,5)
        self.add_line('band-left',(21,10),(25,13)); self.relate('connect','band-left','rakhi')
        self.add_line('band-right',(33,19),(39,22)); self.relate('connect','band-right','rakhi')
