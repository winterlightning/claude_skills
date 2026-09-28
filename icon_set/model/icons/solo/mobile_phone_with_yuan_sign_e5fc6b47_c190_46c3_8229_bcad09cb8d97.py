"""Mobile Phone with Yuan Sign.

Symbol plan: Symmetric upright phone with lower bezel encloses a Y-shaped yuan symbol with the single bar shown in the reference. Shared fork/bar/stem junction. Extremes (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5fc6b47-c190-46c3-8229-bcad09cb8d97'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone yuan sign_e5fc6b47-c190-46c3-8229-bcad09cb8d97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mobile-phone-with-yuan-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('mobile', 'phone', 'with', 'yuan', 'sign')

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
        # Phone corners share radius four. Side walls expose the bezel nodes.
        self.add_line('top',(12,4),(36,4))
        self.add_arc('tr',(36,4),(40,8),radius_x=4)
        self.add_line('right-upper',(40,8),(40,36))
        self.add_line('right-lower',(40,36),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left-lower',(8,40),(8,36))
        self.add_line('left-upper',(8,36),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('phone','tr','right-upper','right-lower','br','bottom','bl','left-lower','left-upper','tl')
        self.relate('connect','top','phone')
        self.add_line('bezel',(8,36),(40,36))
        self.relate('connect','bezel','phone')
        junction=(24,22)
        self.add_polyline('fork',(17,13),junction,(31,13))
        self.add_line('stem',junction,(24,28))
        self.add_polyline('bar',(18,22),junction,(30,22))
        self.relate('connect','fork','stem')
        self.relate('connect','fork','bar')
        self.relate('connect','stem','bar')
