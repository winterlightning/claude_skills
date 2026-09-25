from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf6cf58a-c4bd-55e5-b5c2-806c4c390311'
SOURCE_PATH = 'icon_set/work/todo-references/insurance card_bf6cf58a-c4bd-55e5-b5c2-806c4c390311.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A rounded insurance identification card containing a shield and a person.'
CONSTRUCTION_PLAN = 'Rounded enclosure uses equal tangent quarter-circle corners; human head and shoulders follow human_ref/user.svg.'
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
    icon_id = 'insurance-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('insurance', 'card')

    def build(self):
        rounded_rect(self,'card',4,8,44,40)
        self.add_polyline('shield',(13,19),(17,17),(21,19),(21,25),(17,30),(13,25),closed=True)
        circle(self,'head',32,19,2)
        # The emitted head bottom is 21 and shoulder top is 29: exact 4u ink gap.
        self.add_arc('shoulders',(29,31),(35,31),radius_x=3,radius_y=2,sweep=True)

KEYSHAPE_CENTERLINE_BOUNDS = [4, 8, 44, 40]
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BODY_INK_GAP = 4  # (29 - 21) - 4, in emitted geometry
