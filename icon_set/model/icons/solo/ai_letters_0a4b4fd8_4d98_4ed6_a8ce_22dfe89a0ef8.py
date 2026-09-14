"""Ai Letters. Retains the complete text and original case with monoline construction.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a4b4fd8-4d98-4ed6-a8ce-22dfe89a0ef8'
SOURCE_PATH = 'pictographic-primitives/symbol/Ai_0a4b4fd8-4d98-4ed6-a8ce-22dfe89a0ef8.svg'
AUTHOR = 'gpt-6'


class AiLetters(Solo48):
    icon_id = 'ai-letters'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('ai', 'letters', 'artificial-intelligence', 'illustrator', 'text', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_polyline('a-arch', (4, 40), (10, 24), (16, 8), (22, 24), (28, 40))
        self.add_line('a-bar', (10, 24), (22, 24))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_dot('i-dot', (44, 12))
        self.add_line('i-stem', (44, 22), (44, 40))
