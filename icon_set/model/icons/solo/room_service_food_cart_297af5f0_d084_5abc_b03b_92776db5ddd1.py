"""Room Service Food Cart.
Plan: Cart owns tray, dome and right push handle; paired wheels share radius and baseline. Ink (2,6)-(46,42).
Construction reference: shopping-cart.
Reduction: Omit cloche knob; reduce wheel size and body depth to preserve clearances.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '297af5f0-d084-5abc-b03b-92776db5ddd1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/room service cart_297af5f0-d084-5abc-b03b-92776db5ddd1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'room-service-food-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hotels'
    aliases = ()
    keywords = ('room', 'service', 'food', 'cart')
    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                if i%2: self.add_arc(f'{name}-{i}',a,b,radius_x=r)
                else: self.add_line(f'{name}-{i}',a,b)
            self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

        self.add_polyline('tray',(4,20),(28,20),(36,20),(36,28),(4,28),closed=True)
        self.add_arc('dome',(4,20),(28,20),radius_x=12)
        self.relate('connect','dome','tray')
        self.add_line('handle-rise',(36,20),(36,12))
        self.add_arc('handle-turn',(36,12),(40,8),radius_x=4)
        self.add_line('handle-grip',(40,8),(44,8))
        self.add_contour('handle','handle-rise','handle-turn','handle-grip')
        self.relate('connect','handle','tray')
        for x in (12,30): circle(f'wheel-{x}',x,38,2)
