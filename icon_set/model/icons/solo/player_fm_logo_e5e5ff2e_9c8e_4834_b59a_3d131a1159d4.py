"""Concentric rings with a deliberate upper-right break in the inner ring; share center and set radii for clear spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5e5ff2e-9c8e-4834-b59a-3d131a1159d4'
SOURCE_PATH = 'pictographic-primitives/logos/playerfm logo_e5e5ff2e-9c8e-4834-b59a-3d131a1159d4.svg'
AUTHOR = 'gpt-6'

class PlayerFmLogo(Solo48):
    icon_id = 'player-fm-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('player-fm', 'podcast', 'rings', 'logo', 'brand', 'audio', 'player')

    def build(self):
        # Plan: Concentric rings with a deliberate upper-right break in the inner ring; share center and set radii for clear spacing.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        circle('outer',24,24,20)
        self.add_arc('inner',(24,13),(35,24),radius_x=11,large_arc=True,sweep=False)

