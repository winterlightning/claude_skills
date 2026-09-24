"""Five-point magic star atop a diagonal wand with an outlined rounded handle.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: star and wand: star outline and diagonal shaft; pill: rounded handle
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2239a15c-dd4c-44b5-99ff-7e5c0c02afee'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-star-wand-with-rounded-handle/20260924T150246Z-thuan-mac/reference/magic wand_2239a15c-dd4c-44b5-99ff-7e5c0c02afee.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-star-wand-with-rounded-handle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('diagonal', 'star', 'wand', 'with', 'rounded', 'handle')
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

        poly('star',(26,6),(32,14),(42,12),(38,22),(42,32),(30,30),(24,40),(20,28),(12,24),(23,19),closed=True)
        path('handle',(20,28),[('L',(6,36)),('C',(13,42),(6,42),(10,42)),('L',(27,35))]);join('handle','star')
