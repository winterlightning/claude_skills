"""Six Armed Snowflake.

Plan: Six spokes and twelve branch tips from shared center24. Bounds (6,6)-(42,42).
Construction: Lucide snowflake repetition and sixfold branching; supplied source straight radial structure.
Reduction: One fork per spoke; integer-grid diagonal pairs mirror without artificial tiny gaps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'b065d72b-169f-5562-98ee-79f23cac025a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas snowflake_b065d72b-169f-5562-98ee-79f23cac025a.svg'
AUTHOR = 'gpt-6'


class IconSixArmedSnowflake(Solo48):
    icon_id = 'six-armed-snowflake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('six', 'armed', 'snowflake')

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
        spokes=[((24,6),(24,13),[(18,8),(30,8)]),((42,14),(35,18),[(34,10),(42,20)]),((42,34),(35,30),[(42,28),(34,38)]),((24,42),(24,35),[(18,40),(30,40)]),((6,34),(13,30),[(6,28),(14,38)]),((6,14),(13,18),[(14,10),(6,20)])]
        for i,(tip,junction,branches) in enumerate(spokes):
         path('spoke'+str(i),(24,24),[('L',junction),('L',tip)])
         for j,b in enumerate(branches):self.add_line(f'branch{i}-{j}',junction,b);self.relate('connect',f'branch{i}-{j}','spoke'+str(i))
        for i in range(6):
         for j in range(i):self.relate('connect','spoke'+str(i),'spoke'+str(j))
