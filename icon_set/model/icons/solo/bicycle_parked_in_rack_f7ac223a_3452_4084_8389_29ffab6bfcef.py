'A bicycle parked against a tall rack. Equal wheels share radius 8; source provides rack on right and bicycle geometry. Lucide bike contributes paired round wheels. HRECT_M spans 4,10 to 44,38. Frame is opened and pedals omitted; parking stand remains essential. The stand physically hides the right wheel half; exposed semicircle meets actual split stand nodes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f7ac223a-3452-4084-8389-29ffab6bfcef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bike parking 1_f7ac223a-3452-4084-8389-29ffab6bfcef.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'bicycle-parked-in-rack'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Bicycle Secured Beside a Parking Stand']
    keywords = ['bicycle', 'parking', 'stand', 'rack', 'wheels', 'frame', 'transport']
    def build(self):
        def path(name,start,steps,closed=False):
            point=start; members=[]
            for i,step in enumerate(steps):
                pid=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(pid,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(pid,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(pid)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True),((x,y-r),r,r,True)],True)
        circle('rear-wheel',12,30,8)
        path('front-wheel',(36,22),[((28,30),8,8,False),((36,38),8,8,False)])
        self.add_polyline('frame',(12,22),(20,10),(28,18),(36,22))
        self.add_line('saddle',(12,10),(20,10))
        self.relate('connect','saddle','frame')
        self.relate('connect','frame','rear-wheel')
        self.relate('connect','frame','front-wheel')
        path('rack',(36,38),[(36,22),(36,14),((40,10),4,4,True),(44,10),(44,38),(36,38)],True)
        self.relate('connect','rack','front-wheel')
        self.relate('connect','rack','frame')
