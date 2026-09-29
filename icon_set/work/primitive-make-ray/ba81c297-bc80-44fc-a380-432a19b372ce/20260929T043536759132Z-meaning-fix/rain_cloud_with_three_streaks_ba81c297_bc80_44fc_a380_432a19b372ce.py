"""Restored a tall central cloud lobe and three slanted rain streaks with a longer middle streak.
Plan and comparison: The cloud is flattened and every rain streak has the same short length.
Construction reference: cloud-rain: distinct cloud lobe and detached rain strokes
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ba81c297-bc80-44fc-a380-432a19b372ce'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rain-cloud-with-three-streaks/20260929T043142Z-thuan-mac/reference/hail_ba81c297-bc80-44fc-a380-432a19b372ce.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rain-cloud-with-three-streaks'
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

        # Cloud owns three rounded lobes and a flat base; rain is a detached series.
        self.path('cloud',(12,28),[('A',(12,12),8,8,True),('L',(14,12)),('A',(34,14),10,10,True),('L',(36,14)),('A',(36,28),7,7,True),('L',(12,28))],True)
        for n,(x,y) in enumerate(((12,40),(24,44),(36,40))):
            self.add_line(f'rain-{n}',(x,35),(x-3,y))
