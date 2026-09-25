"""Secure Hierarchy Diagram.

Plan: Lock root and three repeated square nodes; bounds (4,8)-(44,40). Keyhole omitted and branches angled outward to preserve clearance.
Construction reference: Lucide network: repeated nodes and orthogonal branch; rounded shackle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0d1f6d50-1124-5d7a-86ce-bde7860e127e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/lock hierarchy_0d1f6d50-1124-5d7a-86ce-bde7860e127e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'padlock-root-with-three-connected-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('secure', 'hierarchy', 'diagram')

    def build(self):
        path(self,'shackle',(20,16),('L',(20,12)),('A',4,4,True,(28,12)),('L',(28,16)))
        box(self,'lock',14,16,34,24,2,xs=(24,))
        for i,x in enumerate((8,24,40)):
         line(self,f'branch-{i}',(16+i*8,24),(x,32))
         poly(self,f'node-{i}',(x,32),(x+4,32),(x+4,40),(x-4,40),(x-4,32),(x,32))
        contacts(self)
