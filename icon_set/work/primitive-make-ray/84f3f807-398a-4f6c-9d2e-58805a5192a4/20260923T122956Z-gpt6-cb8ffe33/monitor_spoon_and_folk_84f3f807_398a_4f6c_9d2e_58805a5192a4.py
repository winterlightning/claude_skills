from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '84f3f807-398a-4f6c-9d2e-58805a5192a4'
SOURCE_PATH = 'icon_set/work/todo-references/monitor spoon and folk_84f3f807-398a-4f6c-9d2e-58805a5192a4.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A monitor showing a round spoon and a pointed knife, as in the supplied reference.'
CONSTRUCTION_PLAN = 'Circular spoon bowl joins its handle; separate curved knife blade joins its stem. Preserve the pictured knife despite the filename folk.'
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
    icon_id = 'monitor-spoon-and-folk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('monitor', 'spoon', 'and', 'folk')

    def build(self):
        monitor(self)
        circle(self,'spoon-bowl',18,18,3)
        self.add_line('spoon-handle',(18,21),(18,25))
        self.relate('connect','spoon-bowl','spoon-handle')
        self.add_line('knife-upper',(30,15),(30,22))
        self.add_line('knife-handle',(30,22),(30,25))
        self.add_bezier('knife-blade',(30,15),((32,17),(33,20),(33,22)))
        self.add_line('knife-base',(33,22),(30,22))
        self.add_contour('knife','knife-upper','knife-handle')
        self.relate('connect','knife','knife-blade','knife-base')
