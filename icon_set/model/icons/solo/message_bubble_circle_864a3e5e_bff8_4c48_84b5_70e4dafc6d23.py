from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '864a3e5e-bff8-4c48-84b5-70e4dafc6d23'
SOURCE_PATH = 'icon_set/work/todo-references/message bubble circle_864a3e5e-bff8-4c48-84b5-70e4dafc6d23.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'An empty broad oval speech bubble with a lower-left tail.'
CONSTRUCTION_PLAN = 'Wider oval than circle 1, with tangent cardinal extrema and intentional lower-left tail asymmetry.'
KEYSHAPE_CENTERLINE_BOUNDS = [4, 8, 44, 40]

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
    icon_id = 'message-bubble-circle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('message', 'bubble', 'circle')

    def build(self):
        self.add_bezier('top-right',(24,8),((35,8),(44,14),(44,22)))
        self.add_bezier('bottom-right',(44,22),((44,30),(35,36),(24,36)),((22,36),(20,36),(18,35)))
        self.add_line('tail-1',(18,35),(8,40))
        self.add_line('tail-2',(8,40),(11,32))
        self.add_bezier('left',(11,32),((7,29),(4,26),(4,22)),((4,14),(13,8),(24,8)))
        self.add_contour('bubble','top-right','bottom-right','tail-1','tail-2','left',closed=True)
