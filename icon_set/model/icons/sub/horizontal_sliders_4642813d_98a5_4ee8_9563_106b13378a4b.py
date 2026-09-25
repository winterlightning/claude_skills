"""Horizontal Sliders: Two horizontal tracks each carry a circular knob, positioned left on the upper track and right on the lower one. Generate this component alone; exclude Rounded Square Frame.

Construction: Two horizontal slider tracks meet circular knobs at exact cardinal endpoints.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4642813d-98a5-4ee8-9563-106b13378a4b'
SOURCE_PATH = 'pictographic-primitives/state/square slider_4642813d-98a5-4ee8-9563-106b13378a4b.svg'
AUTHOR = 'gpt-6'


class HorizontalSliders(Sub32):
    icon_id = 'horizontal-sliders'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('horizontal', 'sliders', 'tracks', 'carry', 'circular', 'knob', 'positioned', 'left')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        for name,cx,y in (("upper",10,8),("lower",22,24)):
            circle(name+"-knob",cx,y,6)
            self.add_line(name+"-left",(2,y),(cx-6,y))
            self.add_line(name+"-right",(cx+6,y),(30,y))
            self.relate("connect",name+"-knob",name+"-left")
            self.relate("connect",name+"-knob",name+"-right")
