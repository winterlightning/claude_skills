'Angry portrait: preserve the existing attached bust construction, with a round head, inward brows and a compact frown.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dafb63e7-5f8a-47d0-a53c-945b0a5d235d'
SOURCE_PATH = 'pictographic-primitives/symbol/angry person_dafb63e7-5f8a-47d0-a53c-945b0a5d235d.svg'
AUTHOR = 'gpt-6'


class AngryPerson(Solo48):
    icon_id = 'angry-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('angry', 'person', 'face', 'mad', 'emotion', 'frown', 'user', 'upset')

    def build(self) -> None:
        self.add_arc('head-top', (8,20), (40,20), radius_x=16, radius_y=16)
        self.add_arc('head-bottom', (40,20), (8,20), radius_x=16, radius_y=16)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)

        # Preserve the original continuous head-to-shoulder junction at (24,36).
        # The rounded human head and broad shoulders follow the shared human vocabulary.
        self.add_bezier('shoulders',(8,44),((12,38),(18,36),(24,36)),((30,36),(36,38),(40,44)))
        self.relate('connect','head','shoulders')
        self.add_line('brow-left',(18,15),(20,17));self.add_line('brow-right',(28,17),(30,15))
        self.add_arc('frown',(21,26),(27,26),radius_x=3,radius_y=1)
