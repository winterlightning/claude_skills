'Eye: balanced smooth almond-like envelope and a circular iris with generous clear space.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a73a3ea1-b1ee-5adb-a13b-215a290d268a'
SOURCE_PATH = 'icons-json/interface-essential/view_a73a3ea1-b1ee-5adb-a13b-215a290d268a.json'
AUTHOR = 'gpt-6'

class View(Solo48):
    icon_id = 'view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('view', 'interface-essential')

    def build(self):
        # Eye: balanced smooth almond-like envelope and a circular iris with generous clear space.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        a('upper',(4,24),(44,24),20,16)
        a('lower',(44,24),(4,24),20,16)
        self.add_contour('eye','upper','lower',closed=True)
        c('iris',24,24,7)
