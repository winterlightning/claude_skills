"""A round rabbit head with two long outward-leaning ears rises above a top hat's straight brim. The hat tapers toward a rounded base and carries a horizontal band.
Symbol plan: Round rabbit cheeks and two matching long ears emerge from a top hat. Radius-4 ear tips and a circular lower face; broad straight brim and tapered hat. Omit facial features and the extra band so the round cheeks retain enough height.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: rabbit. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '241a4c1f-1361-497b-b8e6-8120ae1c505c'
SOURCE_PATH = 'pictographic-primitives/business/magic rabbit_241a4c1f-1361-497b-b8e6-8120ae1c505c.svg'
SOURCE_CATEGORY = 'business'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'rabbit-emerging-from-top-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('rabbit', 'emerging', 'from', 'top', 'hat')

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

        self.add_line('left-ear-outer',(12,20),(12,8));self.add_arc('left-ear-top',(12,8),(20,8),radius_x=4)
        segments('ears-inner',(20,8),(20,16),(28,16),(28,8));self.add_arc('right-ear-top',(28,8),(36,8),radius_x=4)
        self.add_line('right-ear-outer',(36,8),(36,20));self.add_arc('cheek-right',(36,20),(24,32),radius_x=12)
        self.add_arc('cheek-left',(24,32),(12,20),radius_x=12)
        self.add_contour('rabbit','left-ear-outer','left-ear-top','ears-inner-1','ears-inner-2','ears-inner-3','right-ear-top','right-ear-outer','cheek-right','cheek-left',closed=True)
        self.add_polyline('brim',(8,32),(12,32),(24,32),(36,32),(40,32));self.relate('connect','rabbit','brim')
        self.add_polyline('hat',(12,32),(14,44),(34,44),(36,32));self.relate('connect','hat','brim')
