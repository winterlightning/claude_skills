"""Closed tactile book with six generic raised marks, no text transcription inferred. Two columns and three rows are a visual tactile cue. Bottom page block and rounded spine. Centerline8,4–40,44.
Lucide construction reference: book.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='47a2b590-49ff-4756-986c-0ff92fb659e6'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/blind book close_47a2b590-49ff-4756-986c-0ff92fb659e6.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/blind book close_47a2b590-49ff-4756-986c-0ff92fb659e6.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/blind book close_47a2b590-49ff-4756-986c-0ff92fb659e6.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='braille-book-solo-b018'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=('braille', 'book')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        path('book',(12,6),[('L',(42,6)),('L',(42,34)),('L',(42,42)),('L',(10,42)),('A',4,4,True,(6,38)),('L',(6,12)),('A',6,6,True,(12,6))],True)
        path('pages',(6,38),[('A',4,4,True,(10,34)),('L',(42,34))]);self.relate('connect','book','pages')
        for x in (15,24,33):
            for y in (16,25):self.add_dot('dot'+str(x)+'-'+str(y),(x,y))
