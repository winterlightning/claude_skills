"""Lao Kip Currency Symbol.

Symbol plan: Circular coin encloses a K with horizontal currency bar. Upper/lower branches mirror around y=24; stem and branches share one junction. Circle radius20 centered24,24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'abcbb9db-f5c8-434b-b898-b6580cddb672'
SOURCE_PATH = 'pictographic-primitives/other/circle kips_abcbb9db-f5c8-434b-b898-b6580cddb672.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lao-kip-currency-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('lao', 'kip', 'currency', 'symbol')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded_box(self, name, left, top, right, bottom, r):
        self.add_line(name+'-top', (left+r,top), (right-r,top))
        self.add_arc(name+'-tr', (right-r,top), (right,top+r), radius_x=r)
        self.add_line(name+'-right', (right,top+r), (right,bottom-r))
        self.add_arc(name+'-br', (right,bottom-r), (right-r,bottom), radius_x=r)
        self.add_line(name+'-bottom', (right-r,bottom), (left+r,bottom))
        self.add_arc(name+'-bl', (left+r,bottom), (left,bottom-r), radius_x=r)
        self.add_line(name+'-left', (left,bottom-r), (left,top+r))
        self.add_arc(name+'-tl', (left,top+r), (left+r,top), radius_x=r)
        self.add_contour(name, *(name+'-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

    def build(self):
        axis=24
        self.circle('coin',axis,axis,20)
        junction=(20,axis)
        self.add_polyline('stem',(20,14),junction,(20,34))
        self.add_polyline('arms',(30,16),junction,(30,32))
        self.add_polyline('crossbar',(14,axis),junction,(34,axis))
        self.relate('connect','stem','arms')
        self.relate('connect','stem','crossbar')
        self.relate('connect','arms','crossbar')
