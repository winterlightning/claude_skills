from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '58b70697-62ea-4501-873d-8e51b3416d7a'
SOURCE_PATH = 'icon_set/work/todo-references/insurance cheap_58b70697-62ea-4501-873d-8e51b3416d7a.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A balance with a low dollar coin and raised medical cross, indicating cheap insurance.'
CONSTRUCTION_PLAN = 'Keep the tilted beam and triangle fulcrum; plus uses open equal-length strokes to reduce detail.'
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
    icon_id = 'insurance-cheap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('insurance', 'cheap')

    def build(self):
        # Shared beam pivot and currency centre; deliberate upward-right tilt.
        self.add_line('beam-left',(4,35),(24,30))
        self.add_line('beam-right',(24,30),(44,25))
        self.add_polyline('fulcrum',(16,40),(24,30),(32,40),closed=True)
        self.relate('connect','beam-left','beam-right','fulcrum')
        circle(self,'coin',13,21,9)
        self.add_bezier('dollar',(16,17),((8,15),(8,21),(13,21)),((19,21),(18,27),(10,25)))
        self.add_line('dollar-tick-top',(13,14),(13,17))
        self.add_line('dollar-tick-bottom',(13,25),(13,28))
        self.relate('connect','dollar','dollar-tick-top')
        self.relate('connect','dollar','dollar-tick-bottom')
        self.add_line('medical-horizontal',(28,15),(44,15))
        self.add_line('medical-vertical',(36,8),(36,22))
        self.relate('connect','medical-horizontal','medical-vertical')

KEYSHAPE_CENTERLINE_BOUNDS = [4, 8, 44, 40]
