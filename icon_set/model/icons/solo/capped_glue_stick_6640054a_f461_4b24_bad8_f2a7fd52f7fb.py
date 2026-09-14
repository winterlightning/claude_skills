"""Capped glue stick with label and twist base. VRECT_M (11,6)-(37,42) preserves tall tube proportions. Simple tangent circular corners; no useful exact Lucide match. Fine base grooves omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6640054a-f461-4b24-bad8-f2a7fd52f7fb'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/paper glue_6640054a-f461-4b24-bad8-f2a7fd52f7fb.svg'
AUTHOR = 'gpt-6'

class CappedGlueStick(Solo48):
    icon_id = 'capped-glue-stick'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('glue', 'stick', 'adhesive', 'paper', 'craft', 'stationery', 'cap')

    def build(self) -> None:
        """Opening repair: Rebalanced the tube with equal deeper cap/base bands and a centred label; fits the vertical keyshape."""
        left, right, top, bottom = (8, 40, 4, 44)
        self.add_polyline('body', (left, top), (right, top), (right, 12), (right, 36), (right, bottom), (left, bottom), (left, 36), (left, 12), closed=True)
        self.add_line('cap', (left, 12), (right, 12))
        self.add_line('base', (left, 36), (right, 36))
        self.relate('connect', 'cap', 'body')
        self.relate('connect', 'base', 'body')
        self.add_polyline('label', (20, 20), (28, 20), (28, 28), (20, 28), closed=True)
