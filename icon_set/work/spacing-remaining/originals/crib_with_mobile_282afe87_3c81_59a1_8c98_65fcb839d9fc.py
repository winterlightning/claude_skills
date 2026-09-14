'Crib mobile: equal toy spacing and a regular crib rail, with clear gaps around the suspended toys.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '282afe87-3c81-59a1-8c98-65fcb839d9fc'
SOURCE_PATH = 'pictographic-primitives/babies/baby care cot mobile crib_282afe87-3c81-59a1-8c98-65fcb839d9fc.svg'
AUTHOR = 'gpt-6'


class CribWithMobile(Solo48):
    icon_id = 'crib-with-mobile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('crib', 'with', 'mobile', 'baby', 'nursery', 'toy')

    def build(self):
        # Crib mobile: equal toy spacing and a regular crib rail, with clear gaps around the suspended toys.
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

        p('crib',(6,42),(6,30),(42,30),(42,42))
        l('rail',(6,38),(42,38))
        link('connect','rail','crib')
        for x in (18,30):
            l(f'slat-{x}',(x,30),(x,38))
            link('connect',f'slat-{x}','crib')
            link('connect',f'slat-{x}','rail')
        p('mobile',(10,15),(10,6),(38,6),(38,15))
        l('middle',(24,6),(24,15))
        link('connect','mobile','middle')
        for x in (10,24,38):
            c(f'toy-{x}',x,18,3)
            link('connect',f'toy-{x}','middle' if x==24 else 'mobile')
