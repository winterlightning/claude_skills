"""Hearing-assistance ear with an inner fold, diagonal marks and a sound arc.
Plan: SQUARE balances the ear with the detached marks.
Reduction: Inner fold shortened to remain open; diagonal series retains two marks rather than three.
Construction: ear: continuous outer ear and a separate open inner fold. Asymmetry follows the ear profile.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "42121486-14f6-4035-afad-601034d0d354"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/disability hearing t_42121486-14f6-4035-afad-601034d0d354.svg'
AUTHOR = "gpt-6"


class HearingAssistanceSymbol(Solo48):
    icon_id = "hearing-assistance-symbol"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "accessibility/hearing"
    aliases = ("ear with sound arc", "hearing aid symbol")
    keywords = ("auditory", "ear", "sound", "accessibility")

    def build(self) -> None:
        self.add_bezier("ear-crown",(10,16),((14,11),(20,10),(26,11)),((32,12),(34,18),(34,24)))
        self.add_bezier("ear-lobe",(34,24),((34,30),(29,32),(27,37)),((26,41),(23,42),(20,42)))
        self.add_contour("ear","ear-crown","ear-lobe")
        self.add_bezier("inner-fold",(19,23),((21,19),(25,20),(25,24)))
        self.add_bezier("outer-sound-arc",(35,6),((39,8),(42,12),(42,16)))
        self.add_line("diagonal-lower",(6,34),(10,38))
        self.add_line("diagonal-upper",(12,28),(16,32))
