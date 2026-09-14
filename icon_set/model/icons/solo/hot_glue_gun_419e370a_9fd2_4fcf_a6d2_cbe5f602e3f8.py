"""A glue gun with nozzle, trigger, rear glue stick and a short curved glue trail; surface details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '419e370a-9fd2-4fcf-a6d2-cbe5f602e3f8'
SOURCE_PATH = 'pictographic-primitives/tools/tools glue gun_419e370a-9fd2-4fcf-a6d2-cbe5f602e3f8.svg'
AUTHOR = 'gpt-6'

class HotGlueGun(Solo48):
    icon_id = 'hot-glue-gun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('glue gun', 'hot glue', 'glue', 'adhesive', 'craft', 'diy', 'nozzle', 'tool')

    def build(self) -> None:
        self.add_polyline('body',(6,30),(12,22),(26,6),(34,10),(30,18),(42,26))
        self.add_polyline('underside',(6,30),(14,30),(24,22),(30,34),(34,24))
        self.relate('connect','body','underside')
        self.add_line('glue-stick',(30,8),(34,6))
        self.relate('connect','glue-stick','body')
        self.add_arc('glue-left',(6,40),(14,40),radius_x=4,radius_y=2,sweep=False)
        self.add_arc('glue-right',(14,40),(22,40),radius_x=4,radius_y=2)
        self.add_contour('glue','glue-left','glue-right')
