from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5369bbbe-4735-40b1-9ac5-84246a859e0f'
SOURCE_PATH = 'icon_set/work/todo-references/movie_5369bbbe-4735-40b1-9ac5-84246a859e0f.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A film frame with matching perforations down both sides.'
CONSTRUCTION_PLAN = 'Symmetric rounded film frame with a shared repeated perforation spacing.'
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
    icon_id = 'movie'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('movie',)

    def build(self):
        rounded_rect(self,'frame',6,6,42,42)
        for side in [-1,1]:
            for row,y in enumerate([15,24,33]):self.add_dot(f'perforation-{side}-{row}',(24+side*9,y))
