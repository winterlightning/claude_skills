"""Angular clenched fist with two finger separations and a detached slanted thumb stroke. Source fist silhouette owns the pose; full_body_ref.png informs minimal round-ended anatomical strokes. Reduce three finger lines to two and outline thumb to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '933a9282-8c0b-4df8-ad7e-a679f6cef998'
SOURCE_PATH = 'pictographic-primitives/logos/riot games logo_933a9282-8c0b-4df8-ad7e-a679f6cef998.svg'
AUTHOR = 'gpt-6'

class RiotGamesLogo(Solo48):
    icon_id = 'riot-games-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('riot-games', 'fist', 'gaming', 'logo', 'brand', 'publisher', 'league')

    def build(self):
        # Plan: Angular clenched fist with two finger separations and a detached slanted thumb stroke. Source fist silhouette owns the pose; full_body_ref.png informs minimal round-ended anatomical strokes. Reduce three finger lines to two and outline thumb to one stroke.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('fist',(8,14),(30,4),(40,7),(38,32),(26,32),(24,30),(22,32),(18,32),(10,32),closed=True)
        for x,y,end in [(18,20,23),(26,16,22)]:
            self.add_line('finger-'+str(x),(x,y),(x,end))
        self.add_line('thumb',(24,42),(36,44))

