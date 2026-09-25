from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '675d2e83-bae0-46ca-b68a-04732a2c88a9'
SOURCE_PATH = 'pictographic-primitives/other/monitor shuttlecock_675d2e83-bae0-46ca-b68a-04732a2c88a9.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A monitor showing a diagonal badminton shuttlecock.'
CONSTRUCTION_PLAN = 'Shared monitor enclosure with a rounded shuttle base and three feather lobes; diagonal subject orientation retained.'
KEYSHAPE_CENTERLINE_BOUNDS = [8, 4, 40, 44]

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
    rounded_rect(icon,'screen',8,4,40,36,bottom_split=24)
    icon.add_line('stand',(24,36),(24,44))
    icon.add_line('base-left',(16,44),(24,44))
    icon.add_line('base-right',(24,44),(32,44))
    icon.relate('connect','screen','stand')
    icon.relate('connect','stand','base-left','base-right')

class Drawing(Solo48):
    icon_id = 'monitor-shuttlecock'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("combination", "other", "primitives-generate")
    aliases = ()
    keywords = ('monitor', 'shuttlecock')

    def build(self):
        monitor(self)
        # One open feather fan and rounded cork silhouette; omit overlapping feather loops.
        self.add_line('feather-fan-1',(17,23),(21,13))
        self.add_line('feather-fan-2',(21,13),(31,17))
        self.add_line('feather-fan-3',(31,17),(25,23))
        self.add_arc('cork',(25,23),(17,23),radius_x=4)
        self.add_contour('shuttle','feather-fan-1','feather-fan-2','feather-fan-3','cork',closed=True)
