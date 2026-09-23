from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '37149c15-c3c1-44b7-b2c0-328541d9789b'
SOURCE_PATH = 'icon_set/work/todo-references/message bubble circle 1_37149c15-c3c1-44b7-b2c0-328541d9789b.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'An empty near-circular speech bubble with a lower-left tail.'
CONSTRUCTION_PLAN = 'Smooth oval lobes join a deliberate angular tail; preserve the reference empty interior and tail direction.'
KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]

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
    icon_id = 'message-bubble-circle-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('message', 'bubble', 'circle', '1')

    def build(self):
        self.add_bezier('top-right',(24,6),((34,6),(42,13),(42,22)))
        self.add_bezier('bottom-right',(42,22),((42,31),(34,38),(24,38)),((22,38),(20,38),(18,37)))
        self.add_line('tail-1',(18,37),(8,42))
        self.add_line('tail-2',(8,42),(11,33))
        self.add_bezier('left',(11,33),((8,30),(6,27),(6,22)),((6,13),(14,6),(24,6)))
        self.add_contour('bubble','top-right','bottom-right','tail-1','tail-2','left',closed=True)
