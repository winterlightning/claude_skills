from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd9ee582-67bc-480d-85e3-0fdc2982679b'
SOURCE_PATH = 'icon_set/work/todo-references/monitoring bed_fd9ee582-67bc-480d-85e3-0fdc2982679b.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A reclining medical bed below a small heartbeat monitor.'
CONSTRUCTION_PLAN = 'Rounded reclining cushion on a pedestal, with an independent small screen at upper left. Preserve the two-part arrangement.'
KEYSHAPE_CENTERLINE_BOUNDS = [4, 8, 44, 40]

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def rounded_rect(icon,name,left,top,right,bottom,r=4,bottom_split=None):
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom)]
    if bottom_split is not None:points.append((bottom_split,bottom))
    points += [(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%len(points)];n=f'{name}-{i}';members.append(n)
        if start[0]!=end[0] and start[1]!=end[1]:icon.add_arc(n,start,end,radius_x=r)
        else:icon.add_line(n,start,end)
    icon.add_contour(name,*members,closed=True)

def monitor(icon):
    # Shared screen, central attachment and two base halves, drawn on SOLO48.
    rounded_rect(icon,'screen',6,6,42,34,bottom_split=24)
    icon.add_line('stand',(24,34),(24,42))
    icon.add_line('base-left',(16,42),(24,42))
    icon.add_line('base-right',(24,42),(32,42))
    icon.relate('connect','screen','stand')
    icon.relate('connect','stand','base-left','base-right')

class Drawing(Solo48):
    icon_id = 'monitoring-bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('monitoring', 'bed')

    def build(self):
        rounded_rect(self,'monitor',6,8,28,22,r=3)
        self.add_polyline('pulse',(6,16),(11,16),(14,12),(19,19),(22,15),(28,15))
        self.relate('connect','monitor','pulse')
        self.add_line('bed-top',(7,28),(31,28))
        self.add_bezier('bed-rise',(31,28),((35,28),(35,24),(36,21)))
        self.add_line('back-top',(36,21),(38,14))
        self.add_arc('back-cap',(38,14),(44,16),radius_x=4)
        self.add_line('back-bottom',(44,16),(39,30))
        self.add_bezier('bed-bottom',(39,30),((38,34),(34,34),(31,34)))
        self.add_line('bed-bottom-right',(31,34),(24,34))
        self.add_line('bed-bottom-left',(24,34),(7,34))
        self.add_arc('foot',(7,34),(7,28),radius_x=3)
        self.add_contour('bed','bed-top','bed-rise','back-top','back-cap','back-bottom','bed-bottom','bed-bottom-right','bed-bottom-left','foot',closed=True)
        self.add_line('pedestal',(24,34),(24,40))
        self.add_polyline('base',(16,40),(24,40),(32,40))
        self.relate('connect','bed','pedestal')
        self.relate('connect','pedestal','base')
