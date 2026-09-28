"""An uncapped lipstick angles from lower-left to upper-right. A rectangular base and shorter collar support a long exposed stick whose tip is cut diagonally and slightly curved on one side.
Symbol plan: Diagonal lipstick with a rounded rectangular base and a slanted exposed tip. The radius-5 base heel uses exact 3:4 tangent sides; one collar seam separates the base and stick. Omit the second narrow collar band.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: paintbrush. Lucide original and atomic-debug renders inspected where named.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '83761b53-9c5f-453d-8f28-587272bd1aba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lipstick-angled-upward-right/20260927T104148Z-thuan-mac-1/reference/lipstick_83761b53-9c5f-453d-8f28-587272bd1aba.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'lipstick-angled-upward-right'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('lipstick', 'angled', 'upward', 'right')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        segments('outline',(9,29),(21,20),(36,8),(36,20),(27,28),(15,37))
        self.add_arc('heel',(15,37),(9,29),radius_x=5)
        self.add_contour('lipstick',*[f'outline-{j}' for j in range(1,6)],'heel',closed=True)
        self.add_line('collar',(21,20),(27,28));self.relate('connect','collar','lipstick')
        self.add_line('base-seam',(13,26),(19,34));self.relate('connect','base-seam','lipstick')
