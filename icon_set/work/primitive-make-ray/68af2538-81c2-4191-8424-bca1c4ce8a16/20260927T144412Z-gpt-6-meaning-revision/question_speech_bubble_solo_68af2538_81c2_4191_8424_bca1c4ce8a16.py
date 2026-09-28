"""Question inside an upright speech bubble; VRECT_L centerline extremes 8,4 to 40,44. Shared corner radius 4; open question hook and separate dot.
Construction reference: Lucide circle-question-mark: rounded hook; message-circle-reply: integrated tail.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='68af2538-81c2-4191-8424-bca1c4ce8a16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__question-speech-bubble-solo/20260927T144036Z-thuan-mac-1/reference/messages bubble square question_68af2538-81c2-4191-8424-bca1c4ce8a16.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'question-speech-bubble-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'messages'
    categories = ('messages', 'state')
    aliases = ()
    keywords = ('messages', 'bubble', 'square', 'question')
    def build(self):
        # Square speech bubble owns a large, open question mark and a distinct dot.
        self.path('bubble',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,36)),('A',(36,40),4,4,True),('L',(20,40)),('L',(12,44)),('L',(12,40)),('A',(8,36),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.add_bezier('question-crown',(17,18),((17,11),(31,11),(31,18)))
        self.add_line('question-turn',(31,18),(24,22))
        self.add_contour('question','question-crown','question-turn')
        self.add_dot('question-dot',(24,31))

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
