"""A head-on bus with a large windscreen, two slanted lights and wheel stubs. VRECT_L ink (6,6)-(42,42). Lucide bus-front informed bilateral symmetry and simple face markings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6be3bbdd-720f-407c-af2d-59983752017d'
SOURCE_PATH = 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'
SOURCE_REFERENCES = (('6be3bbdd-720f-407c-af2d-59983752017d', 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'),)
AUTHOR = 'gpt-6'

class BusFront(Solo48):
    icon_id = 'bus-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('bus', 'front', 'public transport', 'coach', 'vehicle', 'transit', 'commute', 'head-on')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_line('body-top-0',(12, 4),(36, 4))
        self.add_arc('body-top-corner',(36, 4),(40, 8),radius_x=4)
        self.add_line('body-right-0',(40, 8),(40, 18))
        self.add_line('body-right-1',(40, 18),(40, 34))
        self.add_arc('body-right-corner',(40, 34),(36, 38),radius_x=4)
        self.add_line('body-bottom-0',(36, 38),(34, 38))
        self.add_line('body-bottom-1',(34, 38),(14, 38))
        self.add_line('body-bottom-2',(14, 38),(12, 38))
        self.add_arc('body-bottom-corner',(12, 38),(8, 34),radius_x=4)
        self.add_line('body-left-0',(8, 34),(8, 18))
        self.add_line('body-left-1',(8, 18),(8, 8))
        self.add_arc('body-left-corner',(8, 8),(12, 4),radius_x=4)
        self.add_contour('body','body-top-0','body-top-corner','body-right-0','body-right-1','body-right-corner','body-bottom-0','body-bottom-1','body-bottom-2','body-bottom-corner','body-left-0','body-left-1','body-left-corner',closed=True)

        self.add_line('windscreen',(8,18),(40,18))
        self.relate('connect','windscreen','body')
        for side,x in [('left',14),('right',34)]:
            self.add_line(side+'-wheel',(x,38),(x,44))
            self.relate('connect',side+'-wheel','body')
        self.add_line('left-light',(17,27),(18,28))
        self.add_line('right-light',(30,28),(31,27))
