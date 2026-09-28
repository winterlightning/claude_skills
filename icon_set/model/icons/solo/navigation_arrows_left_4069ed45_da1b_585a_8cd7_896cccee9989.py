'Left navigation: regular chevrons with a broad front arrow and consistent diagonal gaps.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4069ed45-da1b-585a-8cd7-896cccee9989'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation arrows left_4069ed45-da1b-585a-8cd7-896cccee9989.svg'
AUTHOR = 'gpt-6'

class NavigationArrowsLeftInterfaceEssential(Solo48):
    icon_id = 'navigation-arrows-left-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'arrows', 'left', 'interface-essential')

    def build(self):
        # Left navigation: regular chevrons with a broad front arrow and consistent diagonal gaps.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('front',(18,8),(4,24),(18,40),(18,8))
        p('middle',(31,8),(17,24),(31,40))
        p('back',(44,8),(30,24),(44,40))
