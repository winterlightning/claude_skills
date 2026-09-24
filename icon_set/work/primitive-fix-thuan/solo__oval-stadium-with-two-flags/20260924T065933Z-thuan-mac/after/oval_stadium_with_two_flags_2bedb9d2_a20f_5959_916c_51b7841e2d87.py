"""Oval stadium bowl with a broad opening and two raised flags.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; shared elliptical bowl and repeated flags.
Omissions: Inner field arc omitted because an additional nested opening cannot fit with 8-unit centerline spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2bedb9d2-a20f-5959-916c-51b7841e2d87'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__oval-stadium-with-two-flags/20260924T065933Z-thuan-mac/reference/stadium classic_2bedb9d2-a20f-5959-916c-51b7841e2d87.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='oval-stadium-with-two-flags'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('oval', 'stadium', 'with', 'two', 'flags')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Capsule rim and elliptical wall retain an open bowl; poles end on explicit rim nodes.
        self.path('rim',(12,21),[('L',(34,21)),('L',(36,21)),('A',(42,27),6,6,True),('A',(36,33),6,6,True),('L',(12,33)),('A',(6,27),6,6,True),('A',(12,21),6,6,True)],True)
        self.path('wall',(6,27),[('L',(6,35)),('A',(42,35),18,7,False),('L',(42,27))])
        self.relate('connect','wall','rim')
        for i,x in enumerate([12,34]):
            self.add_polyline('flag-'+str(i),(x,6),(x+8,10),(x,14),closed=True)
            self.add_line('pole-'+str(i),(x,14),(x,21))
            self.relate('connect','pole-'+str(i),'flag-'+str(i));self.relate('connect','pole-'+str(i),'rim')
