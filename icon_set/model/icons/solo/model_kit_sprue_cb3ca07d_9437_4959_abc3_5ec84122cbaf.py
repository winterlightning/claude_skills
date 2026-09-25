"""Model Kit Sprue.

Plan: Integral model sprue with a round part and a square part and connecting runners. Reduce three parts to two different shapes to keep gaps open. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb3ca07d-9437-4959-abc3-5ec84122cbaf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/model parts_cb3ca07d-9437-4959-abc3-5ec84122cbaf.svg'
AUTHOR = 'gpt-6'

class ModelKitSprue(Solo48):
    icon_id = 'model-kit-sprue'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('model', 'kit', 'sprue')

    def build(self):
        self.add_polyline('frame',(6,6),(17,6),(42,6),(42,30),(42,42),(30,42),(6,42),(6,17),closed=True)
        pts=[(17,14),(20,17),(17,20),(14,17),(17,14)]
        for i in range(4):self.add_arc(f'circle-{i}',pts[i],pts[i+1],radius_x=3)
        self.add_contour('round-part',*[f'circle-{i}' for i in range(4)],closed=True)
        self.add_polyline('square-part',(26,26),(34,26),(34,30),(34,34),(30,34),(26,34),closed=True)
        for name,a,b,part in [('top',(17,6),(17,14),'round-part'),('left',(6,17),(14,17),'round-part'),('right',(34,30),(42,30),'square-part'),('bottom',(30,34),(30,42),'square-part')]:
         self.add_line(name,a,b);self.relate('connect','frame',name);self.relate('connect',part,name)
