"""Frozen Ice Pop Treat."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '274a4f5f-f0fe-47ff-bffb-de80580ae46a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream stick 2_274a4f5f-f0fe-47ff-bffb-de80580ae46a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'grooved-ice-pop'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice pop', 'popsicle', 'frozen', 'stick', 'dessert', 'groove', 'treat')

    def build(self):
        # Plan: Domed ice pop with a central groove and rounded wooden stick. Lucide ice-cream construction with shared stick junctions. Three grooves reduced to one. Envelope (10,4)-(38,44).
        self.add_bezier('dome',(10,18),((10,10),(16,4),(24,4)),((32,4),(38,10),(38,18)))
        self.add_polyline('body',(38,18),(38,34),(28,34),(20,34),(10,34),(10,18));self.relate('connect','body','dome')
        self.add_line('groove',(24,14),(24,24))
        self.add_line('stick-l',(20,34),(20,40));self.add_arc('stick-b',(20,40),(28,40),radius_x=4,sweep=False);self.add_line('stick-r',(28,40),(28,34))
        self.add_contour('stick','stick-l','stick-b','stick-r');self.relate('connect','stick','body')
