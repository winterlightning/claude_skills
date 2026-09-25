"""Evergreen Pine Tree.

Plan: Mirrored three-tier silhouette around x24; centerlines (8,4)-(40,44). Single trunk joins the flat crown base.
Construction: Lucide tree-pine: stepped branch outline and open-stroke trunk.
Reduction: Trunk becomes one stroke to keep branches dominant.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '06a1cf65-773f-5246-a6d5-0485b57469b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas tree ornaments_06a1cf65-773f-5246-a6d5-0485b57469b2.svg'
AUTHOR = 'gpt-6'


class EvergreenPineTree(Solo48):
    icon_id = 'evergreen-pine-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('evergreen', 'pine', 'tree')

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
        axis=24
        left=[(axis,4),(14,16),(16,16),(10,26),(12,26),(8,36),(axis,36)]
        right=[(2*axis-x,y) for x,y in reversed(left[:-1])]
        self.add_polyline('crown',*(left+right),closed=True)
        self.add_line('trunk',(axis,36),(axis,44))
        self.relate('connect','trunk','crown')
