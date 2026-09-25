"""Oxygen Text: A large uppercase O is followed at lower right by a smaller numeral 2, forming the text O₂. Generate this component alone; exclude Circle Frame.

Construction: A large oval O and smaller lowered 2 preserve the source subscript arrangement.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '937fbb98-3693-46f2-91da-e8ed80b0bdc3'
SOURCE_PATH = 'pictographic-primitives/state/circle oxi_937fbb98-3693-46f2-91da-e8ed80b0bdc3.svg'
AUTHOR = 'gpt-6'


class OxygenText(Sub32):
    icon_id = 'oxygen-text'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('oxygen', 'text', 'large', 'uppercase', 'o', 'followed', 'lower', 'right')

    def build(self):
        self.add_arc('o-top',(2,12),(16,12),radius_x=7,radius_y=8)
        self.add_arc('o-bottom',(16,12),(2,12),radius_x=7,radius_y=8)
        self.add_contour('o','o-top','o-bottom',closed=True)
        self.add_arc('two-hook',(24,16),(30,16),radius_x=3,radius_y=4)
        self.add_line('two-diagonal',(30,16),(24,28))
        self.add_line('two-base',(24,28),(30,28))
        self.add_contour('two','two-hook','two-diagonal','two-base')
