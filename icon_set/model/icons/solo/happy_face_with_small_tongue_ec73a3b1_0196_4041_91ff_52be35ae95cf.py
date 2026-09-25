"""Round happy face with curved closed eyes, a true curved smile and a small rounded tongue below it.
Keyshape CIRCLE: exact SOLO48 contract envelope.
Construction: Shared human_ref/user.svg: circular head construction; no useful exact Lucide tongue-face match
Omissions: None; head-only icon has no body-gap requirement.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ec73a3b1-0196-4041-91ff-52be35ae95cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face smile tongue_ec73a3b1-0196-4041-91ff-52be35ae95cf.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='happy-face-with-small-tongue'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('happy', 'face', 'with', 'small', 'tongue')
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

        ellipse('face',24,24,20,20)
        for i,x in enumerate((18,30)):
         path(f'eye-{i}',(x-2,17),[('A',(x+2,17),2,2,True)])
        path('smile',(14,25),[('C',(20,27),(15,26),(17,27)),('C',(28,27),(22,28),(26,28)),('C',(34,25),(31,27),(33,26))])
        path('tongue',(20,27),[('L',(20,31)),('A',(28,31),4,4,False),('L',(28,27))]);join('tongue','smile')
