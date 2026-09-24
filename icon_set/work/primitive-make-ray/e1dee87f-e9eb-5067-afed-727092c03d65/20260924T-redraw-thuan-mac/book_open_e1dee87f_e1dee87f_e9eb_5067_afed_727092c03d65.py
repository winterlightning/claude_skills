"""Open book with straight outer sides, rounded corners, curved paired leaves and a central binding.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction: book-open: straight sides, paired leaf curves and shared spine
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e1dee87f-e9eb-5067-afed-727092c03d65'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__book-open-e1dee87f/20260924T142441Z-thuan-mac/reference/book open_e1dee87f-e9eb-5067-afed-727092c03d65.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='book-open-e1dee87f'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('book', 'open', 'e1dee87f')
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

        path('spread',(24,14),[('C',(8,8),(20,10),(15,8)),('L',(6,8)),('A',(4,10),2,2,False),('L',(4,34)),('A',(6,36),2,2,False),('L',(8,36)),('C',(24,40),(15,36),(20,37)),('C',(40,36),(28,37),(33,36)),('L',(42,36)),('A',(44,34),2,2,False),('L',(44,10)),('A',(42,8),2,2,False),('L',(40,8)),('C',(24,14),(33,8),(28,10))],True)
        line('spine',(24,14),(24,40));join('spine','spread')
