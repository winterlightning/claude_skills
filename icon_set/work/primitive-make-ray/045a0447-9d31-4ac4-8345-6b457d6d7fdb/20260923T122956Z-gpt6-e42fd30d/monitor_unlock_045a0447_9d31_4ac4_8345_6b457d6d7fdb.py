from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '045a0447-9d31-4ac4-8345-6b457d6d7fdb'
SOURCE_PATH = 'icon_set/work/todo-references/monitor unlock_045a0447-9d31-4ac4-8345-6b457d6d7fdb.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A monitor displaying an unlocked padlock.'
CONSTRUCTION_PLAN = 'Rounded lock body with an open circular shackle above it, inside the shared monitor.'
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
    icon_id = 'monitor-unlock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('monitor', 'unlock')

    def build(self):
        monitor(self)
        rounded_rect(self,'lock',17,21,31,29,r=2)
        self.add_line('shackle-stem',(20,21),(20,15))
        self.add_arc('shackle-arch',(20,15),(28,15),radius_x=4)
        self.add_contour('shackle','shackle-stem','shackle-arch')
        self.relate('connect','lock','shackle')
