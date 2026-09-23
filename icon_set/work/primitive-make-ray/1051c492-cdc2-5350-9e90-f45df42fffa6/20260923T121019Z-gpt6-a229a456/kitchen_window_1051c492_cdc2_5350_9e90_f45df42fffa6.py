from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1051c492-cdc2-5350-9e90-f45df42fffa6'
SOURCE_PATH = 'icon_set/work/todo-references/kitchen window_1051c492-cdc2-5350-9e90-f45df42fffa6.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A four-pane kitchen window resting on a projecting sill.'
CONSTRUCTION_PLAN = 'Shared central axis and repeated pane widths; no useful Lucide window subject match.'
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
    icon_id = 'kitchen-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('kitchen', 'window')

    def build(self):
        # Window walls split at the mullion and sill attachment nodes.
        xs=[10,24,38];ys=[6,20,34]
        for ix,x in enumerate(xs):
            for iy in range(2):
                self.add_line(f'v-{ix}-{iy}',(x,ys[iy]),(x,ys[iy+1]))
        for iy,y in enumerate(ys):
            for ix in range(2):
                self.add_line(f'h-{iy}-{ix}',(xs[ix],y),(xs[ix+1],y))
        self.add_polyline('sill',(10,34),(6,34),(6,42),(42,42),(42,34),(38,34))
        # Contacts are declared only for actual shared endpoints.
        segments={}
        for ix,x in enumerate(xs):
            for iy in range(2):segments[f'v-{ix}-{iy}']={(x,ys[iy]),(x,ys[iy+1])}
        for iy,y in enumerate(ys):
            for ix in range(2):segments[f'h-{iy}-{ix}']={(xs[ix],y),(xs[ix+1],y)}
        for a,ap in segments.items():
            for b,bp in segments.items():
                if a<b and ap&bp:self.relate('connect',a,b)
            if ap & {(10,34),(38,34)}: self.relate('connect',a,'sill')

KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]
