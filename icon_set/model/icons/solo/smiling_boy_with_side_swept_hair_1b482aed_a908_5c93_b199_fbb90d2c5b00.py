"""Smiling Boy with Side-Swept Hair.

Plan: SQUARE centerlines (6,6)-(42,42); circular face with sweeping asymmetric hair and one curved smile. Circular jaw follows the shared human reference.
Construction references: Shared human_ref/user.svg for circular face; supplied boy head for directional hair and smile.
Reduction: Omitted tiny eyes and ears to maintain open facial space. Isolated head: no head/body gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1b482aed-a908-5c93-b199-fbb90d2c5b00'
SOURCE_PATH = 'pictographic-primitives/avatars/boy head_1b482aed-a908-5c93-b199-fbb90d2c5b00.svg'
SOURCE_ICON_IDS = ('1b482aed-a908-5c93-b199-fbb90d2c5b00',)
SOURCE_PATHS = ('pictographic-primitives/avatars/boy head_1b482aed-a908-5c93-b199-fbb90d2c5b00.svg',)
AUTHOR = 'gpt-6'


class SmilingBoyWithSideSweptHair(Solo48):
    icon_id = 'smiling-boy-with-side-swept-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('smiling', 'boy', 'with', 'side-swept', 'hair')
    HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"
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

        path("face",(6,24),[("A",(42,24),18,18,True),("A",(6,24),18,18,True)],True)
        path("hair",(6,24),[("C",(14,16),(6,20),(10,16)),("C",(30,16),(22,20),(26,20)),("C",(42,24),(32,20),(38,22))])
        self.relate("connect","face","hair")
        path("smile",(18,30),[("C",(30,30),(21,34),(27,34))])
