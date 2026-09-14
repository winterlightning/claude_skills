"""Rounded right-facing snowmobile with handlebars, track and front ski. No exact local Lucide match. Shared front ski geometry preserves the differing body and track silhouettes.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adb91652-44e2-42ba-9e88-08f20a810180'
SOURCE_PATH = 'pictographic-primitives/symbol/snow scooter_adb91652-44e2-42ba-9e88-08f20a810180.svg'
AUTHOR = 'gpt-6'


class Snowmobile(Solo48):
    icon_id = 'snowmobile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('snowmobile', 'snow', 'scooter', 'winter', 'vehicle', 'sled', 'ride', 'mountain')

    def build(self) -> None:

        self.add_polyline('handlebar',(20,8),(22,8),(28,18))

        self.add_line('rear',(4,30),(4,26))
        self.add_arc('rear-corner',(4,26),(8,22),radius_x=4)
        pts=[(8,22),(18,22),(20,18),(28,18),(34,20)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('upper-'+str(j),a,b)
        top=['rear','rear-corner']+['upper-'+str(j) for j in range(1,5)]

        self.add_arc('nose',(34,20),(34,30),radius_x=4,radius_y=5)
        pts=[(34,30),(32,30),(24,30),(20,30),(8,30),(4,30)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('bottom-'+str(j),a,b)
        self.add_contour('body',*top,'nose',*['bottom-'+str(j) for j in range(1,6)],closed=True)
        self.relate('connect','handlebar','body')
        self.add_line('ski-post',(32,30),(32,40))
        self.add_polyline('ski-flat',(26,40),(32,40),(38,40))
        self.add_arc('ski-curl',(38,40),(44,34),radius_x=6,sweep=False)
        self.relate('connect','ski-post','body')
        self.relate('connect','ski-post','ski-flat')
        self.relate('connect','ski-flat','ski-curl')

        self.add_arc('track',(4,30),(20,30),radius_x=8,radius_y=10,sweep=False)
        self.relate('connect','track','body')
