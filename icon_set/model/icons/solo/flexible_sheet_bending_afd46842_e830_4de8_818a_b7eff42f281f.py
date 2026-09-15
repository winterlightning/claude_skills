"""Flexible Sheet Bending.

Plan: VRECT centerlines (8,4)-(40,44); two coherent bowed edges share one width and identical curve controls translated horizontally.
Construction references: Supplied bent-sheet silhouette; no useful exact Lucide match.
Reduction: Removed the detached echo stroke to keep generous clearance around the material edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'afd46842-e830-4de8-818a-b7eff42f281f'
SOURCE_PATH = 'pictographic-primitives/construction/bendable_afd46842-e830-4de8-818a-b7eff42f281f.svg'
SOURCE_ICON_IDS = ('afd46842-e830-4de8-818a-b7eff42f281f',)
SOURCE_PATHS = ('pictographic-primitives/construction/bendable_afd46842-e830-4de8-818a-b7eff42f281f.svg',)
AUTHOR = 'gpt-6'


class FlexibleSheetBending(Solo48):
    icon_id = 'flexible-sheet-bending'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('flexible', 'sheet', 'bending')

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

        width=20
        path("sheet",(20,4),[("L",(20+width,4)),("C",(8+width,44),(40,22),(36,34)),("L",(8,44)),("C",(20,4),(16,34),(20,22))],True)
