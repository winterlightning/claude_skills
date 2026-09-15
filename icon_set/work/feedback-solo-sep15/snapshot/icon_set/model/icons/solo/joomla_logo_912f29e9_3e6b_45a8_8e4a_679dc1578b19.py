"""Four curved links, each ending in a rounded ball at a corner, interlock at the centre in a square knot.

Plan: Four curved terminal links attach to a central diamond knot using shared nodes.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected flower-2: rotational repeat; tangent terminal curves.
Simplification: Interweaving bands reduce to a diamond knot with four curved links and round terminals.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '912f29e9-3e6b-45a8-8e4a-679dc1578b19'
SOURCE_PATH = 'pictographic-primitives/logos/joomla logo_912f29e9-3e6b-45a8-8e4a-679dc1578b19.svg'
AUTHOR = 'gpt-6'


class JoomlaLogo(Solo48):
    icon_id = 'joomla-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('joomla', 'cms', 'knot', 'logo', 'brand', 'web', 'open-source')

    def build(self):
        def rot(p,n):
         x,y=p[0]-24,p[1]-24
         for _ in range(n):x,y=-y,x
         return x+24,y+24
        self.add_polyline('knot',(24,14),(29,19),(34,24),(29,29),(24,34),(19,29),(14,24),(19,19),closed=True)
        for i in range(4):
         self.add_bezier(f'link{i}',rot((9,12),i),tuple(rot(p,i) for p in ((12,12),(16,16),(19,19))))
         self.add_arc(f'ball{i}a',rot((9,12),i),rot((9,6),i),radius_x=3)
         self.add_arc(f'ball{i}b',rot((9,6),i),rot((9,12),i),radius_x=3)
         self.add_contour(f'ball{i}',f'ball{i}a',f'ball{i}b',closed=True)
         self.relate('connect',f'ball{i}',f'link{i}')
         self.relate('connect','knot',f'link{i}')
