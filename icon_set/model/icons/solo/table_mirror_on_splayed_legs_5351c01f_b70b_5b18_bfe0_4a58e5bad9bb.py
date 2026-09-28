"""A tall rectangular mirror with rounded upper corners stands on a thick horizontal support and two outward-leaning legs. Two diagonal reflection strokes cross the upper-middle of its glass.
Symbol plan: Round-topped rectangular table mirror with a broad support rail and two mirrored splayed legs. One diagonal reflection stroke replaces two to keep the glass open.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: no useful exact mirror match. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '5351c01f-b70b-5b18-bfe0-4a58e5bad9bb'
SOURCE_PATH = 'pictographic-primitives/beauty/make up table mirror_5351c01f-b70b-5b18-bfe0-4a58e5bad9bb.svg'
SOURCE_CATEGORY = 'beauty'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'table-mirror-on-splayed-legs'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('table', 'mirror', 'on', 'splayed', 'legs')

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

        self.add_line('mirror-left',(12,28),(12,8));self.add_arc('mirror-top-left',(12,8),(16,4),radius_x=4)
        self.add_line('mirror-top',(16,4),(32,4));self.add_arc('mirror-top-right',(32,4),(36,8),radius_x=4)
        self.add_line('mirror-right',(36,8),(36,28));self.add_contour('mirror','mirror-left','mirror-top-left','mirror-top','mirror-top-right','mirror-right')
        self.add_polyline('support',(8,28),(12,28),(36,28),(40,28),(40,36),(36,36),(12,36),(8,36),closed=True);self.relate('connect','support','mirror')
        self.add_line('reflection',(21,19),(27,13))
        for n,a,b in [('left',(12,36),(8,44)),('right',(36,36),(40,44))]:
         self.add_line(n+'-leg',a,b);self.relate('connect',n+'-leg','support')
