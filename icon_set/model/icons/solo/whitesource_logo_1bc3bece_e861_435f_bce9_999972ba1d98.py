"""Hard-hat dome with central ridge above an open toothed half gear. Preserve the helmet and lower cog rhythm; simplify the gear to one open stepped contour."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bc3bece-e861-435f-bce9-999972ba1d98'
SOURCE_PATH = 'pictographic-primitives/logos/whitesource logo_1bc3bece-e861-435f-bce9-999972ba1d98.svg'
AUTHOR = 'gpt-6'

class WhitesourceLogo(Solo48):
    icon_id = 'whitesource-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('whitesource', 'mend', 'security', 'hard-hat', 'gear', 'logo', 'brand')

    def build(self):
        # Plan: Hard-hat dome with central ridge above an open toothed half gear. Preserve the helmet and lower cog rhythm; simplify the gear to one open stepped contour.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_arc('dome-left',(10,20),(24,6),radius_x=14);self.add_arc('dome-right',(24,6),(38,20),radius_x=14)
        self.add_polyline('brim',(6,20),(10,20),(24,20),(38,20),(42,20))
        self.add_line('ridge',(24,6),(24,20))
        for a,b in [('dome-left','dome-right'),('dome-left','brim'),('dome-right','brim'),('dome-left','ridge'),('dome-right','ridge'),('brim','ridge')]:self.relate('connect',a,b)
        self.add_polyline('gear',(6,29),(12,29),(12,35),(18,35),(18,42),(30,42),(30,35),(36,35),(36,29),(42,29))

