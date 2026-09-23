"""A woman with long hair and shoulders within a rounded profile frame.

HRECT_L extrema (4,8)-(44,40). The portrait mirrors around x=24; hair and
shoulders share their base attachments. Human reference user.svg guides face
and shoulder proportions; Lucide contact-round guides the enclosing card.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "f6b0c496-3280-4b18-b7cf-57c44827d9b8"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/composition window woman_f6b0c496-3280-4b18-b7cf-57c44827d9b8.svg"
AUTHOR = "gpt-6"


class FramedWomanUserProfile(Solo48):
    icon_id = "framed-woman-user-profile"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "people/profiles"
    aliases = ("woman portrait", "female profile card")
    keywords = ("user", "avatar", "frame", "hair")

    def build(self) -> None:
        p=[(8,8),(40,8),(44,12),(44,36),(40,40),(8,40),(4,36),(4,12),(8,8)]
        members=[]
        for i,(a,b) in enumerate(zip(p,p[1:])):
            n=f"frame-{i}"
            if i%2:self.add_arc(n,a,b,radius_x=4,radius_y=4,sweep=True)
            else:self.add_line(n,a,b)
            members.append(n)
        self.add_contour("frame",*members,closed=True)
        self.add_bezier("hair-left",(24,16),((17,16),(12,22),(12,30)),((12,34),(13,38),(16,40)))
        self.add_bezier("hair-right",(24,16),((31,16),(36,22),(36,30)),((36,34),(35,38),(32,40)))
        self.add_arc("face-left",(24,16),(24,30),radius_x=7,radius_y=7,sweep=False)
        self.add_arc("face-right",(24,30),(24,16),radius_x=7,radius_y=7,sweep=False)
        self.add_contour("face","face-left","face-right",closed=True)
        self.add_bezier("shoulders-left",(24,30),((21,34),(17,36),(16,40)))
        self.add_bezier("shoulders-right",(24,30),((27,34),(31,36),(32,40)))
        for name in ("hair-left","hair-right","shoulders-left","shoulders-right"):
            self.relate("connect",name,"frame")
        for name in ("hair-left","hair-right","shoulders-left","shoulders-right"):
            self.relate("connect",name,"face")
        self.relate("connect","hair-left","shoulders-left")
        self.relate("connect","hair-right","shoulders-right")
