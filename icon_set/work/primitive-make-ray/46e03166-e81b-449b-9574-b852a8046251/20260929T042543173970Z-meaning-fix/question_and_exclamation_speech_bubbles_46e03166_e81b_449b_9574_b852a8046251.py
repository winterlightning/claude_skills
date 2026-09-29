"""Two offset rounded speech bubbles, full rear question sign and front exclamation with separate stem and dot; rear outline interrupted only by the front bubble.
Reference comparison: The rejected rear bubble was open on the left and its exclamation was only a dot. Feedback asks to recover both messages and their punctuation.
Construction references: Lucide message-square: rounded frame and corner tail; message-circle-question-mark punctuation.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '46e03166-e81b-449b-9574-b852a8046251'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__question-and-exclamation-speech-bubbles/20260929T042221Z-thuan-mac/reference/conversation question warning_46e03166-e81b-449b-9574-b852a8046251.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'question-and-exclamation-speech-bubbles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.path('rear',(22,34),('L',(14,42)),('L',(14,34)),('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(32,6)),('A',(36,10),4,4,True),('L',(36,16)))
        self.path('front',(28,22),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,36)),('A',(38,40),4,4,True),('L',(38,44)),('L',(32,40)),('L',(28,40)),('A',(24,36),4,4,True),('L',(24,26)),('A',(28,22),4,4,True),closed=True)
        self.path('question',(14,15),('A',(22,15),4,4,True),('A',(19,19),4,4,True),('L',(19,21)))
        self.add_dot('question-dot',(19,27))
        self.add_line('exclamation-stem',(33,27),(33,30))
        self.add_dot('exclamation-dot',(33,36))

Drawing.exception = {'reason': 'Two complete message symbols require compact punctuation and close overlapping enclosure edges. All intended marks remain visibly separated with 4px strokes; user authorized composition and spacing exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'e806ef403f289a7ccd04a2cff9c941bd27aa777515f4b29e21ac4b5089b31c2b'}
