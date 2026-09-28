from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '675d2e83-bae0-46ca-b68a-04732a2c88a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-shuttlecock/20260927T142540Z-thuan-mac-1/reference/monitor shuttlecock_675d2e83-bae0-46ca-b68a-04732a2c88a9.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A monitor showing a diagonal badminton shuttlecock.'
CONSTRUCTION_PLAN = 'Complete monitor pedestal, a round cork, and four joined feather strokes fanning diagonally.'
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
    icon_id = 'monitor-shuttlecock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("combination", "other", "primitives-generate")
    aliases = ()
    keywords = ('monitor', 'shuttlecock')

    def build(self):
        monitor(self)
        # The round cork is explicit; three uneven feather tips fan up-right.
        circle(self,'cork',20,22,3)
        for name, tip in (('upper',(25,15)),('middle',(29,15)),
                          ('outer',(33,18)),('lower',(28,25))):
            self.add_line('feather-'+name,(23,22),tip)
            self.relate('connect','cork','feather-'+name)
        self.relate('connect','feather-upper','feather-middle','feather-outer','feather-lower')
