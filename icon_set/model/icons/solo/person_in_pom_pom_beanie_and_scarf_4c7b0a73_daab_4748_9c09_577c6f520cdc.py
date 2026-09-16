"""A blank oval face wears a rounded beanie with a wide turned-up band and small top pom-pom. A thick scarf collar sits above the shoulders and central clothing seam.
Symbol plan: Pom-pom beanie above a circular jaw, a broad scarf collar and a short central coat seam. Use radius-2 pom-pom and a single brim line; omit the double brim strip to reserve the scarf opening.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: human_ref/user.svg; hat-glasses. Named Lucide original/atomic geometry and shared human references inspected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '4c7b0a73-daab-4748-9c09-577c6f520cdc'
SOURCE_PATH = 'pictographic-primitives/avatars/man beanie_4c7b0a73-daab-4748-9c09-577c6f520cdc.svg'
SOURCE_CATEGORY = 'avatars'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'person-in-pom-pom-beanie-and-scarf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('person', 'in', 'pom', 'pom', 'beanie', 'and', 'scarf')

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

        self.add_arc('pom-right',(24,4),(24,8),radius_x=2);self.add_arc('pom-left',(24,8),(24,4),radius_x=2);self.add_contour('pom','pom-right','pom-left',closed=True)
        self.add_arc('cap-left',(14,18),(24,8),radius_x=10,radius_y=10);self.add_arc('cap-right',(24,8),(34,18),radius_x=10,radius_y=10)
        segments('brim',(34,18),(32,18),(16,18),(14,18));self.add_contour('cap','cap-left','cap-right','brim-1','brim-2','brim-3',closed=True);self.relate('connect','pom','cap')
        self.add_arc('jaw',(32,18),(16,18),radius_x=8);self.relate('connect','jaw','cap')
        shoulders(26,kind='scarf',head='jaw',join_y=40)
        self.add_line('body-seam',(24,38),(24,44));self.relate('connect','body-seam','body-neckline')
