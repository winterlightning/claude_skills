"""Farmer in Broad-Brimmed Hat.

Plan: VRECT centerlines (8,4)-(40,44); flat-topped broad hat, circular radius-10 jaw centered at x24, smooth shoulders and bib overalls. Jaw bottom24 and shoulder top28 give exactly zero visible ink gap, per current avatar contract.
Construction references: Shared human_ref/user.svg for circular face and curved open shoulders; inspected farmer-man-avatar for the validated bib construction.
Reduction: Omitted ears and the small V neckline; retained the tall hat and overall straps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'f06d4ddf-8967-5755-aa5f-6eccdebe382f'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar farmer man_f06d4ddf-8967-5755-aa5f-6eccdebe382f.svg'
SOURCE_ICON_IDS = ('f06d4ddf-8967-5755-aa5f-6eccdebe382f',)
SOURCE_PATHS = ('pictographic-primitives/avatars/avatar farmer man_f06d4ddf-8967-5755-aa5f-6eccdebe382f.svg',)
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'


class FarmerInBroadBrimmedHat(Solo48):
    icon_id = 'farmer-in-broad-brimmed-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('farmer', 'in', 'broad-brimmed', 'hat')

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

        axis=24
        path("crown",(12,14),[("C",(18,4),(14,14),(14,4)),("L",(30,4)),("C",(36,14),(34,4),(34,14))])
        self.add_polyline("brim",(8,14),(12,14),(14,14),(34,14),(36,14),(40,14))
        self.relate("connect","crown","brim")
        self.add_arc("face",(34,14),(14,14),radius_x=10)
        self.relate("connect","face","brim")
        head_bottom=24
        top=head_bottom+HEAD_BODY_CENTERLINE_GAP
        path("shoulder-left",(8,44),[("L",(8,40)),("A",(18,top),10,40-top,True)])
        self.add_line("body-top-left",(18,top),(24,top))
        self.add_line("body-top-right",(24,top),(30,top))
        path("shoulder-right",(30,top),[("A",(40,40),10,40-top,True),("L",(40,44))])
        self.relate("connect","shoulder-left","body-top-left")
        self.relate("connect","body-top-left","body-top-right")
        self.relate("connect","body-top-right","shoulder-right")
        self.relate("connect","face","body-top-left")
        self.relate("connect","face","body-top-right")
        self.add_polyline("overalls",(18,top),(18,44),(30,44),(30,top))
        self.relate("connect","body-top-left","overalls")
        self.relate("connect","body-top-right","overalls")
