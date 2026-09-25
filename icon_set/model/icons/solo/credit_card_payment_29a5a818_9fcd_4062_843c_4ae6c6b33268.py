"""A payment terminal with receipt beside a card and insertion arrow.
Symbol plan and construction: credit-card and receipt: rounded card and broad paper notch.
Keyshape: HRECT_L reserves separate terminal and card/arrow columns.
Omissions: Card stripe, upper terminal bezel and extra keypad marks removed; two keys and one broad receipt notch remain.
Review: Approved: terminal, emerging receipt, separate card and downward arrow read clearly in both themes. Receipt meets actual split terminal nodes."""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='29a5a818-9fcd-4062-843c-4ae6c6b33268'
SOURCE_PATH = 'pictographic-primitives/payments/credit card payment_29a5a818-9fcd-4062-843c-4ae6c6b33268.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='credit-card-payment'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'payments'
    aliases=()
    keywords=('credit', 'card', 'payment')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('terminal',(8,24),(24,24),(28,24),(28,40),(4,40),(4,24),closed=True)
        self.add_polyline('receipt',(8,24),(8,8),(16,12),(24,8),(24,24));self.relate('connect','receipt','terminal')
        for i,x in enumerate((12,20)):self.add_dot(f'key-{i}',(x,32))
        self.rounded('card',36,8,44,24,2)
        self.add_line('shaft',(40,32),(40,40))
        self.add_polyline('arrow',(36,36),(40,40),(44,36));self.relate('connect','shaft','arrow')


    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)
