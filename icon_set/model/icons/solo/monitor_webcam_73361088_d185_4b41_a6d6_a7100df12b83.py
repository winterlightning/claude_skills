from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73361088-d185-4b41-a6d6-a7100df12b83'
SOURCE_PATH = 'icon_set/work/todo-references/monitor webcam_73361088-d185-4b41-a6d6-a7100df12b83.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A monitor with a central webcam interrupting the top edge.'
CONSTRUCTION_PLAN = 'Top border has symmetric gaps around the camera dot; paired sloping supports attach to a shared base.'
KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]

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
    icon_id = 'monitor-webcam-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ()
    keywords = ('monitor', 'webcam')

    def build(self):
        self.add_line('top-left',(16,6),(10,6))
        self.add_arc('corner-tl',(10,6),(6,10),radius_x=4,sweep=False)
        self.add_line('left',(6,10),(6,30))
        self.add_arc('corner-bl',(6,30),(10,34),radius_x=4,sweep=False)
        self.add_polyline('bottom',(10,34),(20,34),(28,34),(38,34))
        self.add_arc('corner-br',(38,34),(42,30),radius_x=4,sweep=False)
        self.add_line('right',(42,30),(42,10))
        self.add_arc('corner-tr',(42,10),(38,6),radius_x=4,sweep=False)
        self.add_line('top-right',(38,6),(32,6))
        self.add_contour('screen-left','top-left','corner-tl','left','corner-bl')
        self.add_contour('screen-right','corner-br','right','corner-tr','top-right')
        self.relate('connect','screen-left','bottom')
        self.relate('connect','screen-right','bottom')
        self.add_dot('webcam',(24,6))
        for side in [-1,1]:
            self.add_line(f'support-{side}',(24+side*4,34),(24+side*6,42))
            self.relate('connect',f'support-{side}','bottom')
        self.add_polyline('base',(14,42),(18,42),(30,42),(34,42))
        for side in [-1,1]:self.relate('connect','base',f'support-{side}')
