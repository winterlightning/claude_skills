"""ffffound-logo: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59b2591b-f0db-40b6-a945-fa2be2dc52b3'
SOURCE_PATH = 'pictographic-primitives/logos/ffffound logo_59b2591b-f0db-40b6-a945-fa2be2dc52b3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FfffoundLogo(Solo48):
    icon_id = 'ffffound-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('ffffound', 'logo', 'logos')

    def build(self):
        # Plan: VRECT_L; matched tall lobes and smooth tapered sides; remove the tiny bottom stub.
        # Reference: Lucide heart: smooth paired lobes; retain the elongated logo shape.
        self.add_bezier('left-inner',(24,13),((24,8),(20,4),(16,4)))
        self.add_arc('left-lobe',(16,4),(8,14),radius_x=8,radius_y=10,sweep=False)
        self.add_bezier('left-side',(8,14),((8,21),(19,32),(24,44)))
        self.add_bezier('right-side',(24,44),((29,32),(40,21),(40,14)))
        self.add_arc('right-lobe',(40,14),(32,4),radius_x=8,radius_y=10,sweep=False)
        self.add_bezier('right-inner',(32,4),((28,4),(24,8),(24,13)))
        self.add_contour('outline','left-inner','left-lobe','left-side','right-side','right-lobe','right-inner',closed=True)
