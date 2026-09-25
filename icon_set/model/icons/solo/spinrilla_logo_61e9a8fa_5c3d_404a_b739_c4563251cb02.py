"""Opposite quarter-circle strokes rotate around one central ring. Preserve the rotational pairing; reduce broad outlined bands to single strokes and use required round caps."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '61e9a8fa-5c3d-404a-b739-c4563251cb02'
SOURCE_PATH = 'pictographic-primitives/logos/spinrilla logo_61e9a8fa-5c3d-404a-b739-c4563251cb02.svg'
AUTHOR = 'gpt-6'

class SpinrillaLogo(Solo48):
    icon_id = 'spinrilla-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('spinrilla', 'music', 'mixtapes', 'spin', 'logo', 'brand', 'hip-hop')

    def build(self):
        # Plan: Opposite quarter-circle strokes rotate around one central ring. Preserve the rotational pairing; reduce broad outlined bands to single strokes and use required round caps.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_arc('upper-left',(24,4),(4,24),radius_x=20,sweep=False)
        self.add_arc('lower-right',(24,44),(44,24),radius_x=20,sweep=False)
        circle('core',24,24,5)

