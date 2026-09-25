from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26790288-140d-4885-a97e-0a3a2c64fc42'
SOURCE_PATH = 'icon_set/work/todo-references/movies director chair_26790288-140d-4885-a97e-0a3a2c64fc42.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A director chair with a star on its back and crossed folding legs.'
CONSTRUCTION_PLAN = 'Shared axis mirrors the back, arms and legs; star is nested inside the back panel. No useful direct local Lucide chair match used.'
KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def rounded_rect(icon,name,left,top,right,bottom,r=4,bottom_split=None):
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom)]
    if bottom_split is not None:points.append((bottom_split,bottom))
    points += [(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%len(points)];n=f'{name}-{i}';members.append(n)
        if start[0]!=end[0] and start[1]!=end[1]:icon.add_arc(n,start,end,radius_x=r)
        else:icon.add_line(n,start,end)
    icon.add_contour(name,*members,closed=True)

def monitor(icon):
    # Shared screen, central attachment and two base halves, drawn on SOLO48.
    rounded_rect(icon,'screen',6,6,42,34,bottom_split=24)
    icon.add_line('stand',(24,34),(24,42))
    icon.add_line('base-left',(16,42),(24,42))
    icon.add_line('base-right',(24,42),(32,42))
    icon.relate('connect','screen','stand')
    icon.relate('connect','stand','base-left','base-right')

class Drawing(Solo48):
    icon_id = 'movies-director-chair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "movies"
    aliases = ()
    keywords = ('movies', 'director', 'chair')

    def build(self):
        self.add_polyline('back',(14,6),(14,24),(34,24),(34,6))
        self.add_line('back-top',(14,8),(34,8))
        self.relate('connect','back','back-top')
        self.add_polyline('star',(24,11),(26,15),(30,16),(27,19),(28,23),(24,21),(20,23),(21,19),(18,16),(22,15),closed=True)
        for side in [-1,1]:
            self.add_polyline(f'arm-{side}',(24+side*18,24),(24+side*15,24),(24+side*13,30))
        self.add_line('seat',(11,30),(37,30))
        for side in [-1,1]:self.relate('connect','seat',f'arm-{side}')
        self.add_line('leg-left',(14,30),(34,42))
        self.add_line('leg-right',(34,30),(14,42))
        self.relate('connect','seat','leg-left','leg-right')
