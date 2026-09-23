from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f27e9ceb-3471-4f88-9ba7-afea584d2ef1'
SOURCE_PATH = 'icon_set/work/todo-references/message bubble person_f27e9ceb-3471-4f88-9ba7-afea584d2ef1.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A rectangular speech bubble containing a small person portrait.'
CONSTRUCTION_PLAN = 'Rounded enclosure includes a lower-left tail. A circular head and shared-axis elliptical shoulders follow human_ref/user.svg with exactly four ink units of detached clearance.'
KEYSHAPE_CENTERLINE_BOUNDS = [8, 4, 40, 44]

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def rounded_rect(icon,name,left,top,right,bottom,r=4,split_y=None):
    points=[(left+r,top),(right-r,top),(right,top+r)]
    if split_y is not None: points.append((right,split_y))
    points += [(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r)]
    if split_y is not None: points.append((left,split_y))
    points += [(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%len(points)];n=f'{name}-{i}';members.append(n)
        if start[0]!=end[0] and start[1]!=end[1]: icon.add_arc(n,start,end,radius_x=r)
        else:icon.add_line(n,start,end)
    icon.add_contour(name,*members,closed=True)

class Drawing(Solo48):
    icon_id = 'message-bubble-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('message', 'bubble', 'person')

    def build(self):
        self.add_line('top',(12,4),(36,4))
        self.add_arc('top-right',(36,4),(40,8),radius_x=4)
        self.add_line('right',(40,8),(40,34))
        self.add_arc('bottom-right',(40,34),(36,38),radius_x=4)
        tail_nodes=[(36,38),(24,38),(16,44),(16,38),(12,38)]
        for i,(start,end) in enumerate(zip(tail_nodes,tail_nodes[1:]),1):
            self.add_line(f'tail-{i}',start,end)
        self.add_arc('bottom-left',(12,38),(8,34),radius_x=4)
        self.add_line('left',(8,34),(8,8))
        self.add_arc('top-left',(8,8),(12,4),radius_x=4)
        self.add_contour('bubble','top','top-right','right','bottom-right',*[f'tail-{i}' for i in range(1,5)],'bottom-left','left','top-left',closed=True)
        circle(self,'head',24,16,3)
        self.add_arc('shoulders',(17,29),(31,29),radius_x=7,radius_y=2)
        # Head bottom 19; shoulders apex 27 => 8 centreline / 4 ink gap.

HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
