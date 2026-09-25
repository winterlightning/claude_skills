"""question-and-exclamation-speech-bubbles: Two overlapping rectangular speech bubbles retain an open question hook and a vertical warning mark, with clean round joins and exact spacing.
Lucide construction: messages-square; original and atomic-debug inspected.
Omissions: Separate punctuation dots omitted, matching the supplied thin-line marks.
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46e03166-e81b-449b-9574-b852a8046251'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__question-and-exclamation-speech-bubbles/20260924T171114Z-thuan-mac/reference/conversation question warning_46e03166-e81b-449b-9574-b852a8046251.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'question-and-exclamation-speech-bubbles'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('question', 'and', 'exclamation', 'speech', 'bubbles')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('back',(32,20),(32,8),(4,8),(4,32),(10,32),(10,38),(18,32))
        poly('front',(28,20),(32,20),(44,20),(44,38),(38,38),(38,40),(36,38),(28,38),closed=True);join('back','front')
        path('question',(13,20),[('A',(19,20),3,3,True),('C',(17,24),(19,22),(17,22))])
        line('exclamation',(36,28),(36,30))
