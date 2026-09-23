"""An arched gravestone with a cross stands on a rectangular plinth.
No useful exact Lucide match used; semicircular arch and shared cross junction built from elementary geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49acece9-c782-56a9-b119-aa74bb42774e'
SOURCE_PATH = 'icon_set/work/todo-references/grave_49acece9-c782-56a9-b119-aa74bb42774e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'grave'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('grave',)
    def build(self):

        # Plan: symmetric arch and plinth around x=24; cross has one shared center.
        # VRECT_L visible extrema (6,2)-(42,46), centerlines (8,4)-(40,44).
        self.add_line('stone-left',(10,36),(10,18))
        self.add_arc('stone-arch',(10,18),(38,18),radius_x=14)
        self.add_line('stone-right',(38,18),(38,36))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_polyline('plinth',(8,36),(40,36),(40,44),(8,44),closed=True)
        self.relate('connect','stone','plinth')
        center=(24,20)
        for name,point in [('top',(24,13)),('bottom',(24,28)),('left',(20,20)),('right',(28,20))]:
            self.add_line('cross-'+name,center,point)
        self.relate('connect','cross-top','cross-bottom','cross-left','cross-right')
