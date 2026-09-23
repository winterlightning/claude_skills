"""Three user busts sit beneath three Wi-Fi arcs.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Small side heads reduced to two-unit-radius circles.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a119cf45-d021-460f-b469-9d1f28774714'
SOURCE_PATH='icon_set/work/todo-references/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='multiple-users-wifi'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('multiple', 'users', 'wifi')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        # Series: three centered radio arcs. Shared human_ref/user.svg bust vocabulary.
        for i,(x,y,w) in enumerate([(10,12,28),(14,19,20),(18,25,12)]):
            self.add_arc('wifi-'+str(i),(x,y),(x+w,y),radius_x=w//2,radius_y=6)
        for n,x,y,r in [('center',24,27,3),('left',10,29,2),('right',38,29,2)]:
            self.circle(n+'-head',x,y,r)
        self.add_bezier('center-body',(16,42),((16,38),(20,38),(24,38)),((28,38),(32,38),(32,42)))
        self.add_bezier('left-body',(6,42),((6,39),(10,39),(10,39)),((12,39),(16,40),(16,42)))
        self.add_bezier('right-body',(32,42),((32,40),(36,39),(38,39)),((38,39),(42,39),(42,42)))
        self.relate('connect','center-body','left-body');self.relate('connect','center-body','right-body')
        # Head bottoms 30/31, shoulder crests38/39: each exact centerline gap8.

# Final visible bounds: (4, 4, 44, 44)
# Construction: Shared human references supplied round heads, broad shoulders and coherent pose construction. Analytical head/body spacing is recorded in the visual review.
# Final reductions: Small side heads reduced to two-unit-radius circles.
# Visual review: Three heads and shoulders remain present but the lowest Wi-Fi arc merges with the center head. Radio arc gaps fail MIC. Center head bottom30 / shoulder crest38 and side head bottoms31 / shoulder crests39 each give exactly8 centerline units, hence4 visible ink units. Not approved.
