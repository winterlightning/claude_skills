"""Serif W with three top serif bars and two pointed lower vertices. Build the letter and serifs from shared junctions; omit the fine crossed central hairlines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '793906e6-107e-4799-9640-74fbddf9a406'
SOURCE_PATH = 'pictographic-primitives/logos/wikipedia logo_793906e6-107e-4799-9640-74fbddf9a406.svg'
AUTHOR = 'gpt-6'

class WikipediaLogo(Solo48):
    icon_id = 'wikipedia-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('wikipedia', 'encyclopedia', 'letter-w', 'wiki', 'logo', 'brand', 'knowledge')

    def build(self):
        # Plan: Serif W with three top serif bars and two pointed lower vertices. Build the letter and serifs from shared junctions; omit the fine crossed central hairlines.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_polyline('w',(8,8),(16,40),(24,8),(32,40),(40,8))
        for j,x in enumerate((8,24,40)):
            self.add_polyline('serif-'+str(j),(x-4,8),(x,8),(x+4,8));self.relate('connect','w','serif-'+str(j))

