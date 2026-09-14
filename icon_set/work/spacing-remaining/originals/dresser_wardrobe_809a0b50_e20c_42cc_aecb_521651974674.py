'Wardrobe: symmetric doors and handles, with consistent clearance from the centre seam.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '809a0b50-e20c-42cc-aecb-521651974674'
SOURCE_PATH = 'icons-json/furnitures/dresser wardrobe_809a0b50-e20c-42cc-aecb-521651974674.json'
AUTHOR = 'gpt-6'

class DresserWardrobe(Solo48):
    icon_id = 'dresser-wardrobe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('dresser', 'wardrobe', 'furnitures')

    def build(self):
        # Wardrobe: symmetric doors and handles, with consistent clearance from the centre seam.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('cabinet',(6,38),(6,6),(42,6),(42,38),(6,38))
        l('seam',(24,6),(24,38))
        link('connect','seam','cabinet')
        for x in (15,33):
            l(f'handle-{x}',(x,20),(x,24))
        for x in (10,38):
            l(f'foot-{x}',(x,38),(x,42))
            link('connect',f'foot-{x}','cabinet')
