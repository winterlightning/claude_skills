"""Independent upright bar and large upper-right circle; preserve brand asymmetry. Reduce narrow bar outline to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5be08654-5325-4e0b-bfab-4d0a28ddb8dc'
SOURCE_PATH = 'pictographic-primitives/logos/patreon logo_5be08654-5325-4e0b-bfab-4d0a28ddb8dc.svg'
AUTHOR = 'gpt-6'

class PatreonLogo(Solo48):
    icon_id = 'patreon-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('patreon', 'creators', 'membership', 'logo', 'brand', 'crowdfunding', 'support')

    def build(self):
        # Plan: Independent upright bar and large upper-right circle; preserve brand asymmetry. Reduce narrow bar outline to one stroke.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_line('bar',(6,6),(6,42))
        circle('disc',29,19,13)

