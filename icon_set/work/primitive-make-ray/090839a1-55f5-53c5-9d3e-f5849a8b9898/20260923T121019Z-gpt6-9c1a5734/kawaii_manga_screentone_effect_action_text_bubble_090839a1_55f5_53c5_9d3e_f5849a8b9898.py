from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '090839a1-55f5-53c5-9d3e-f5849a8b9898'
SOURCE_PATH = 'icon_set/work/todo-references/kawaii manga screentone effect action text bubble_090839a1-55f5-53c5-9d3e-f5849a8b9898.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'An empty manga action bubble with scalloped points and radiating emphasis strokes.'
CONSTRUCTION_PLAN = 'Mirror the speech burst about both canvas axes; no useful direct Lucide construction match.'
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
    icon_id = 'kawaii-manga-screentone-effect-action-text-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('kawaii', 'manga', 'screentone', 'effect', 'action', 'text', 'bubble')

    def build(self):
        # Shared upper-half knots mirrored below; every cubic is one scallop.
        upper=[((4,24),(10,22),(9,20),(8,18)),((8,18),(13,19),(16,18),(17,14)),((17,14),(21,18),(27,18),(31,14)),((31,14),(32,18),(35,19),(40,18)),((40,18),(39,20),(38,22),(44,24))]
        members=[]
        for i,(a,b,c,d) in enumerate(upper):
            n=f'upper-{i}';self.add_bezier(n,a,(b,c,d));members.append(n)
        for i,(a,b,c,d) in enumerate(reversed(upper)):
            flip=lambda p:(p[0],48-p[1])
            n=f'lower-{i}';self.add_bezier(n,flip(d),(flip(c),flip(b),flip(a)));members.append(n)
        self.add_contour('burst',*members,closed=True)
        for side in [-1,1]:
            for y,dy in [(8,1),(40,-1)]:
                self.add_line(f'ray-{side}-{y}',(24+side*19,y),(24+side*17,y+dy))
        self.add_line('ray-top',(24,8),(24,8))
        self.add_line('ray-bottom',(24,40),(24,40))

KEYSHAPE_CENTERLINE_BOUNDS = [4, 8, 44, 40]
