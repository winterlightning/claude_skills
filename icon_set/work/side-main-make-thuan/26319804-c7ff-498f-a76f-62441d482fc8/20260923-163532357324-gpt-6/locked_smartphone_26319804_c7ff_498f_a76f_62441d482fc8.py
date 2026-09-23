"""Locked Smartphone.

Symbol plan: Vertically symmetric phone encloses complete padlock with U shackle and lower bezel. Shared shackle/body nodes. VRECT_L centerline extremes (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '26319804-c7ff-498f-a76f-62441d482fc8'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone lock_26319804-c7ff-498f-a76f-62441d482fc8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'locked-smartphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('locked', 'smartphone')

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
        self.add_polyline('lock-body',(17,20),(20,20),(28,20),(31,20),(31,28),(17,28),closed=True)
        self.add_line('shackle-left',(20,20),(20,16))
        self.add_arc('shackle-top',(20,16),(28,16),radius_x=4)
        self.add_line('shackle-right',(28,16),(28,20))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')
