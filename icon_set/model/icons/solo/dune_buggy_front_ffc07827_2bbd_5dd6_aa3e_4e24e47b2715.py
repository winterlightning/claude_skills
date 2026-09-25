"""A head-on buggy with a trapezoid roll cage, winged body and tall outboard tyres. Square envelope supports the exposed suspension. Lucide car-front informed mirrored construction; the small hub is reduced to the suspension junction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffc07827-2bbd-5dd6-aa3e-4e24e47b2715'
SOURCE_PATH = 'pictographic-primitives/transportation/car_ffc07827-2bbd-5dd6-aa3e-4e24e47b2715.svg'
SOURCE_REFERENCES = (('ffc07827-2bbd-5dd6-aa3e-4e24e47b2715', 'pictographic-primitives/transportation/car_ffc07827-2bbd-5dd6-aa3e-4e24e47b2715.svg'),)
AUTHOR = 'gpt-6'

class DuneBuggyFront(Solo48):
    icon_id = 'dune-buggy-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('buggy', 'dune buggy', 'off-road', 'atv', 'front', 'vehicle', 'offroad', 'utv')

    def build(self) -> None:
        self.add_polyline('body',(10,26),(6,18),(14,18),(34,18),(42,18),(38,26),(24,34),(10,26),closed=True)
        self.add_polyline('cage',(14,18),(18,6),(30,6),(34,18))
        self.relate('connect','cage','body')
        for name,x in [('left',10),('right',38)]:
            self.add_arc(name+'-top-a',(x,26),(x+4,30),radius_x=4)
            self.add_line(name+'-right',(x+4,30),(x+4,38))
            self.add_arc(name+'-bottom',(x+4,38),(x-4,38),radius_x=4)
            self.add_line(name+'-left',(x-4,38),(x-4,30))
            self.add_arc(name+'-top-b',(x-4,30),(x,26),radius_x=4)
            self.add_contour(name+'-tyre',name+'-top-a',name+'-right',name+'-bottom',name+'-left',name+'-top-b',closed=True)
            self.relate('connect','body',name+'-tyre')
