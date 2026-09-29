from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '26319804-c7ff-498f-a76f-62441d482fc8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-phone-lock/20260929T094854Z-thuan-mac/reference/mobile phone lock_26319804-c7ff-498f-a76f-62441d482fc8.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The phone was too square and blocky, making the locked-mobile concept read as a generic framed lock.
# Revision plan: Restored a tall rounded phone silhouette, bottom screen divider and clear closed padlock.
# Construction reference: smartphone: portrait rounded enclosure; lock-keyhole: rounded shackle and distinct lock body

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
    icon_id = 'mobile-phone-lock'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The complete closed padlock and phone footer need compact gaps. Preserve the tall phone and lock identity with4px strokes rather than broadening the body into a generic frame.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'dc4bef5c0e1e5f38a08ced451d974a325c435713b0873062884a939c13ef1453'}
    aliases = ()
    keywords = ('mobile phone lock',)

    def build(self):
        # VRECT_M extremes10,4–38,44: phone proportions own the composition.
        rounded(self,'phone',10,4,38,44,5)
        self.add_line('screen-divider',(10,35),(38,35));self.relate('connect','phone','screen-divider')
        rounded(self,'lock-body',17,22,31,29,2)
        self.add_line('shackle-left',(19,22),(19,19))
        self.add_arc('shackle-top',(19,19),(29,19),radius_x=5)
        self.add_line('shackle-right',(29,19),(29,22))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','lock-body','shackle')
