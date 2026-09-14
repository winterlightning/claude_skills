"""A minimal bicycle with plain wheels, an open frame and a handlebar turned back toward the rider. HRECT_L ink (6,6)-(42,42). Lucide bike informed equal circular wheels; all three identical source references are retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ce17d6f-0a53-4eaa-b433-061d444307dc'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'
SOURCE_REFERENCES = (('6ce17d6f-0a53-4eaa-b433-061d444307dc', 'pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'), ('809ac450-efd8-4c1a-94b3-ed96c86e92df', 'pictographic-primitives/transportation/bicycle_809ac450-efd8-4c1a-94b3-ed96c86e92df.svg'), ('c94a3698-f47d-459c-afbc-fc5e64f7a783', 'pictographic-primitives/transportation/bicycle_c94a3698-f47d-459c-afbc-fc5e64f7a783.svg'))
AUTHOR = 'gpt-6'

class MinimalBicycle(Solo48):
    icon_id = 'minimal-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'cycling', 'simple', 'pedal', 'transport', 'two wheels', 'ride')

    def build(self) -> None:
        # Identical wheels share radius and baseline; attachments are exact top extrema.
        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-right',(x,26),(x,40),radius_x=7)
            self.add_arc(side+'-left',(x,40),(x,26),radius_x=7)
            self.add_contour(side+'-wheel',side+'-right',side+'-left',closed=True)
        self.add_polyline('frame',(11,26),(19,16),(31,16))
        self.add_polyline('seat',(8,8),(16,8),(19,16))
        self.relate('connect','frame','rear-wheel')
        self.relate('connect','seat','frame')

        self.add_polyline('fork',(37,26),(31,16),(29,8),(25,8))
        self.relate('connect','fork','front-wheel')
        self.relate('connect','fork','frame')
