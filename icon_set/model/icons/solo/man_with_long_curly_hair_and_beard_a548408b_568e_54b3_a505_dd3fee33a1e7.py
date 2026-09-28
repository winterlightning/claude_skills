"""A blank male face is framed by a large scalloped mass of long curly hair. A full rounded beard and small moustache cover the lower face above broad shoulders.
Symbol plan: Circular face framed by broad long curly hair and a rounded beard. Three large crown lobes replace many tiny curls; a single beard division replaces the moustache. Open broad shoulders touch the circular jaw with zero ink gap.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: human_ref/user.svg. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a548408b-568e-54b3-a505-dd3fee33a1e7'
SOURCE_PATH = 'pictographic-primitives/avatars/male_a548408b-568e-54b3-a505-dd3fee33a1e7.svg'
SOURCE_CATEGORY = 'avatars'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'man-with-long-curly-hair-and-beard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'with', 'long', 'curly', 'hair', 'and', 'beard')

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

        self.add_line('hair-left',(6,42),(6,26));self.add_arc('hair-left-lower',(6,26),(10,16),radius_x=4,radius_y=10)
        self.add_arc('hair-left-upper',(10,16),(16,10),radius_x=6)
        self.add_arc('hair-crown',(16,10),(32,10),radius_x=8,radius_y=4)
        self.add_arc('hair-right-upper',(32,10),(38,16),radius_x=6)
        self.add_arc('hair-right-lower',(38,16),(42,26),radius_x=4,radius_y=10)
        self.add_line('hair-right',(42,26),(42,42));self.add_contour('hair','hair-left','hair-left-lower','hair-left-upper','hair-crown','hair-right-upper','hair-right-lower','hair-right')
        self.add_arc('crown',(16,24),(32,24),radius_x=8);self.add_arc('jaw',(32,24),(16,24),radius_x=8);self.add_contour('head','crown','jaw',closed=True)
        self.add_line('beard-top',(16,24),(32,24));self.relate('connect','beard-top','head')
        shoulders(32,pl=16,left=6,right=42,bottom=42,join_y=41)
        self.relate('connect','hair','body-left');self.relate('connect','hair','body-right')
