"""Android Mascot without Arms.

Plan: Symmetric dome/body with a structural head seam, paired antennae and short rounded legs. SQUARE (6,6)-(42,42) with arms; VRECT (8,4)-(40,44) without. Shared radii and mirrored attachment nodes.
Construction references: Lucide bot: minimal antenna/body construction, paired appendages; supplied Android source owns the dome silhouette.
Reduction: Replaced outlined legs and optional arms with rounded strokes to preserve clear appendages; retained the blank face in the sources.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '596b45cf-ebbb-4b9e-8b3b-4920f3f23506'
SOURCE_PATH = 'pictographic-primitives/apps/android_596b45cf-ebbb-4b9e-8b3b-4920f3f23506.svg'
SOURCE_ICON_IDS = ('596b45cf-ebbb-4b9e-8b3b-4920f3f23506', '5a895be7-0613-57bb-9e1f-038063cbd8b8', 'c737ad22-037b-47d7-883f-17a8b36a58e5')
SOURCE_PATHS = ('pictographic-primitives/apps/android_596b45cf-ebbb-4b9e-8b3b-4920f3f23506.svg', 'pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg', 'pictographic-primitives/apps/android_c737ad22-037b-47d7-883f-17a8b36a58e5.svg')
AUTHOR = 'gpt-6'


class AndroidMascotWithoutArms(Solo48):
    icon_id = 'android-mascot-without-arms'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('android', 'mascot', 'without', 'arms', 'sub icon')

    def build(self) -> None:
        axis = 24
        left, right, dome_y = 9, 39, 18
        self.add_arc("dome-left-low",(left,dome_y),(15,10),radius_x=15,radius_y=10)
        self.add_arc("dome-left-high",(15,10),(axis,8),radius_x=15,radius_y=10)
        self.add_arc("dome-right-high",(axis,8),(33,10),radius_x=15,radius_y=10)
        self.add_arc("dome-right-low",(33,10),(right,dome_y),radius_x=15,radius_y=10)
        self.add_line("right-wall",(right,dome_y),(right,34))
        self.add_arc("lower-right",(right,34),(35,38),radius_x=4)
        self.add_line("bottom-right",(35,38),(32,38))
        self.add_line("bottom-mid",(32,38),(16,38))
        self.add_line("bottom-left",(16,38),(13,38))
        self.add_arc("lower-left",(13,38),(left,34),radius_x=4)
        self.add_line("left-wall",(left,34),(left,dome_y))
        self.add_contour("body","dome-left-low","dome-left-high","dome-right-high","dome-right-low","right-wall","lower-right","bottom-right","bottom-mid","bottom-left","lower-left","left-wall",closed=True)
        self.add_line("head-seam",(left,dome_y),(right,dome_y))
        self.relate("connect","body","head-seam")
        for side,x in [("left",16),("right",32)]:
            self.add_line(f"leg-{side}",(x,38),(x,44))
            self.relate("connect","body",f"leg-{side}")
        # Antennae join exact Pythagorean points on the circular dome, which is
        # split below at those owning attachment nodes rather than near-touching it.

        for side,x,dx in [("left",15,-7),("right",33,7)]:
            self.add_line(f"antenna-{side}",(x,10),(x+dx,4))
            self.relate("connect","body",f"antenna-{side}")


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('c737ad22-037b-47d7-883f-17a8b36a58e5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/android_c737ad22-037b-47d7-883f-17a8b36a58e5.svg')]
