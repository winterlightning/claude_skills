"""Staggered T and serif I monogram. Omit the overlapping square outlines to retain both identifying letters and their stepped placement with open spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ee2db23-9b8f-4227-94b9-8016ea62cb77'
SOURCE_PATH = 'pictographic-primitives/logos/tunein logo_2ee2db23-9b8f-4227-94b9-8016ea62cb77.svg'
AUTHOR = 'gpt-6'

class TuneinLogo(Solo48):
    icon_id = 'tunein-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('tunein', 'radio', 'streaming', 'ti', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: Staggered T and serif I monogram. Omit the overlapping square outlines to retain both identifying letters and their stepped placement with open spacing.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('t-top',(6,20),(12,20),(18,20));self.add_line('t-stem',(12,20),(12,42));self.relate('connect','t-top','t-stem')
        for n,y in [('top',6),('bottom',30)]:
            self.add_polyline('i-'+n,(30,y),(36,y),(42,y))
        self.add_line('i-stem',(36,6),(36,30));self.relate('connect','i-top','i-stem');self.relate('connect','i-bottom','i-stem')

