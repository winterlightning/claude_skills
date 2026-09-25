from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1aef3c2a-6d0d-43a2-9616-698d70dc5298'
SOURCE_PATH = 'pictographic-primitives/other/monitor small squares_1aef3c2a-6d0d-43a2-9616-698d70dc5298.svg'
AUTHOR = "gpt-6"
SUBJECT = 'A monitor showing two vertically stacked small squares.'
CONSTRUCTION_PLAN = 'Shared monitor enclosure and one square definition repeated down the left screen area.'
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
    icon_id = 'monitor-small-squares'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('monitor', 'small', 'squares')

    def build(self):
        # This retained vertical tile layout cannot meet all SOLO48 clearances.
        # Preserve two recognizable square tiles rather than claim the enlarged but clipped attempt passes.
        self.add_polyline('screen',(8,4),(40,4),(40,36),(24,36),(8,36),closed=True)
        self.add_line('stand',(24,36),(24,44));self.add_polyline('base',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','base')
        for i,y in enumerate((10,24)):
            self.add_polyline(f'square-{i}',(16,y),(22,y),(22,y+6),(16,y+6),closed=True)


# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '65f7ab7b3e6dbcdaaa81cd56d64774533777e54e10b957f94097f0eab69157a9', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '1aef3c2a-6d0d-43a2-9616-698d70dc5298'}
