"""Hand Reaching toward Foot.

Plan: Hand reaches down-left over side-view foot pointing right. Two coherent outlines, bounds (6,6)-(42,42).
Construction: Human reference economy; Lucide hand rounded digits. Source hand/foot relationship.
Reduction: Removed secondary finger curls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '06de442e-575d-48bb-ae42-82d8ef6c23c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/guru purnima hand_06de442e-575d-48bb-ae42-82d8ef6c23c5.svg'
AUTHOR = 'gpt-6'


class HandReachingTowardFoot(Solo48):
    icon_id = 'hand-reaching-toward-foot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('hand', 'reaching', 'toward', 'foot')

    def build(self) -> None:

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
        path('hand',(42,6),[('L',(31,6)),('C',(25,9),(28,6),(27,7)),('L',(19,15)),('A',(25,21),5,5,False),('L',(31,15)),('C',(42,15),(35,19),(40,18))])
        path('foot',(6,28),[('L',(14,28)),('C',(34,32),(14,32),(27,32)),('A',(34,42),5,5,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,28))],True)
