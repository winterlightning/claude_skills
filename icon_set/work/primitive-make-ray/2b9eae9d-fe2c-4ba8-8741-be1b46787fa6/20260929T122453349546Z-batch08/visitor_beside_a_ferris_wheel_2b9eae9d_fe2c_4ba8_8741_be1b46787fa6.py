"""The rejected visitor has only a head and arrow-like shoulders; restore a visible standing body and legs beside the wheel. No written reviewer feedback.
Restored the visitor torso and separated legs beside the circular wheel and support.
Construction: Shared human_ref/full_body_ref.png. Head center (10,15), radius4; torso starts (10,27): exactly 8 centerline / 4 ink units of detached head clearance, aligned on x=10.
Omissions: Tiny cabin rings omitted; wheel, spokes, support and standing visitor retained.
Keyshape: SQUARE. Balanced overall composition; centerline extremes (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2b9eae9d-fe2c-4ba8-8741-be1b46787fa6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__visitor-beside-a-ferris-wheel/20260929T121814Z-thuan-mac/reference/amusement park ferris wheel person_2b9eae9d-fe2c-4ba8-8741-be1b46787fa6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='visitor-beside-a-ferris-wheel'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('visitor', 'beside', 'a', 'ferris', 'wheel')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.circle('head',10,15,4)
        self.add_line('torso',(10,27),(10,34));self.mark_human_figure('visitor',head='head',torso='torso',torso_junction='start')
        self.add_polyline('arms',(6,31),(10,27),(14,31));self.relate('connect','arms','torso')
        self.add_polyline('legs',(6,42),(10,34),(14,42));self.relate('connect','legs','torso')
        self.circle('wheel',32,16,10)
        self.add_polyline('spoke-v',(32,6),(32,16),(32,26));self.add_polyline('spoke-h',(22,16),(32,16),(42,16))
        for k in ('spoke-v','spoke-h'):self.relate('connect',k,'wheel')
        self.relate('connect','spoke-v','spoke-h')
        self.add_polyline('stand',(24,42),(32,26),(40,42));self.relate('connect','stand','wheel');self.relate('connect','stand','spoke-v')
