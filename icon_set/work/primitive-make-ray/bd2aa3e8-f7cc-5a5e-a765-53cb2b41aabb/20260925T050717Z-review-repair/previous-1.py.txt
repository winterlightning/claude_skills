"""Android Mascot with Arms.

Plan: Symmetric dome/body with a structural head seam, paired antennae and short rounded legs. HRECT (4,8)-(44,40) with arms; VRECT (8,4)-(40,44) without. Shared radii and mirrored attachment nodes.
Construction references: Lucide bot: minimal antenna/body construction, paired appendages; supplied Android source owns the dome silhouette.
Reduction: Replaced outlined legs and optional arms with rounded strokes to preserve clear appendages; retained the blank face in the sources.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb'
SOURCE_PATH = 'pictographic-primitives/apps/android_bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb.svg'
SOURCE_ICON_IDS = ('bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb',)
SOURCE_PATHS = ('pictographic-primitives/apps/android_bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb.svg',)
AUTHOR = 'gpt-6'


class AndroidMascotWithArms(Solo48):
    icon_id = 'android-mascot-with-arms'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    aliases = ()
    keywords = ('android', 'mascot', 'with', 'arms')

    def build(self) -> None:
        axis = 24
        left, right, dome_y = 14, 34, 20
        self.add_arc("dome-left-low",(left,dome_y),(18,12),radius_x=10,radius_y=10)
        self.add_arc("dome-left-high",(18,12),(axis,10),radius_x=10,radius_y=10)
        self.add_arc("dome-right-high",(axis,10),(30,12),radius_x=10,radius_y=10)
        self.add_arc("dome-right-low",(30,12),(right,dome_y),radius_x=10,radius_y=10)
        self.add_line("right-wall",(right,dome_y),(right,32))
        self.add_arc("lower-right",(right,32),(30,36),radius_x=4)
        self.add_line("bottom-right",(30,36),(28,36))
        self.add_line("bottom-mid",(28,36),(20,36))
        self.add_line("bottom-left",(20,36),(18,36))
        self.add_arc("lower-left",(18,36),(left,32),radius_x=4)
        self.add_line("left-wall",(left,32),(left,dome_y))
        self.add_contour("body","dome-left-low","dome-left-high","dome-right-high","dome-right-low","right-wall","lower-right","bottom-right","bottom-mid","bottom-left","lower-left","left-wall",closed=True)
        self.add_line("head-seam",(left,dome_y),(right,dome_y))
        self.relate("connect","body","head-seam")
        for side,x in [("left",20),("right",28)]:
            self.add_line(f"leg-{side}",(x,36),(x,40))
            self.relate("connect","body",f"leg-{side}")
        # Antennae join exact Pythagorean points on the circular dome, which is
        # split below at those owning attachment nodes rather than near-touching it.

        for side,x,dx in [("left",18,-4),("right",30,4)]:
            self.add_line(f"antenna-{side}",(x,12),(x+dx,8))
            self.relate("connect","body",f"antenna-{side}")

        for side,x in [("left",4),("right",44)]:
            self.add_line(f"arm-{side}",(x,24),(x,31))
