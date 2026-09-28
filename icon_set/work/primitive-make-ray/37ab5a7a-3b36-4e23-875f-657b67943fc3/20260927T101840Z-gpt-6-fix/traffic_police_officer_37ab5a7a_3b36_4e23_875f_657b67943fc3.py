"""Traffic police officer; independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '37ab5a7a-3b36-4e23-875f-657b67943fc3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__traffic-police-officer/20260927T101610Z-thuan-mac-1/reference/police_37ab5a7a-3b36-4e23-875f-657b67943fc3.svg'
AUTHOR = "gpt-6"
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '37ab5a7a-3b36-4e23-875f-657b67943fc3', 'SOURCE_PATH': 'pictographic-primitives/transportation/police_37ab5a7a-3b36-4e23-875f-657b67943fc3.svg', 'AUTHOR': 'gpt-6'}]

class TrafficPoliceOfficer(Solo48):
    icon_id = 'traffic-police-officer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('traffic', 'police', 'officer')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Head/cap over asymmetric raised-arm torso.
        self.add_polyline('cap',(20,14),(18,6),(38,6),(36,14),(20,14))
        self.add_arc('face',(36,14),(20,14),radius_x=8,sweep=True)
        self.relate('connect','cap','face')
        self.add_polyline('collar',(22,32),(28,38),(34,32))
        self.add_arc('right-shoulder',(34,32),(42,40),radius_x=8)
        self.add_line('right-side',(42,40),(42,42))
        self.add_contour('right-torso','right-shoulder','right-side')
        self.relate('connect','collar','right-torso')
        self.add_line('left-side',(22,32),(22,42))
        self.relate('connect','left-side','collar')
        # A continuous raised arm follows the broad curved silhouette of the source.
        self.add_bezier('raised-arm',(22,32),((11,26),(6,24),(6,12)))
        self.relate('connect','collar','raised-arm')
        self.relate('connect','left-side','raised-arm')
