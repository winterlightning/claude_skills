"""A thick outlined right-pointing chevron and an outlined lambda stand side by side, with two stacked outlined bars forming an equals sign at the right.

Plan: Chevron, lambda and equals sign; lambda branches share the centre node.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; joined diagonals and shared equals spacing.
Simplification: Outlined letter bands reduce to single strokes; every symbol retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40273791-5465-4a8f-a435-343b36ef5a3e'
SOURCE_PATH = 'pictographic-primitives/logos/haskell logo_40273791-5465-4a8f-a435-343b36ef5a3e.svg'
AUTHOR = 'gpt-6'


class HaskellLogo(Solo48):
    icon_id = 'haskell-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('haskell', 'lambda', 'functional', 'programming', 'logo', 'brand', 'language')

    def build(self):
        self.add_polyline('chevron',(4,8),(12,24),(4,40))
        self.add_polyline('lambda-spine',(16,8),(24,24),(32,40))
        self.add_line('lambda-leg',(16,40),(24,24))
        self.relate('connect','lambda-spine','lambda-leg')
        for i,y in enumerate((16, 26)):
            self.add_line(f'equals-{i}',(36,y),(44,y))
