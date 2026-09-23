from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='c14f0462-1a4f-4fce-8591-b63fddf2fa6d'
SOURCE_PATH='icon_set/work/todo-references/truck medical_c14f0462-1a4f-4fce-8591-b63fddf2fa6d.svg'
AUTHOR='gpt-6'
PLAN='Medical truck with two wheels, cab window and outlined medical cross.'
CONSTRUCTION_REFERENCE='truck and ambulance: circular wheels, interrupted lower chassis and cab profile'

class Drawing(Solo48):
    icon_id='truck-medical'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
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
        # Main cargo body and cab intentionally differ in height.
        self.add_polyline('cargo',(4,34),(4,8),(28,8),(28,34))
        self.add_polyline('cab',(28,16),(36,16),(44,26),(44,34),(40,34))
        self.circle('wheel-left',12,36,4)
        self.circle('wheel-right',36,36,4)
        self.add_line('chassis',(16,36),(32,36))
        self.relate('connect','chassis','wheel-left','wheel-right')
        self.add_polyline('window',(34,18),(34,26),(44,26))
        self.relate('connect','window','cab')
        self.add_polyline('medical-cross',(13,15),(19,15),(19,20),(24,20),(24,26),(19,26),(19,31),(13,31),(13,26),(8,26),(8,20),(13,20),closed=True)
