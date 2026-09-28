"""A tall lipstick case with rounded lower corners supports a stepped collar and exposed cosmetic stick. The stick's upper edge slopes upward to the right, with a softly curved left corner.
Symbol plan: Upright lipstick with a diagonal cut and smooth outer tip inside a round-cornered case. The case is wider than the exposed stick. CIRCLE retains upright proportions without widening to a rectangular keyshape; omit the second narrow collar tier.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: no useful exact lipstick match. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '422fa961-4cef-5bf4-8415-0550aee83639'
SOURCE_PATH = 'pictographic-primitives/beauty/make up lipstick_422fa961-4cef-5bf4-8415-0550aee83639.svg'
SOURCE_CATEGORY = 'beauty'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'upright-lipstick-with-angled-tip'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('beauty', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('upright', 'lipstick', 'with', 'angled', 'tip')

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

        segments('case-top',(12,24),(16,24),(32,24),(36,24),(36,36))
        self.add_arc('case-right-corner',(36,36),(32,40),radius_x=4)
        self.add_line('case-bottom',(32,40),(16,40));self.add_arc('case-left-corner',(16,40),(12,36),radius_x=4)
        self.add_line('case-left',(12,36),(12,24));self.add_contour('case','case-top-1','case-top-2','case-top-3','case-top-4','case-right-corner','case-bottom','case-left-corner','case-left',closed=True)
        segments('stick-left',(16,24),(16,12),(24,4));self.add_arc('stick-tip',(24,4),(32,16),radius_x=8,radius_y=12)
        self.add_line('stick-right',(32,16),(32,24));self.add_contour('stick','stick-left-1','stick-left-2','stick-tip','stick-right');self.relate('connect','stick','case')
