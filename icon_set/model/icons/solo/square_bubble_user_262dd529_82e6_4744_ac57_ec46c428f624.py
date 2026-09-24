"""A square speech bubble containing a user bust.
Plan: Rounded bubble with lower-left tail encloses circular head and symmetric shoulder arch; detached head/shoulder ink gap exactly four.
Construction: human_ref/user.svg: circular head and broad shoulder arch; message-square: integrated speech tail
Envelope: visible (4,4)-(44,44); centerlines (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '262dd529-82e6-4744-ac57-ec46c428f624'
SOURCE_PATH = 'icon_set/work/todo-references/square bubble user_262dd529-82e6-4744-ac57-ec46c428f624.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-bubble-user'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('square', 'bubble', 'user')

    def build(self):
        self.add_line('top',(10,6),(38,6))
        self.add_arc('upper-right',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,32))
        self.add_arc('lower-right',(42,32),(38,36),radius_x=4)
        tail_points=[(38,36),(24,36),(16,42),(16,36),(10,36)]
        for i in range(4):self.add_line(f'tail-{i+1}',tail_points[i],tail_points[i+1])
        self.add_arc('lower-left',(10,36),(6,32),radius_x=4)
        self.add_line('left',(6,32),(6,10))
        self.add_arc('upper-left',(6,10),(10,6),radius_x=4)
        self.add_contour('bubble','top','upper-right','right','lower-right',*(f'tail-{i}' for i in range(1,5)),'lower-left','left','upper-left',closed=True)
        self.circle('head',24,16,3)
        # Head lower centerline y19; shoulder apex y27. 27-19-4 = 4 ink units.
        self.add_arc('shoulders-left',(16,33),(24,27),radius_x=8,radius_y=6)
        self.add_arc('shoulders-right',(24,27),(32,33),radius_x=8,radius_y=6)
        self.add_contour('shoulders','shoulders-left','shoulders-right')

    def box(self,name,l=6,t=6,r=42,b=42,rad=4):
        mx,my=(l+r)//2,(t+b)//2
        pts=[(mx,t),(r-rad,t),(r,t+rad),(r,my),(r,b-rad),(r-rad,b),(mx,b),(l+rad,b),(l,b-rad),(l,my),(l,t+rad),(l+rad,t)]
        for i in range(12):
            a,z=pts[i],pts[(i+1)%12]
            if i in (1,4,7,10):self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(12)),closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def arrow(self,name,start,tip,a,b):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',a,tip,b)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')
