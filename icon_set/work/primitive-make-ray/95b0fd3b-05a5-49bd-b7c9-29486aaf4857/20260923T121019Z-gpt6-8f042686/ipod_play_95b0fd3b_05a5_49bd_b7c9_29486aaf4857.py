from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '95b0fd3b-05a5-49bd-b7c9-29486aaf4857'
SOURCE_PATH = 'icon_set/work/todo-references/ipod play_95b0fd3b-05a5-49bd-b7c9-29486aaf4857.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'An iPod player with play triangle, screen division, and circular control.'
CONSTRUCTION_PLAN = 'Tangent rounded device body with independently authored play and control. '
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
    icon_id = 'ipod-play'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ipod', 'play')

    def build(self):
        rounded_rect(self,'body',8,4,40,44)
        self.add_polyline('play',(18,13),(30,20),(18,27),closed=True)
        self.add_line('screen-divider',(8,32),(40,32))
        self.relate('connect','body','screen-divider')
        circle(self,'control',24,38,2)

KEYSHAPE_CENTERLINE_BOUNDS = [8, 4, 40, 44]
