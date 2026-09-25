"""Desktop Computer Monitor.

Symbol plan: Symmetric rounded screen with lower bezel; paired splayed stand legs share screen-bottom nodes. SQUARE centerline extremes 6,6,42,42.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a857f0fd-7c79-4e85-aa88-a49b91dc1b32'
SOURCE_PATH = 'pictographic-primitives/other/computer_a857f0fd-7c79-4e85-aa88-a49b91dc1b32.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'desktop-computer-monitor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('desktop', 'computer', 'monitor')

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
        axis = 24
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-1',(42, 10),(42, 24))
        self.add_line('right-2',(42, 24),(42, 28))
        self.add_arc('br',(42,28),(38,32),radius_x=4)
        self.add_line('bottom-1',(38, 32),(28, 32))
        self.add_line('bottom-2',(28, 32),(20, 32))
        self.add_line('bottom-3',(20, 32),(10, 32))
        self.add_arc('bl',(10,32),(6,28),radius_x=4)
        self.add_line('left-1',(6, 28),(6, 24))
        self.add_line('left-2',(6, 24),(6, 10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        # All outline members form one continuous rounded screen.
        self.add_contour('screen','top','tr','right-1','right-2','br','bottom-1','bottom-2','bottom-3','bl','left-1','left-2','tl',closed=True)
        self.add_line('bezel',(6,24),(42,24))
        self.relate('connect','bezel','screen')
        for side,x in [('left',20),('right',28)]:
            foot = axis + (x-axis)*2
            self.add_line('stand-'+side,(x,32),(foot,42))
            self.relate('connect','stand-'+side,'screen')
        self.add_polyline('base',(12,42),(16,42),(32,42),(36,42))
        for side in ('left','right'):
            self.relate('connect','stand-'+side,'base')
