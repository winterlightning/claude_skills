from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '42a2cdda-9bae-4c47-b68a-7075bb296796'
SOURCE_PATH = 'icon_set/work/todo-references/keyboard button direction_42a2cdda-9bae-4c47-b68a-7075bb296796.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'Three keyboard direction keys arranged with up above left and right.'
CONSTRUCTION_PLAN = 'Repeated rounded keys share dimensions and arrow lengths; bottom arrows mirror.'
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
    icon_id = 'keyboard-button-direction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('keyboard', 'button', 'direction')

    def build(self):
        rounded_rect(self,'up-key',16,6,32,22,3)
        for side in [-1,1]:
            cx=24+side*10
            rounded_rect(self,f'key-{side}',cx-8,26,cx+8,42,3)
            self.add_line(f'shaft-{side}',(cx-side*4,34),(cx+side*4,34))
            self.add_polyline(f'arrow-{side}',(cx,30),(cx+side*4,34),(cx,38))
            self.relate('connect',f'shaft-{side}',f'arrow-{side}')
        self.add_line('up-shaft',(24,18),(24,10))
        self.add_polyline('up-arrow',(20,14),(24,10),(28,14))
        self.relate('connect','up-shaft','up-arrow')

KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]
