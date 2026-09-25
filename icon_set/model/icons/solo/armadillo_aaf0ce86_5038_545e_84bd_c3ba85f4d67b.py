"""Low domed shell with two curved bands, pointed head, ear, two feet and tapered tail.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction: No useful exact Lucide match; source silhouette and shared shell parameters.
Omissions: Far-side feet omitted at native size.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aaf0ce86-5038-545e-84bd-c3ba85f4d67b'
SOURCE_PATH = 'pictographic-primitives/animals/armadillo_aaf0ce86-5038-545e-84bd-c3ba85f4d67b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='armadillo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases=()
    keywords=('armadillo',)
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

        path('shell',(14,32),[('C',(15,22),(14,29),(14,25)),('C',(24,8),(17,13),(18,8)),('C',(34,12),(28,8),(32,9)),('C',(40,28),(38,17),(40,21)),('C',(32,32),(40,31),(36,32)),('L',(14,32))],True)
        path('head',(15,22),[('L',(9,15)),('L',(9,22)),('L',(4,28)),('C',(14,32),(6,31),(10,32))]);join('head','shell')
        path('band-one',(24,8),[('C',(24,24),(26,12),(26,18))]);join('band-one','shell')
        path('band-two',(34,12),[('C',(34,24),(35,16),(35,20))]);join('band-two','shell')
        poly('front-foot',(17,32),(15,40),(19,40));join('front-foot','shell')
        poly('rear-foot',(31,32),(33,40),(37,40));join('rear-foot','shell')
        path('tail',(40,28),[('C',(44,36),(40,33),(41,36))]);join('tail','shell')
