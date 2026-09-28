"""Braille book with rounded binding and six tactile dots arranged in a clear two-column series.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: book: continuous spine and rounded lower page turn
Omissions: Reference dots regularized as generic Braille cells, no text transcription.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47a2b590-49ff-4756-986c-0ff92fb659e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/blind book close_47a2b590-49ff-4756-986c-0ff92fb659e6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='braille-book-batch-020-09'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('braille', 'book', 'batch', '020', '09')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('right-bottom',(40,4),[('L',(40,44)),('L',(12,44)),('A',(8,40),4,4,True),('A',(12,36),4,4,True)])
        path('spine',(8,40),[('L',(8,10)),('A',(14,4),6,6,True)]);join('spine','right-bottom')
        line('top',(14,4),(40,4));join('top','spine');join('top','right-bottom')
        line('page',(12,36),(40,36));join('page','right-bottom')
        for col in range(2):
         for row in range(3):self.add_dot(f'dot-{col}-{row}',(19+10*col,12+8*row))
