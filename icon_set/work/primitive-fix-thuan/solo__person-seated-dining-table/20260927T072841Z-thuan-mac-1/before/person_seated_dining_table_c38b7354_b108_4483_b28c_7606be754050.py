"""Person sitting at a table.
Symbol plan: Seated stick figure, chair and table. Head center(14,11), radius5; torso starts(14,24): exact8 centerline /4 ink gap. Bounds (6,6)-(42,42).
Construction reference: icon_set/references/human_ref/full_body_ref.png and icon_set/skills/icon-design/human-reference.md: circular head, coherent round-ended limbs and detached spacing; source seated pose.
Reduction: Tiny cup and tall vessel omitted; seated pose, chair and table retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c38b7354-b108-4483-b28c-7606be754050'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/restaurant seat_c38b7354-b108-4483-b28c-7606be754050.svg'
AUTHOR = 'gpt-6'

class PersonSeatedDiningTable(Solo48):
    icon_id = 'person-seated-dining-table'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('person', 'seated', 'dining', 'table')

    def build(self):
        head_x,head_y,head_r=14,11,5
        neck=(head_x,head_y+head_r+8);hip=(head_x,34)
        self.loop('head',head_x,head_y,head_r)
        self.add_line('torso',neck,hip)
        self.add_polyline('leg',hip,(24,34),(24,42));self.relate('connect','leg','torso')
        self.add_line('arm',neck,(26,24));self.relate('connect','arm','torso')
        self.add_polyline('chair',(6,24),(6,34),hip);self.relate('connect','chair','torso');self.relate('connect','chair','leg')
        self.add_line('chair-leg',(6,34),(6,42));self.relate('connect','chair-leg','chair')
        self.add_polyline('table',(26,24),(36,24),(42,24));self.relate('connect','table','arm')
        self.add_line('table-leg',(36,24),(36,42));self.relate('connect','table-leg','table')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
