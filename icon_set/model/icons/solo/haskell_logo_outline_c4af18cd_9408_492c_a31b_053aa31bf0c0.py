"""A right-pointing chevron and a lambda drawn as single strokes lean side by side, followed by two short horizontal bars at the right like an equals sign.

Plan: Chevron, lambda and equals sign; lambda branches share the centre node.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; joined diagonals and shared equals spacing.
Simplification: Outlined letter bands reduce to single strokes; every symbol retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4af18cd-9408-492c-a31b-053aa31bf0c0'
SOURCE_PATH = 'pictographic-primitives/logos/haskell logo 1_c4af18cd-9408-492c-a31b-053aa31bf0c0.svg'
AUTHOR = 'gpt-6'


class HaskellLogoOutline(Solo48):
    icon_id = 'haskell-logo-outline'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('haskell', 'lambda', 'functional', 'programming', 'logo', 'brand', 'language')

    def build(self):
        self.add_polyline('chevron',(4,8),(12,24),(4,40))
        self.add_polyline('lambda-spine',(16,8),(24,24),(32,40))
        self.add_line('lambda-leg',(16,40),(24,24))
        self.relate('connect','lambda-spine','lambda-leg')
        for i,y in enumerate((18, 28)):
            self.add_line(f'equals-{i}',(36,y),(44,y))
