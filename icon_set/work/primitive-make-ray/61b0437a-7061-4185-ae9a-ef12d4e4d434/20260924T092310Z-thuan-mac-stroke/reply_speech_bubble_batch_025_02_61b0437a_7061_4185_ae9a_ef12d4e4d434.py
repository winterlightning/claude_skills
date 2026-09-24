"""Square reply speech bubble with left arrow integrated into the top border; rounded corners and long lower-left tail. Bounds 6,6 to42,42.
Construction reference: Lucide message-circle-reply: open arrowhead and coherent bubble contour.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '61b0437a-7061-4185-ae9a-ef12d4e4d434'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__reply-speech-bubble-batch-025-02/20260924T092136Z-thuan-mac/reference/message bubble arrow 1_61b0437a-7061-4185-ae9a-ef12d4e4d434.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'reply-speech-bubble-batch-025-02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('message', 'bubble', 'arrow', '1')
    def build(self):
        self.path('bubble',(14,12),[('L',(12,12)),('A',(6,18),6,6,False),('L',(6,30)),('A',(12,36),6,6,False),('L',(12,42)),('L',(22,36)),('L',(36,36)),('A',(42,30),6,6,False),('L',(42,18)),('A',(36,12),6,6,False),('L',(24,12))])
        self.add_polyline('arrow',(30,6),(24,12),(30,18))
        self.relate('connect','bubble','arrow')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
