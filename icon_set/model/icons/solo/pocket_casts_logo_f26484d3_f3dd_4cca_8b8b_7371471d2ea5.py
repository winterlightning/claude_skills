"""Shared-center circular badge and open curl; reduce the innermost curl to a dot to preserve spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f26484d3-f3dd-4cca-8b8b-7371471d2ea5'
SOURCE_PATH = 'pictographic-primitives/logos/pocket casts logo_f26484d3-f3dd-4cca-8b8b-7371471d2ea5.svg'
AUTHOR = 'gpt-6'

class PocketCastsLogo(Solo48):
    icon_id = 'pocket-casts-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('pocket-casts', 'podcast', 'spiral', 'logo', 'brand', 'audio', 'player')

    def build(self):
        # Plan: Shared-center circular badge and open curl; reduce the innermost curl to a dot to preserve spacing.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        circle('badge',24,24,20)
        self.add_arc('curl',(35,24),(24,35),radius_x=11,large_arc=True,sweep=False)
        self.add_dot('core',(24,24))

