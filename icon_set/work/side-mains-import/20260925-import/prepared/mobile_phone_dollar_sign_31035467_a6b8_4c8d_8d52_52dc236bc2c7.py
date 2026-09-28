"""Restore phone footer and dollar currency ticks. Native SOLO48 redraw, preserving all defining source features."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '31035467-a6b8-4c8d-8d52-52dc236bc2c7'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone dollar sign_31035467-a6b8-4c8d-8d52-52dc236bc2c7.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/mobile_phone_dollar_sign_31035467_a6b8_4c8d_8d52_52dc236bc2c7.py'
class Drawing(Solo48):
    exception = {'approved_by': 'user', 'reason': 'User approved the smaller dollar sign shown in Proposed currency alternatives — 2-unit spacing. Exception applies to dollar geometry and its spacing within the unchanged device.', 'svg_sha256': 'd5bd8ab1467496d1db98f28a72a74dea5f5b17ac3c25de8ad69d7845d5158122'}
    icon_id = 'mobile-phone-dollar-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile phone dollar sign',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.box('phone',8,4,40,44,4)
        self.add_line('footer',(8,36),(40,36));self.relate('connect','phone','footer')
        self.path('dollar',(29,12),[('L',(24,12)),('L',(21,12)),('C',(21,20),(16,12),(16,20)),('L',(27,20)),('C',(27,28),(32,20),(32,28)),('L',(24,28)),('L',(19,28))])
        self.add_line('currency-top',(24,10),(24,12));self.add_line('currency-bottom',(24,28),(24,30))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')

    icon_id = 'mobile-phone-dollar-sign'
    category = 'objects/device'
    aliases = ('payment phone', 'dollar smartphone')
    keywords = ('mobile', 'money', 'commerce', 'payment')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'reason': 'User approved the smaller dollar sign shown in Proposed currency alternatives — 2-unit spacing. Exception applies to dollar geometry and its spacing within the unchanged device.', 'svg_sha256': 'd5bd8ab1467496d1db98f28a72a74dea5f5b17ac3c25de8ad69d7845d5158122', 'source_svg_sha256': 'd5bd8ab1467496d1db98f28a72a74dea5f5b17ac3c25de8ad69d7845d5158122'}
