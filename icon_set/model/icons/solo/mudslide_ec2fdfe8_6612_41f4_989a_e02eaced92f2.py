from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec2fdfe8-6612-41f4-989a-e02eaced92f2'
SOURCE_PATH = 'icon_set/work/todo-references/mudslide_ec2fdfe8-6612-41f4-989a-e02eaced92f2.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A diamond warning sign showing a curved mudslide descending from a slope.'
CONSTRUCTION_PLAN = 'Angular diamond frame contrasts with a coherent curved landslide boundary. Preserve the uneven downhill silhouette. No useful Lucide subject match used.'
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
    icon_id = 'mudslide'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('mudslide',)

    def build(self):
        self.add_polyline('frame',(6,24),(24,6),(42,24),(34,32),(24,42),closed=True)
        self.add_line('cliff-1',(14, 28),(14, 22))
        self.add_line('cliff-2',(14, 22),(20, 15))
        self.add_line('cliff-3',(20, 15),(24, 19))
        self.add_bezier('slide',(24,19),((21,25),(26,32),(29,32)),((31,32),(32,30),(34,32)))
        self.add_contour('upper-slope','cliff-1','cliff-2','cliff-3','slide')
        self.add_bezier('lower-slope',(14,28),((20,28),(22,33),(28,33)))
        self.relate('connect','upper-slope','lower-slope')
        self.relate('connect','upper-slope','frame')
