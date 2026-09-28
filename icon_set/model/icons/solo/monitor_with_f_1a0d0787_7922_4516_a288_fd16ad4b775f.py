from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a0d0787-7922-4516-a288-fd16ad4b775f'
SOURCE_PATH = 'icon_set/work/todo-references/monitor with F_1a0d0787-7922-4516-a288-fd16ad4b775f.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A monitor displaying the uppercase letter F.'
CONSTRUCTION_PLAN = 'Shared monitor and a hand-authored F made from a split upright and two horizontal bars.'
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
    icon_id = 'monitor-with-f'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('monitor', 'with', 'F')

    def build(self):
        monitor(self)
        self.add_line('f-upper',(20,13),(20,21))
        self.add_line('f-lower',(20,21),(20,27))
        self.add_line('f-top',(20,13),(29,13))
        self.add_line('f-middle',(20,21),(27,21))
        self.relate('connect','f-upper','f-lower','f-middle')
        self.relate('connect','f-upper','f-top')
