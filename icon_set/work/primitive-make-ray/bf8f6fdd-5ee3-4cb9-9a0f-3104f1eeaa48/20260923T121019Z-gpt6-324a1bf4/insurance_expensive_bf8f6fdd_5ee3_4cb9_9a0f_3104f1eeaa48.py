from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48'
SOURCE_PATH = 'icon_set/work/todo-references/insurance expensive_bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A balance with a raised dollar coin and lower medical cross, indicating expensive insurance.'
CONSTRUCTION_PLAN = 'Use the same balance construction and reverse its tilt.'
# Keyshape extremes are fixed by SOLO48; all geometry authored directly at 48.

def circle(icon, name, cx, cy, radius):
    icon.add_arc(name+'-a', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
    icon.add_arc(name+'-b', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
    icon.add_contour(name, name+'-a', name+'-b', closed=True)

def rounded_rect(icon, name, left, top, right, bottom, radius=4):
    r=radius
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%8]; member=f'{name}-{i}'; members.append(member)
        if i%2: icon.add_arc(member,start,end,radius_x=r)
        else: icon.add_line(member,start,end)
    icon.add_contour(name,*members,closed=True)

class Drawing(Solo48):
    icon_id = 'insurance-expensive'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('insurance', 'expensive')

    def build(self):
        self.add_line('beam-left',(4,25),(24,30))
        self.add_line('beam-right',(24,30),(44,35))
        self.add_polyline('fulcrum',(16,40),(24,30),(32,40),closed=True)
        self.relate('connect','beam-left','beam-right','fulcrum')
        circle(self,'coin',13,17,9)
        self.add_bezier('dollar',(16,13),((8,11),(8,17),(13,17)),((19,17),(18,23),(10,21)))
        self.add_line('dollar-tick-top',(13,10),(13,13))
        self.add_line('dollar-tick-bottom',(13,21),(13,24))
        self.relate('connect','dollar','dollar-tick-top')
        self.relate('connect','dollar','dollar-tick-bottom')
        self.add_line('medical-horizontal',(28,20),(44,20))
        self.add_line('medical-vertical',(36,13),(36,27))
        self.relate('connect','medical-horizontal','medical-vertical')

KEYSHAPE_CENTERLINE_BOUNDS = [4, 8, 44, 40]
