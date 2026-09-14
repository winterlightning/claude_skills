'Upload arrow: centered arrowhead and shaft; detached dashes retain 8-unit spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1642e1b5-838a-47dc-b8bc-bf1bcffb0f3f'
SOURCE_PATH = 'icons-json/arrows/upload dash arrow_1642e1b5-838a-47dc-b8bc-bf1bcffb0f3f.json'
AUTHOR = 'gpt-6'

class UploadDashArrow(Solo48):
    icon_id = 'upload-dash-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'dash', 'arrow', 'arrows')

    def build(self):
        # Upload arrow: centered arrowhead and shaft; detached dashes retain 8-unit spacing.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('arrow',(16,34),(16,18),(8,18),(24,4),(40,18),(32,18),(32,34))
        for x in (16,32):
            l(f'dash-{x}',(x,42),(x,44))
