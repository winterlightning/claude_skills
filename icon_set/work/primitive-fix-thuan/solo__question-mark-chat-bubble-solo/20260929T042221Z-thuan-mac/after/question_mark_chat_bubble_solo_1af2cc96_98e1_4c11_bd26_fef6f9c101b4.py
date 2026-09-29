"""Smooth rounded bubble with a distinct tail; upright question hook with curved return and a separate dot.
Reference comparison: The rejected question hook collapsed into a diagonal wedge and crowded the enclosure. Feedback asks to restore the reference question bubble.
Construction references: Lucide message-circle-question-mark and message-square: coherent enclosure and independently readable question mark.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1af2cc96-98e1-4c11-bd26-fef6f9c101b4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__question-mark-chat-bubble-solo/20260929T042221Z-thuan-mac/reference/question mark in chat bubble_1af2cc96-98e1-4c11-bd26-fef6f9c101b4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'question-mark-chat-bubble-solo'
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
        self.path('bubble',(10,32),('A',(6,22),16,16,True),('A',(24,6),18,16,True),('A',(42,22),18,16,True),('A',(24,38),18,16,True),('L',(18,38)),('L',(6,42)),('L',(10,32)),closed=True)
        self.path('question',(18,17),('A',(24,12),6,5,True),('A',(30,18),6,6,True),('A',(27,23),6,6,True),('A',(24,27),5,5,False))
        self.add_dot('question-dot',(24,33))

Drawing.exception = {'reason': 'Question-mark dot and hook retain 2-unit ink separation, and enclosure clearances are locally below 4 to preserve a readable full question sign; user authorized native-size visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'e43bbd6bdd6456981eae055fc9188e84b4fdddbb5385d1ca2aa7fa8c6c9a462c'}
