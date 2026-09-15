"""A rounded four-lobed cross, like a quatrefoil with softly pinched sides, holds a ring at its centre.

Plan: Four matching rounded lobes rotate around a central ring.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected flower-2: repeated rounded lobes.
Simplification: Central ring reduced to fit broad negative space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1ec3ebc-af3e-4938-9bbc-35d4bd66a87a'
SOURCE_PATH = 'pictographic-primitives/logos/jeet logo_c1ec3ebc-af3e-4938-9bbc-35d4bd66a87a.svg'
AUTHOR = 'gpt-6'


class JeetLogo(Solo48):
    icon_id = 'jeet-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('jeet', 'grid', 'css', 'quatrefoil', 'logo', 'brand', 'framework')

    def build(self):
        def rot(p,n):
         x,y=p[0]-24,p[1]-24
         for _ in range(n):x,y=-y,x
         return x+24,y+24
        for i in range(4):
         self.add_bezier(f'q{i}',rot((24,6),i),tuple(rot(p,i) for p in ((34,6),(28,16),(34,16))),tuple(rot(p,i) for p in ((40,16),(42,18),(42,24))))
        self.add_contour('lobes',*[f'q{i}' for i in range(4)],closed=True)
        self.add_arc('r1',(27,24),(21,24),radius_x=3)
        self.add_arc('r2',(21,24),(27,24),radius_x=3)
        self.add_contour('ring','r1','r2',closed=True)
