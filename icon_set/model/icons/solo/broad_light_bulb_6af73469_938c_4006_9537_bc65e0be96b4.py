'Light bulb: circular crown, equal shoulders and a base with a 10-unit interior height.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6af73469-938c-4006-9537-bc65e0be96b4'
SOURCE_PATH = 'pictographic-primitives/work/bulb 1_6af73469-938c-4006-9537-bc65e0be96b4.svg'
AUTHOR = 'gpt-6'


class BroadLightBulb(Solo48):
    icon_id = 'broad-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'light', 'lamp', 'idea', 'illumination', 'electricity')

    def build(self):
        # Light bulb: tangent circular crown and reverse-curved shoulders, with a balanced open base.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        a('crown',(8,20),(40,20),16)
        a('shoulder-r',(40,20),(32,28),8)
        a('neck-r',(32,28),(28,32),4,sweep=False)
        l('base-r',(28,32),(28,42))
        a('base-br',(28,42),(26,44),2)
        l('base-bottom',(26,44),(22,44))
        a('base-bl',(22,44),(20,42),2)
        l('base-l',(20,42),(20,32))
        a('neck-l',(20,32),(16,28),4,sweep=False)
        a('shoulder-l',(16,28),(8,20),8)
        self.add_contour('bulb','crown','shoulder-r','neck-r','base-r','base-br','base-bottom','base-bl','base-l','neck-l','shoulder-l',closed=True)
        l('seam',(20,34),(28,34))
        link('connect','bulb','seam')
