"""Restore laptop base divider and dollar currency ticks. Native SOLO48 redraw, preserving all defining source features."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e6666fd5-a646-4ccf-89c4-7931517ccd22'
SOURCE_PATH = 'pictographic-primitives/other/laptop dollar sign_e6666fd5-a646-4ccf-89c4-7931517ccd22.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/laptop_dollar_symbol_e6666fd5_a646_4ccf_89c4_7931517ccd22.py'
class Drawing(Solo48):
    exception = {'approved_by': 'user', 'reason': 'User approved the smaller dollar sign shown in Proposed currency alternatives — 2-unit spacing. Exception applies to dollar geometry and its spacing within the unchanged device.', 'svg_sha256': 'd5fa95fd28ef8176fd671d423762e670bba8ac2d7a5b6e57aac80c7185cfd86c'}
    icon_id = 'laptop-dollar-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('laptop dollar sign',)

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
        self.path('screen',(8,34),[('L',(8,10)),('A',(12,6),4,4,True),('L',(36,6)),('A',(40,10),4,4,True),('L',(40,34)),('L',(8,34))],True)
        self.add_polyline('base',(8,34),(6,42),(42,42),(40,34))
        self.relate('connect','screen','base')
        self.path('dollar',(29,14),[('L',(24,14)),('L',(21,14)),('C',(21,20),(16,14),(16,20)),('L',(27,20)),('C',(27,26),(32,20),(32,26)),('L',(24,26)),('L',(19,26))])
        self.add_line('currency-top',(24,12),(24,14));self.add_line('currency-bottom',(24,26),(24,28))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')

    icon_id = 'laptop-dollar-symbol'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('payment laptop', 'ecommerce laptop')
    keywords = ('computer', 'dollar', 'money', 'online shopping')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    exception = {'approved_by': 'user', 'reason': 'User approved the smaller dollar sign shown in Proposed currency alternatives — 2-unit spacing. Exception applies to dollar geometry and its spacing within the unchanged device.', 'svg_sha256': 'd5fa95fd28ef8176fd671d423762e670bba8ac2d7a5b6e57aac80c7185cfd86c', 'source_svg_sha256': 'd5fa95fd28ef8176fd671d423762e670bba8ac2d7a5b6e57aac80c7185cfd86c'}
