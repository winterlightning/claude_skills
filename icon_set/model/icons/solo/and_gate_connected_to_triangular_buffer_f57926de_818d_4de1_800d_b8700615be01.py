"""Logic AND Gate and Buffer.

Plan: D gate and triangular buffer joined by signal wire; bounds (4,8)-(44,40). Inputs share split gate wall nodes.
Construction reference: No useful exact Lucide match; geometric gate construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f57926de-818d-4de1-800d-b8700615be01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/xor_f57926de-818d-4de1-800d-b8700615be01.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'and-gate-connected-to-triangular-buffer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('logic', 'and', 'gate', 'and', 'buffer')

    def build(self):
        poly(self,'gate-left',(12,8),(12,16),(12,32),(12,40),(16,40))
        path(self,'gate-round',(16,40),('A',8,16,False,(24,24)),('A',8,16,False,(16,8)),('L',(12,8)))
        for y in (16,32): line(self,f'input-{y}',(4,y),(12,y))
        line(self,'wire',(24,24),(32,24))
        poly(self,'buffer',(32,12),(32,24),(32,36),(40,24),(32,12))
        line(self,'output',(40,24),(44,24))
        contacts(self)
