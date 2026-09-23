from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fdaa2690-f7c0-4893-81b1-967aecf80f4b'
SOURCE_PATH = 'icon_set/work/todo-references/laboratory sperm_fdaa2690-f7c0-4893-81b1-967aecf80f4b.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A circular laboratory field containing two sperm and an isolated oval cell.'
CONSTRUCTION_PLAN = 'Circular field with two repeated curved sperm symbols; no useful Lucide match.'
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
    icon_id = 'laboratory-sperm'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('laboratory', 'sperm')

    def build(self):
        circle(self,'field',24,24,20)
        for name,cx,cy in [('left',17,16),('right',32,22)]:
            self.add_arc(name+'-head-a',(cx-3,cy),(cx+3,cy),radius_x=3,radius_y=4)
            self.add_arc(name+'-head-b',(cx+3,cy),(cx-3,cy),radius_x=3,radius_y=4)
            self.add_contour(name+'-head',name+'-head-a',name+'-head-b',closed=True)
            self.add_bezier(name+'-tail',(cx,cy+4),((cx-7,cy+7),(cx+1,cy+12),(cx-6,cy+15)))
            self.relate('connect',name+'-head',name+'-tail')
        self.add_arc('cell-a',(18,33),(24,33),radius_x=3,radius_y=4)
        self.add_arc('cell-b',(24,33),(18,33),radius_x=3,radius_y=4)
        self.add_contour('cell','cell-a','cell-b',closed=True)

KEYSHAPE_CENTERLINE_BOUNDS = {'center': [24, 24], 'radius': 20}
