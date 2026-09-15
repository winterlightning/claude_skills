'Down navigation: equal chevrons with consistent spacing; the top retains its closed arrow face.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8db0a809-08d9-4893-84fd-28f93e9891b3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation arrows down 1_8db0a809-08d9-4893-84fd-28f93e9891b3.svg'
AUTHOR = 'gpt-6'

class NavigationArrowsDown1(Solo48):
    icon_id = 'navigation-arrows-down-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'down', 'interface-essential')

    def build(self):
        # Down navigation: equal chevrons with consistent spacing; the top retains its closed arrow face.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('top',(8,4),(40,4),(24,18),(8,4))
        p('middle',(8,17),(24,31),(40,17))
        p('bottom',(8,30),(24,44),(40,30))
