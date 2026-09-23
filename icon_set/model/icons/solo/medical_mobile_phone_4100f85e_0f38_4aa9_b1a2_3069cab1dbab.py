from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4100f85e-0f38-4aa9-b1a2-3069cab1dbab'
SOURCE_PATH = 'icon_set/work/todo-references/medical mobile phone_4100f85e-0f38-4aa9-b1a2-3069cab1dbab.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A medical smartphone displaying a plus above a lower panel.'
CONSTRUCTION_PLAN = 'Rounded portrait enclosure with split side-wall attachment nodes and a centred equal-arm medical plus.'
KEYSHAPE_CENTERLINE_BOUNDS = [10, 4, 38, 44]

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
    icon_id = 'medical-mobile-phone'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('medical', 'mobile', 'phone')

    def build(self):
        rounded_rect(self,'phone',10,4,38,44,split_y=34)
        self.add_line('panel-divider',(10,34),(38,34))
        self.relate('connect','phone','panel-divider')
        self.add_line('cross-horizontal',(19,20),(29,20))
        self.add_line('cross-vertical',(24,15),(24,25))
        self.relate('connect','cross-horizontal','cross-vertical')
