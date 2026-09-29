from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vertical-toggle-pair-batch-017-04/20260929T090411Z-thuan-mac/reference/settings toggle vertical_0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.svg'
AUTHOR = "gpt-6"

# Original/current comparison: Octagonal housings and a solid dot obscure the two switch types.
# Revision plan: Replaced polygon corners with rounded switch housings and restored the circular left button and right rocker divider.
# Construction reference: toggle-left: rounded housing and circular knob

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
    if closed: icon.add_contour(name,name+'-curve',closed=True)

class Drawing(Solo48):
    icon_id = 'vertical-toggle-pair-batch-017-04'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Two complete vertical controls require 16-unit housings and a 3-radius button; the button remains legible despite compact housing clearance.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2bf5454dcd0bf3d558222943bd18616770754d88e505993ce2458021617b626e'}
    aliases = ()
    keywords = ('settings toggle vertical',)

    def build(self):
        rounded(self,'left-switch',4,4,20,44,4)
        rounded(self,'right-switch',28,4,44,44,4)
        circle(self,'left-button',12,35,3)
        self.add_line('rocker-divider',(28,30),(44,30))
        self.relate('connect','right-switch','rocker-divider')
