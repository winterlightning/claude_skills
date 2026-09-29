from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ae8162b-1fa3-4f3e-a7f2-5375c421b45f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-earbuds-charging-case-solo-b001-15/20260929T090411Z-thuan-mac/reference/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
AUTHOR = "gpt-6"

# Original/current comparison: Circular rings replaced the earbuds and the charging lightning symbol became a dot.
# Revision plan: Restored shaped earbud heads with stems entering the case and an explicit lightning bolt on the case.
# Construction reference: ear: smooth earbud lobes; original: paired stems, rounded case and central lightning bolt

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
    icon_id = 'wireless-earbuds-charging-case-solo-b001-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Rebalanced the earbuds and case to give the lightning bolt a clear 15-unit height. Retain compact stem and bolt margins at fixed 4px stroke; recognizable charging meaning takes priority over full 4px detail spacing.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'cf233aefac856e313a941a39b351b77be13ae2b2cce60f2887d44c4d7d7593fc'}
    aliases = ()
    keywords = ('earpods charge',)

    def build(self):
        # Mirrored earbud housings retain their downward stems; shared geometry maintains equal proportions.
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            curve(self,'earbud-'+str(side),p(4,19),(p(4,18),p(4,13),p(4,11)),(p(4,1),p(20,1),p(20,10)),(p(20,15),p(14,16),p(10,14)),(p(10,18),p(10,18),p(10,19)))
        # The stems join the case rim; rounded lower corners give a familiar charging case silhouette.
        self.add_line('rim',(6,19),(42,19))
        curve(self,'case',(42,19),((42,26),(42,34),(42,37)),((42,44),(35,44),(31,44)),((27,44),(21,44),(17,44)),((13,44),(6,44),(6,37)),((6,34),(6,26),(6,19)))
        self.relate('connect','rim','case')
        for side in (-1,1):self.relate('connect','rim','earbud-'+str(side))
        self.add_polyline('charge',(26,24),(18,34),(24,34),(22,39),(30,29),(24,29),closed=True)
