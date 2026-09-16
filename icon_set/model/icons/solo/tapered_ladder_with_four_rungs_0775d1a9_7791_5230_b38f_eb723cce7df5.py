"""Tapered Ladder with Four Rungs.

Plan: VRECT centerlines (8,4)-(40,44); mirrored tapered rails, exactly four horizontal rungs at10-unit pitch and equal5-unit end projections. All rung/rail nodes are integer and shared.
Construction references: Supplied tapered ladder source; no useful exact Lucide ladder match.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '0775d1a9-7791-5230-b38f-eb723cce7df5'
SOURCE_PATH = 'pictographic-primitives/business/business ladder_0775d1a9-7791-5230-b38f-eb723cce7df5.svg'
SOURCE_ICON_IDS = ('0775d1a9-7791-5230-b38f-eb723cce7df5',)
SOURCE_PATHS = ('pictographic-primitives/business/business ladder_0775d1a9-7791-5230-b38f-eb723cce7df5.svg',)
AUTHOR = 'gpt-6'


class TaperedLadderWithFourRungs(Solo48):
    icon_id = 'tapered-ladder-with-four-rungs'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('tapered', 'ladder', 'with', 'four', 'rungs')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        y_values=(4,9,19,29,39,44)
        for side in (-1,1):
            self.add_polyline(f"rail-{side}",*[(24+side*(8+(y-4)//5),y) for y in y_values])
        for i,y in enumerate(y_values[1:-1]):
            spread=8+(y-4)//5
            self.add_line(f"rung-{i}",(24-spread,y),(24+spread,y))
            for side in (-1,1):self.relate("connect",f"rung-{i}",f"rail-{side}")
