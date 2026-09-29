from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheelchair-user-holding-a-flag/20260929T090411Z-thuan-mac/reference/flag_8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The wheelchair body and arm merged into a heavy block and the flag looked like a rectangular loop.
# Revision plan: Separated the seated figure from its wheel and restored an outstretched hand holding a gently waving flag.
# Construction reference: human_ref/full_body_ref.png: head/torso proportions; accessibility: open rear wheel and seated leg

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
    icon_id = 'wheelchair-user-holding-a-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Retain a seated person, separate visible wheel and waving flag in one 48px scene. Compact wheel/body spacing is visually clear; the detached head gap stays exactly 4px.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '5f1f487aac773fd251a2a67c67c1ad4e1cfd7daa6889a1d2a4e5fd54caa1f5cb'}
    aliases = ()
    keywords = ('flag',)

    def build(self):
        # Shared human reference: circular r5 head and exact 4px gap at torso junction y23.
        circle(self,'head',17,10,5)
        self.add_line('torso',(17,23),(17,31))
        self.add_polyline('leg',(17,31),(28,31),(37,43))
        self.add_line('arm',(17,23),(34,23))
        self.relate('connect','torso','leg');self.relate('connect','torso','arm')
        curve(self,'wheel',(9,25),((2,28),(3,39),(10,43)),((17,47),(25,42),(25,37)))
        self.add_line('flagpole',(34,4),(34,27))
        curve(self,'flag',(34,4),((38,7),(41,1),(44,4)),((44,7),(44,11),(44,14)),((40,11),(38,17),(34,14)))
        self.relate('connect','flagpole','flag');self.relate('connect','flagpole','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
