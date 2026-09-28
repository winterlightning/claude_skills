"""A seated lucky cat has pointed ears, closed smiling eyes and one raised paw on the left. A collar holds a round medallion above its broad belly, with a tail at the right.
Symbol plan: Seated beckoning cat with pointed ears, raised left foreleg and a round collar medallion. A broad smooth belly balances the raised paw. Omit the tiny eyes, mouth, paw crease and secondary tail.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: cat. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c9e24a22-9295-4cdf-847c-570f09ece027'
SOURCE_PATH = 'pictographic-primitives/business/lucky cat_c9e24a22-9295-4cdf-847c-570f09ece027.svg'
SOURCE_CATEGORY = 'business'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'beckoning-lucky-cat-with-medallion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('beckoning', 'lucky', 'cat', 'with', 'medallion')

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

        def avatar_head(cy=12,r=8,cap=False):
            self.add_arc('crown',(24-r,cy),(24+r,cy),radius_x=r)
            self.add_arc('jaw',(24+r,cy),(24-r,cy),radius_x=r)
            self.add_contour('head','crown','jaw',closed=True)
            if cap:
                self.add_line('cap-band',(24-r,cy),(24+r,cy))
                self.relate('connect','cap-band','head')
            return cy+r

        def shoulders(head_bottom,pl=16,left=8,right=40,bottom=44,join_y=36,kind='plain',head='head'):
            top=head_bottom+HEAD_BODY_CENTERLINE_GAP;pr=48-pl
            self.add_line('body-left-side',(left,bottom),(left,join_y))
            self.add_arc('body-left-shoulder',(left,join_y),(pl,top),radius_x=pl-left,radius_y=join_y-top)
            self.add_contour('body-left','body-left-side','body-left-shoulder')
            self.add_line('body-top',(pl,top),(24,top))
            self.add_line('body-top-right',(24,top),(pr,top))
            members=['body-top','body-top-right']
            if kind=='wrap':
                self.add_bezier('body-wrap',(pr,top),((pr-3,top+7),(left+8,bottom-3),(left,bottom)))
                members+=['body-wrap']
            if kind=='v-neck':
                self.add_line('body-v-right',(pr,top),(24,bottom-2))
                self.add_line('body-v-left',(24,bottom-2),(pl,top))
                members+=['body-v-right','body-v-left']
            if kind=='scarf':
                self.add_arc('body-scarf-right',(pr,top),(24,top+8),radius_x=8)
                self.add_arc('body-scarf-left',(24,top+8),(pl,top),radius_x=8)
                members+=['body-scarf-right','body-scarf-left']
            self.add_contour('body-neckline',*members,closed=kind in ('v-neck','scarf'))
            self.add_arc('body-right-shoulder',(pr,top),(right,join_y),radius_x=right-pr,radius_y=join_y-top)
            self.add_line('body-right-side',(right,join_y),(right,bottom))
            self.add_contour('body-right','body-right-shoulder','body-right-side')
            self.relate('connect','body-left','body-neckline');self.relate('connect','body-right','body-neckline')
            self.relate('connect',head,'body-neckline')
            return top

        segments('ears',(18,18),(18,6),(24,10),(32,10),(38,6),(38,18))
        self.add_arc('cheek-right',(38,18),(28,26),radius_x=10,radius_y=8)
        self.add_arc('cheek-left',(28,26),(18,18),radius_x=10,radius_y=8)
        self.add_contour('head',*[f'ears-{j}' for j in range(1,6)],'cheek-right','cheek-left',closed=True)
        self.add_bezier('body-left',(18,18),((18,24),(14,26),(14,34)))
        self.add_arc('belly',(14,34),(42,34),radius_x=14,radius_y=8,sweep=False)
        self.add_bezier('body-right',(42,34),((42,26),(38,24),(38,18)))
        self.add_contour('body','body-left','belly','body-right');self.relate('connect','body','head')
        self.add_line('raised-paw',(6,14),(6,26));self.add_arc('elbow',(6,26),(14,34),radius_x=8,sweep=False)
        self.add_contour('arm','raised-paw','elbow');self.relate('connect','arm','body')
        self.add_arc('medallion-right',(28,26),(28,32),radius_x=3);self.add_arc('medallion-left',(28,32),(28,26),radius_x=3)
        self.add_contour('medallion','medallion-right','medallion-left',closed=True);self.relate('connect','medallion','head')
