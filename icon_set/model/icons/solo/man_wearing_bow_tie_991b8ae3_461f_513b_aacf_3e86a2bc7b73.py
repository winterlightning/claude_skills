"""An oval head floats above a rounded bust with a flat lower edge. Two triangular bow-tie wings meet at the centre of the neckline, directly beneath the head.
Symbol plan: Round-headed bust with two mirrored broad triangular bow-tie wings meeting at one center knot. Radius-7 head at (24,13) touches shoulder top24. Broad curved shoulders reserve clear space around the bow; omit the enclosing bottom edge and extra neckline.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: human_ref/user.svg. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '991b8ae3-461f-513b-aacf-3e86a2bc7b73'
SOURCE_PATH = 'pictographic-primitives/avatars/man_991b8ae3-461f-513b-aacf-3e86a2bc7b73.svg'
SOURCE_CATEGORY = 'avatars'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'man-wearing-bow-tie'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'wearing', 'bow', 'tie')

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

        bottom=avatar_head(13,7);top=bottom+HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(6,42),(6,30));self.add_arc('body-left-shoulder',(6,30),(13,top),radius_x=7,radius_y=6)
        self.add_line('body-top',(13,top),(24,top));self.add_line('body-top-right',(24,top),(35,top));self.add_contour('body-neckline','body-top','body-top-right')
        self.add_arc('body-right-shoulder',(35,top),(42,30),radius_x=7,radius_y=6);self.add_line('body-right-side',(42,30),(42,42))
        for side in ('left','right'):
         self.relate('connect','body-'+side+'-side','body-'+side+'-shoulder');self.relate('connect','body-'+side+'-shoulder','body-neckline')
        self.relate('connect','head','body-neckline')
        self.add_polyline('body-bow-left',(14,32),(24,37),(14,42),closed=True)
        self.add_polyline('body-bow-right',(34,32),(34,42),(24,37),closed=True);self.relate('connect','body-bow-left','body-bow-right')
