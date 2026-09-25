"""Concentric badge and small transmitter with mirrored mast and one broadcast pair. Omit second wave pair and mast bracing to open negative space; Lucide radio-tower informs repeated arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb368669-5c41-4bef-9da4-50aae9ede9e8'
SOURCE_PATH = 'pictographic-primitives/logos/overcast logo_eb368669-5c41-4bef-9da4-50aae9ede9e8.svg'
AUTHOR = 'gpt-6'

class OvercastLogo(Solo48):
    icon_id = 'overcast-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('overcast', 'podcast', 'radio-tower', 'broadcast', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: Concentric badge and small transmitter with mirrored mast and one broadcast pair. Omit second wave pair and mast bracing to open negative space; Lucide radio-tower informs repeated arcs.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        circle('badge',24,24,20)
        circle('transmitter',24,23,2)
        self.add_polyline('mast',(20,34),(24,25),(28,34))
        self.relate('connect','mast','transmitter')
        for side,sign in [('left',-1),('right',1)]:
            x=24+10*sign
            outer=24+11*sign
            self.add_bezier('wave-'+side,(x,19),((outer,21),(outer,24),(x,26)))

