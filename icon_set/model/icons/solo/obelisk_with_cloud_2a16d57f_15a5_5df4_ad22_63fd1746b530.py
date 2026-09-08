"""A tapered obelisk with a pointed cap, baseline and detached cloud."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a16d57f-15a5-5df4-ad22-63fd1746b530'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/tower_2a16d57f-15a5-5df4-ad22-63fd1746b530.svg'
AUTHOR = 'gpt-6'


class ObeliskWithCloud(Solo48):
    icon_id = 'obelisk-with-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('obelisk', 'monument', 'memorial', 'tower', 'landmark', 'cloud', 'washington', 'pillar')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46); cloud balances tower at left.
        self.add_polyline('obelisk',(11,46),(14,9),(18,2),(22,9),(25,46))
        self.add_polyline('ground',(2,46),(11,46),(25,46),(46,46))
        self.relate('connect','ground','obelisk')
        
        self.add_arc('cloud-top',(32,10),(46,10),radius_x=7,sweep=True)
        self.add_arc('cloud-right',(46,10),(40,16),radius_x=6,sweep=True)
        self.add_line('cloud-base',(40,16),(32,16))
        self.add_arc('cloud-left',(32,16),(32,10),radius_x=3,sweep=True)
        self.add_contour('cloud','cloud-top','cloud-right','cloud-base','cloud-left',closed=True)
