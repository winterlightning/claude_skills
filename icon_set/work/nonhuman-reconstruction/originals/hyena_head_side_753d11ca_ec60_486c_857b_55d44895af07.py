'Hyena profile: preserve the angular ears, lowered muzzle and shaggy open neck; move the eye into the broad cheek.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '753d11ca-ec60-486c-857b-55d44895af07'
SOURCE_PATH = 'pictographic-primitives/animals/hyena head side_753d11ca-ec60-486c-857b-55d44895af07.svg'
AUTHOR = 'gpt-6'


class HyenaHeadProfile(Solo48):
    icon_id = 'hyena-head-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('hyena', 'head', 'profile', 'side', 'snout', 'ear', 'animal', 'wildlife')

    def build(self) -> None:
        self.add_polyline('ears',(4,16),(8,16),(4,8),(19,13),(23,8),(25,17))
        self.add_bezier('forehead',(25,17),((30,18),(33,22),(35,25)))
        self.add_line('snout-top',(35,25),(44,29))
        self.add_bezier('nose',(44,29),((44,32),(43,34),(40,36)))
        self.add_polyline('jaw',(40,36),(30,31),(33,40),(22,34))
        self.add_bezier('neck',(22,34),((17,33),(13,36),(10,40)))
        for a,b in (('ears','forehead'),('forehead','snout-top'),('snout-top','nose'),('nose','jaw'),('jaw','neck')):self.relate('connect',a,b)
        self.add_dot('eye',(21,24))
