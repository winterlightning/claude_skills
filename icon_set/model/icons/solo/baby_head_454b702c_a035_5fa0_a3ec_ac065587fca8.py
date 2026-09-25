"""A circular baby face without ears, one curved hair stroke and an open smile, matching the saved feedback.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'

class BabyHead(Solo48):
    icon_id = 'baby-head'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('baby', 'head', 'sub icon')

    def build(self):
        # Symbol plan: A circular baby face without ears, one curved hair stroke and an open smile, matching the saved feedback.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        circle('head',24,24,20)
        path('hair',(20,15),[('C',(28,15),(22,13),(26,13))])
        dot('eye-left',(16,24));dot('eye-right',(32,24))
        self.add_arc('smile',(20,33),(28,33),radius_x=6,radius_y=3,sweep=False)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('5393b57b-1ff9-4e16-b855-128e09e91ba7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/baby face_5393b57b-1ff9-4e16-b855-128e09e91ba7.svg')]
