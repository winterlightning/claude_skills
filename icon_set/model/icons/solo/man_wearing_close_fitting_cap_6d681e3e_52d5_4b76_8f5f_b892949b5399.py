"""A front-facing man has a rounded cap separated from the blank face by a straight band. Small ears project at the sides, above a curved neckline and short central shirt seam.
Symbol plan: Close-fitting hemispherical cap and circular jaw over smooth shoulders with a short central shirt seam. Mirror the cap and shoulder geometry; omit tiny ears and the extra collar curve.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: human_ref/user.svg; hat-glasses. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '6d681e3e-52d5-4b76-8f5f-b892949b5399'
SOURCE_PATH = 'pictographic-primitives/avatars/man cap_6d681e3e-52d5-4b76-8f5f-b892949b5399.svg'
SOURCE_CATEGORY = 'avatars'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'man-wearing-close-fitting-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'wearing', 'close', 'fitting', 'cap')

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

        bottom=avatar_head(14,10,cap=True);top=shoulders(bottom,join_y=40)
        self.add_line('body-seam',(24,top),(24,44));self.relate('connect','body-seam','body-neckline');self.relate('connect','body-seam','head')
