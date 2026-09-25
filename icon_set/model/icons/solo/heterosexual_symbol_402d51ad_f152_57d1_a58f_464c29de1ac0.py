"""Interlocking Venus and Mars symbols. Lucide venus and transgender inform circle-stem junctions and the diagonal arrow. Both loops and the crossing lens are retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '402d51ad-f152-57d1-a58f-464c29de1ac0'
SOURCE_PATH = 'pictographic-primitives/users/gender hetero_402d51ad-f152-57d1-a58f-464c29de1ac0.svg'
AUTHOR = 'gpt-6'


class HeterosexualSymbol(Solo48):
    icon_id = 'heterosexual-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    aliases = ()
    keywords = ('heterosexual', 'gender', 'male', 'female', 'symbol', 'couple', 'venus', 'mars')

    def build(self) -> None:
        # Square extremes (6,6)-(42,42); r10 rings centered (16,21),(28,21).
        self.add_arc('outer-left-top',(22,13),(16,31),radius_x=10,large_arc=True,sweep=False)
        self.add_arc('outer-left-bottom',(16,31),(22,29),radius_x=10,sweep=False)
        self.add_arc('outer-right-bottom',(22,29),(34,13),radius_x=10,large_arc=True,sweep=False)
        self.add_arc('outer-right-top',(34,13),(22,13),radius_x=10,sweep=False)
        self.add_contour('linked-outline','outer-left-top','outer-left-bottom','outer-right-bottom','outer-right-top',closed=True)
        self.add_arc('lens-right',(22,13),(22,29),radius_x=10)
        self.add_arc('lens-left',(22,29),(22,13),radius_x=10)
        self.relate('connect','linked-outline','lens-right')
        self.relate('connect','linked-outline','lens-left')
        self.relate('connect','lens-right','lens-left')
        self.add_polyline('female-stem',(16,31),(16,40),(16,42))
        self.add_polyline('crossbar',(10,40),(16,40),(22,40))
        self.add_line('male-shaft',(34,13),(42,6))
        self.add_polyline('arrow',(34,6),(42,6),(42,14))
        self.relate('connect','linked-outline','female-stem')
        self.relate('connect','female-stem','crossbar')
        self.relate('connect','linked-outline','male-shaft')
        self.relate('connect','male-shaft','arrow')
