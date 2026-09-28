from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb412b73-2149-4427-b06e-19f0aa825780'
SOURCE_PATH = 'icon_set/work/todo-references/moutain with circle_fb412b73-2149-4427-b06e-19f0aa825780.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A diamond-framed mountain slope beside a circular sun.'
CONSTRUCTION_PLAN = 'Diamond border with explicitly split attachment points for the asymmetric angular slope; separate circular sun.'
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
    icon_id = 'moutain-with-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('moutain', 'with', 'circle')

    def build(self):
        self.add_polyline('frame',(6,24),(14,16),(24,6),(42,24),(32,34),(24,42),closed=True)
        self.add_polyline('mountain',(14,16),(20,17),(22,25),(32,34))
        self.relate('connect','frame','mountain')
        circle(self,'sun',30,21,3)
