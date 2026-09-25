"""Sperm Cell: An irregular oval head joins a long undulating tail that bends first right and then left before curling outward. Generate this component alone; exclude Prohibition Frame.

Construction: A rounded head joins two alternating curved tail segments and an outward terminal; the irregular source head is regularized to a circle for the integer-grid construction.
Keyshape: VRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ff7e8050-8817-4660-b5a8-3ebce79568b0'
SOURCE_PATH = 'pictographic-primitives/state/slash sperm_ff7e8050-8817-4660-b5a8-3ebce79568b0.svg'
AUTHOR = 'gpt-6'


class SpermCell(Sub32):
    icon_id = 'sperm-cell'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sperm', 'cell', 'irregular', 'oval', 'head', 'joins', 'long', 'undulating')

    def build(self):
        self.add_arc('head-top',(4,8),(16,8),radius_x=6)
        self.add_arc('head-bottom',(16,8),(4,8),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_arc('tail-upper',(16,8),(16,20),radius_x=8,radius_y=6)
        self.add_arc('tail-lower',(16,20),(16,30),radius_x=5,sweep=False)
        self.add_line('tail-end',(16,30),(28,30))
        self.add_contour('tail','tail-upper','tail-lower','tail-end')
        self.relate('connect','head','tail')
