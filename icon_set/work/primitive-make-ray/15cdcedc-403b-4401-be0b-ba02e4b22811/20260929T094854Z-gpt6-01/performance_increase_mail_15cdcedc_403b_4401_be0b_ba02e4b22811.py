from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '15cdcedc-403b-4401-be0b-ba02e4b22811'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__performance-increase-mail/20260929T094854Z-thuan-mac/reference/performance increase mail_15cdcedc-403b-4401-be0b-ba02e4b22811.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The chart bars floated above a flat empty envelope and the trend became a detached tiny arrow.
# Revision plan: Restored three outlined columns rising out of an open envelope and a continuous upward trend with arrowhead.
# Construction reference: mail: envelope flap; chart-no-axes-combined: rising columns with an ascending polyline

def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def rounded(icon,name,x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    ids=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8];n=f'{name}-{j}';ids.append(n)
        if j%2: icon.add_arc(n,a,b,radius_x=r)
        else: icon.add_line(n,a,b)
    icon.add_contour(name,*ids,closed=True)

def curve(icon,name,start,*segments,closed=False):
    icon.add_bezier(name+'-curve',start,*segments)
    icon.add_contour(name,name+'-curve',closed=closed)

class Drawing(Solo48):
    icon_id = 'performance-increase-mail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Three visible columns and the trend arrow are the defining meaning. Their compact2px column interiors and gaps are intentional within the complete48px envelope composition.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd7b2471ce7e55eb06a2a35829cf579b38287bdb62770c0877639c2c47117b167'}
    aliases = ()
    keywords = ('performance increase mail',)

    def build(self):
        # Bars terminate exactly on the two envelope-flap diagonals.
        self.add_polyline('envelope',(4,28),(10,31),(16,34),(22,37),(24,38),(28,36),(34,33),(40,30),(44,28),(44,44),(4,44),closed=True)
        for name,x0,x1,top,y0,y1 in [('low',10,16,22,31,34),('mid',22,28,18,37,36),('high',34,40,14,33,30)]:
            self.add_polyline(name,(x0,y0),(x0,top),(x1,top),(x1,y1))
            self.relate('connect','envelope',name)
        self.add_polyline('trend',(6,16),(14,9),(21,12),(29,6),(34,9),(44,3))
        self.add_polyline('arrowhead',(36,3),(44,3),(44,11));self.relate('connect','trend','arrowhead')
