"""Traffic police officer; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37ab5a7a-3b36-4e23-875f-657b67943fc3'
SOURCE_PATH = 'pictographic-primitives/transportation/police_37ab5a7a-3b36-4e23-875f-657b67943fc3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '37ab5a7a-3b36-4e23-875f-657b67943fc3', 'SOURCE_PATH': 'pictographic-primitives/transportation/police_37ab5a7a-3b36-4e23-875f-657b67943fc3.svg', 'AUTHOR': 'gpt-6'}]

class TrafficPoliceOfficer(Solo48):
    icon_id = 'traffic-police-officer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
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
        self.add_line('upper-arm',(22,32),(10,26))
        self.add_arc('raised-elbow',(10,26),(6,18),radius_x=10)
        self.add_line('raised-hand',(6,18),(6,12))
        self.add_contour('raised-arm','upper-arm','raised-elbow','raised-hand')
        self.relate('connect','collar','raised-arm')
        self.relate('connect','left-side','raised-arm')
