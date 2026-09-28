"""A medical truck with a cross and two wheels.
Plan: HRECT_L fits the long cargo box and right-side cab.
Reduction: Window detail omitted and outlined cross reduced to centerlines. Lower body edges taper to wheel-top junctions.
Construction: Lucide truck: cargo/cab hierarchy, two circles and interrupted lower chassis.
Layout: Cross is centered in the cargo area; cab deliberately extends right. Both wheels retain equal radii."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='c14f0462-1a4f-4fce-8591-b63fddf2fa6d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/truck medical_c14f0462-1a4f-4fce-8591-b63fddf2fa6d.svg'
AUTHOR = "gpt-6"
PLAN='Medical truck with two wheels, right-side cab and a centerline medical cross.'
CONSTRUCTION_REFERENCE='truck and ambulance: circular wheels, interrupted lower chassis and cab profile'

class Drawing(Solo48):
    icon_id='truck-medical'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('truck', 'medical')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,left,top,right,bottom,r):
        p=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
           (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,start in enumerate(p):
            n=f'{name}-{i}';end=p[(i+1)%8]
            if i%2:self.add_arc(n,start,end,radius_x=r)
            else:self.add_line(n,start,end)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def cross(self,name,x,y,r,diagonal=False):
        ends=[(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def monitor(self,left=6,top=6,right=42,bottom=34,foot=42):
        # Matched quarter-round corners, bottom wall split at the stand junction.
        r=4;cx=(left+right)//2
        self.add_line('screen-top',(left+r,top),(right-r,top))
        self.add_arc('screen-tr',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('screen-right',(right,top+r),(right,bottom-r))
        self.add_arc('screen-br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('screen-bottom-r',(right-r,bottom),(cx,bottom))
        self.add_line('screen-bottom-l',(cx,bottom),(left+r,bottom))
        self.add_arc('screen-bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('screen-left',(left,bottom-r),(left,top+r))
        self.add_arc('screen-tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(cx,bottom),(cx,foot))
        self.add_polyline('foot',(cx-8,foot),(cx,foot),(cx+8,foot))
        self.relate('connect','stand','screen-bottom-r','screen-bottom-l')
        self.relate('connect','stand','foot')

    def browser(self):
        # Chrome separator joins explicitly split side walls; two tiny source
        # chrome dashes are omitted so the content keeps the available height.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-upper',(42,10),(42,14))
        self.add_line('right-lower',(42,14),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-lower',(6,38),(6,14))
        self.add_line('left-upper',(6,14),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('browser','top','tr','right-upper','right-lower','br','bottom','bl','left-lower','left-upper','tl',closed=True)
        self.add_line('chrome',(6,14),(42,14))
        self.relate('connect','chrome','left-upper','left-lower','right-upper','right-lower')

    def build(self):
        # One centerline medical cross preserves the medical mark at SOLO48.
        self.add_polyline('cargo',(12,32),(4,24),(4,8),(28,8),(28,16),(28,26))
        self.add_polyline('cab',(28,16),(36,16),(44,24),(44,28),(36,32))
        self.circle('wheel-left',12,36,4)
        self.circle('wheel-right',36,36,4)
        self.add_line('chassis',(16,36),(32,36))
        self.relate('connect','cargo','wheel-left')
        self.relate('connect','cab','wheel-right')
        self.relate('connect','cargo','cab')
        self.relate('connect','chassis','wheel-left');self.relate('connect','chassis','wheel-right')
        self.cross('medical-cross',16,20,4)
