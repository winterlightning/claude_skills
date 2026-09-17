"""Temple under Moon and Cloud.

Plan: Domed temple and pointed spire under moon/cloud left. Bounds (6,6)-(42,42).
Construction: Source temple; Lucide cloud and moon economy.
Reduction: Doorway and tower bands omitted; moon and cloud reduced to separate open arc and rounded cloud outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '958ec275-d2c4-4051-9bda-84c178a164c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/poya day_958ec275-d2c4-4051-9bda-84c178a164c4.svg'
AUTHOR = 'gpt-6'


class IconTempleUnderMoonAndCloud(Solo48):
    icon_id = 'temple-under-moon-and-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('temple', 'under', 'moon', 'and', 'cloud')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('temple',(22,42),[('A',(32,32),10,10,True),('A',(42,42),10,10,True),('L',(22,42))],True)
        path('spire',(32,32),[('L',(32,20)),('L',(24,20)),('L',(32,6)),('L',(40,20)),('L',(32,20))]);self.relate('connect','spire','temple')
        path('moon',(10,6),[('A',(6,10),4,4,False)])
        path('cloud',(6,28),[('C',(11,20),(6,22),(8,20)),('C',(16,28),(14,20),(16,22)),('L',(6,28))],True)
