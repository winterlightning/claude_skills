"""Document Printer With Paper Sheet.

Symbol plan: Rounded printer between input and output paper, with clipped input corner. Lucide printer informs interrupted lower housing and projecting output sheet. No controls added.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b22f5f0-0fdf-465b-8951-1e23238ffe7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/printer_3b22f5f0-0fdf-465b-8951-1e23238ffe7b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-document-printer-with-two-paper-sections'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('document', 'printer', 'with', 'paper', 'sheet')

    def build(self):
        self.add_line('bottom-left',(14,34),(10,34));self.add_arc('corner-bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,22));self.add_arc('corner-tl',(6,22),(10,18),radius_x=4)
        self.run('top',(10,18),(14,18),(34,18),(38,18))
        self.add_arc('corner-tr',(38,18),(42,22),radius_x=4);self.add_line('right',(42,22),(42,30))
        self.add_arc('corner-br',(42,30),(38,34),radius_x=4);self.add_line('bottom-right',(38,34),(34,34))
        self.add_contour('housing','bottom-left','corner-bl','left','corner-tl','top-1','top-2','top-3','corner-tr','right','corner-br','bottom-right')
        self.add_polyline('input',(14,18),(14,6),(28,6),(34,12),(34,18))
        self.add_polyline('output',(14,34),(14,26),(34,26),(34,34),(34,42),(14,42),closed=True)
        self.relate('connect','housing','input');self.relate('connect','housing','output')

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f"{name}-{i}",a,b)
