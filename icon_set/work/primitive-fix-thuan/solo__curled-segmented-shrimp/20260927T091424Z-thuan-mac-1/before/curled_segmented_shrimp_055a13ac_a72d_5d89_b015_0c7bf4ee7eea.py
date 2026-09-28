"""Curved Seafood Shrimp."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '055a13ac-a72d-5d89-b015-0c7bf4ee7eea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/shrimp_055a13ac-a72d-5d89-b015-0c7bf4ee7eea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curled-segmented-shrimp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('shrimp', 'prawn', 'seafood', 'shellfish', 'tail', 'segment', 'food')

    def build(self):
        # Plan: Curled shrimp body with two broad shell seams and a small open tail fork. Lucide shrimp coherent body curve; fine divisions and antenna omitted. Envelope (6,6)-(42,42).
        self.add_bezier('outer',(6,16),((6,9),(14,6),(24,6)),((35,6),(42,14),(42,24)),((42,35),(34,42),(24,42)))
        self.add_polyline('tail',(24,42),(14,42),(18,34),(12,28))
        self.add_bezier('inner',(12,28),((18,32),(27,31),(28,26)),((29,21),(26,18),(20,18)),((13,18),(10,19),(6,16)))
        for a,b in (('outer','tail'),('tail','inner'),('inner','outer')):self.relate('connect',a,b)
        self.add_line('segment-a',(24,6),(20,18));self.relate('connect','segment-a','outer');self.relate('connect','segment-a','inner')
        self.add_line('segment-b',(42,24),(28,26));self.relate('connect','segment-b','outer');self.relate('connect','segment-b','inner')
