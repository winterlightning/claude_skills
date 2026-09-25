"""Three Wax Crayons.

Symbol plan: Three identical crayons with 16-unit pitch and 8-unit bodies; wrapper dividers share wall nodes. Drop duplicate lower bands; preserve tips, count and wrapper.
Keyshape: HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29df9348-9709-494f-811c-0658f3b4be06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/tubes_29df9348-9709-494f-811c-0658f3b4be06.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-upright-wax-crayons-with-wrappers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('three', 'wax', 'crayons')

    def build(self):
        for i in range(3):
            x=8+i*16; l=x-4;r=x+4
            self.add_polyline(f'crayon-{i}',(l,16),(x,8),(r,16),(r,24),(r,40),(l,40),(l,24),closed=True)
            self.add_line(f'wrapper-{i}',(l,24),(r,24))
            self.relate('connect',f'crayon-{i}',f'wrapper-{i}')
