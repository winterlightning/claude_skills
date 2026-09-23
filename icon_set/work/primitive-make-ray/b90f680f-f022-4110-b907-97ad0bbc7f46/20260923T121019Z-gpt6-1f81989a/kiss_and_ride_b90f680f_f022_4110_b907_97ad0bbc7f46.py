from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b90f680f-f022-4110-b907-97ad0bbc7f46'
SOURCE_PATH = 'icon_set/work/todo-references/kiss and ride_b90f680f-f022-4110-b907-97ad0bbc7f46.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'The letters K and R separated by a plus sign for kiss and ride.'
CONSTRUCTION_PLAN = 'Hand-authored letter strokes preserve the literal K+R sign; no useful Lucide match.'
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
    icon_id = 'kiss-and-ride'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('kiss', 'and', 'ride')

    def build(self):
        self.add_line('k-upper',(4,10),(4,24))
        self.add_line('k-lower',(4,24),(4,38))
        self.add_polyline('k-arms',(14,10),(4,24),(14,38))
        self.relate('connect','k-upper','k-lower','k-arms')
        self.add_line('plus-horizontal',(18,24),(26,24))
        self.add_line('plus-vertical',(22,20),(22,28))
        self.relate('connect','plus-horizontal','plus-vertical')
        self.add_line('r-upper',(35,10),(35,24))
        self.add_line('r-lower',(35,24),(35,38))
        self.add_line('r-top',(35,10),(37,10))
        self.add_arc('r-round',(37,10),(37,24),radius_x=7)
        self.add_line('r-middle',(37,24),(35,24))
        self.add_contour('r-bowl','r-top','r-round','r-middle')
        self.add_line('r-leg',(37,24),(44,38))
        self.relate('connect','r-upper','r-lower','r-bowl')
        self.relate('connect','r-bowl','r-leg')

KEYSHAPE_CENTERLINE_BOUNDS = [4, 10, 44, 38]
