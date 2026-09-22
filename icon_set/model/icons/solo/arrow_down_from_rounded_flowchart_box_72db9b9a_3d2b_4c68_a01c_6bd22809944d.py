"""Arrow Down from Rounded Flowchart Box. Square envelope; vertically symmetric flowchart node and its attached outbound connector form one diagram subject, not a floating modifier badge. Rounded box owns four equal corners and splits its receiving edge at the genuine shaft junction. No details omitted.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '72db9b9a-3d2b-4c68-a01c-6bd22809944d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram fall down_72db9b9a-3d2b-4c68-a01c-6bd22809944d.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-down-from-rounded-flowchart-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Flowchart Downward Arrow',)
    keywords = ('arrow', 'flowchart', 'box', 'down', 'diagram', 'connector', 'process')

    def build(self):
        left,right,top,bottom,radius = 6,42,6,22,4
        join=(24,bottom)
        self.add_line('box-top',(10,top),(38,top))
        self.add_arc('box-tr',(38,top),(right,10),radius_x=radius)
        self.add_line('box-right',(right,10),(right,18))
        self.add_arc('box-br',(right,18),(38,bottom),radius_x=radius)
        self.add_line('box-bottom-right',(38,bottom),join)
        self.add_line('box-bottom-left',join,(10,bottom))
        self.add_arc('box-bl',(10,bottom),(left,18),radius_x=radius)
        self.add_line('box-left',(left,18),(left,10))
        self.add_arc('box-tl',(left,10),(10,top),radius_x=radius)
        self.add_contour('box','box-top','box-tr','box-right','box-br','box-bottom-right','box-bottom-left','box-bl','box-left','box-tl',closed=True)
        tip=(24,42)
        self.add_line('shaft',join,tip)
        self.add_polyline('head',(16,34),tip,(32,34))
        self.relate('connect','box','shaft')
        self.relate('connect','shaft','head')
