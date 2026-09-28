"""A circular head sits above a straight vertical body line. Two arms curve outward and upward from a horizontal shoulder span, while two straight legs spread diagonally below the torso.
Symbol plan: Detached radius-4 circular head at (24,10) over torso neck (24,22), proving the exact 4 ink gap. Mirrored raised arms use radius-6 elbow turns; legs spread evenly from one hip junction.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: human_ref/full_body_ref.png. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '3fdae13f-e594-5e6c-92d5-5c858625d5d6'
SOURCE_PATH = 'pictographic-primitives/avatars/man 1_3fdae13f-e594-5e6c-92d5-5c858625d5d6.svg'
SOURCE_CATEGORY = 'avatars'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'stick-figure-with-raised-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('stick', 'figure', 'with', 'raised', 'arms')

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

        self.add_arc('head-right',(24,6),(24,14),radius_x=4);self.add_arc('head-left',(24,14),(24,6),radius_x=4);self.add_contour('head','head-right','head-left',closed=True)
        self.add_line('torso',(24,22),(24,24));self.add_line('lower-torso',(24,24),(24,32));self.add_contour('body','torso','lower-torso')
        self.add_line('arm-left-up',(6,14),(6,18));self.add_arc('arm-left-turn',(6,18),(12,24),radius_x=6,sweep=False)
        segments('arms',(12,24),(24,24),(36,24));self.add_arc('arm-right-turn',(36,24),(42,18),radius_x=6,sweep=False)
        self.add_line('arm-right-up',(42,18),(42,14));self.add_contour('raised-arms','arm-left-up','arm-left-turn','arms-1','arms-2','arm-right-turn','arm-right-up');self.relate('connect','raised-arms','body')
        self.add_polyline('legs',(12,42),(24,32),(36,42));self.relate('connect','body','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
