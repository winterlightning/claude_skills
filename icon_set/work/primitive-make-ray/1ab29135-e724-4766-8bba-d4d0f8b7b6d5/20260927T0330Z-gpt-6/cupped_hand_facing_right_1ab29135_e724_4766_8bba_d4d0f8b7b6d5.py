"""Cupped Hand Facing Right.

Plan: HRECT centerlines (4,8)-(44,40); coherent wrist/palm contour, curved thumb, rounded raised fingers, and one shared thumb-fold junction. Directional asymmetry preserves the right-facing gesture.
Construction references: Lucide hand-helping: one cupped contour and one thumb crease; shared human reference checked for simple rounded limb vocabulary.
Reduction: Unified the two equivalent supplied hand references; omitted extra finger separations.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1ab29135-e724-4766-8bba-d4d0f8b7b6d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupped-hand-facing-right/20260927T032242Z-thuan-mac-1/reference/begging hand ask_1ab29135-e724-4766-8bba-d4d0f8b7b6d5.svg'
SOURCE_ICON_IDS = ('1ab29135-e724-4766-8bba-d4d0f8b7b6d5', 'a322931e-aa9b-59e9-8a03-20657747f732')
SOURCE_PATHS = ('pictographic-primitives/business/begging hand ask_1ab29135-e724-4766-8bba-d4d0f8b7b6d5.svg', 'pictographic-primitives/business/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg')
AUTHOR = "gpt-6"
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'


class CuppedHandFacingRight(Solo48):
    icon_id = 'cupped-hand-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('business', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('cupped', 'hand', 'facing', 'right')

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

        path("hand",(4,16),[("C",(18,8),(10,11),(14,8)),("C",(30,15),(23,8),(27,12)),("C",(32,22),(34,16),(35,19)),("L",(40,15)),("C",(44,18),(44,12),(44,13)),("C",(24,40),(44,30),(34,40)),("C",(4,32),(16,40),(12,32)),("L",(4,16))],True)
        self.add_line("thumb-crease",(32,22),(19,19))
        self.relate("connect","hand","thumb-crease")
