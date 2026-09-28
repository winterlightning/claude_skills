"""A snow shelter with rounded shoulders, flat crown, central arched entrance and one block-course mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4e81c34-fd66-5e7e-9aeb-a50605352799'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/igloo_e4e81c34-fd66-5e7e-9aeb-a50605352799.svg'
AUTHOR = 'gpt-6'


class Igloo(Solo48):
    icon_id = 'igloo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('igloo', 'snow', 'arctic', 'shelter', 'dome', 'winter', 'eskimo', 'ice')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('wall-left',(4, 40),(4, 26))
        self.add_bezier('shoulder-left',(4, 26),*(((4, 17.43216908), (11.0539927, 9.90189012), (20, 8)),))
        self.add_line('crown',(20, 8),(28, 8))
        self.add_bezier('shoulder-right',(28, 8),*(((36.9460073, 9.90189012), (44, 17.43216908), (44, 26)),))
        self.add_line('right-foot-1',(44, 26),(44, 40))
        self.add_line('right-foot-2',(44, 40),(31, 40))
        self.add_line('right-foot-3',(31, 40),(31, 31))
        self.add_arc('entrance',(31, 31),(17, 31),radius_x=7,radius_y=7,large_arc=False,sweep=False)
        self.add_line('left-foot-1',(17, 31),(17, 40))
        self.add_line('left-foot-2',(17, 40),(4, 40))
        self.add_line('block-course',(4, 26),(9, 26))
        self.add_contour('right-foot',*('right-foot-1', 'right-foot-2', 'right-foot-3'),closed=False)
        self.add_contour('left-foot',*('left-foot-1', 'left-foot-2'),closed=False)
        self.relate('connect',*('wall-left', 'shoulder-left'))
        self.relate('connect',*('shoulder-left', 'crown'))
        self.relate('connect',*('crown', 'shoulder-right'))
        self.relate('connect',*('shoulder-right', 'right-foot'))
        self.relate('connect',*('right-foot', 'entrance'))
        self.relate('connect',*('entrance', 'left-foot'))
        self.relate('connect',*('left-foot', 'wall-left'))
        self.relate('connect',*('block-course', 'wall-left'))
        self.relate('connect',*('block-course', 'shoulder-left'))
