"""Circular squeeze bulb and slender diagonal nozzle joined with smooth shoulders and a rounded tip.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: syringe and pill: parallel diagonal nozzle and curved tip
Omissions: Neck ridges omitted; continuous silhouette retains bulb identity.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9212f764-8dab-491c-8848-a82fe8880545'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bulb-syringe/20260924T142441Z-thuan-mac/reference/enema_9212f764-8dab-491c-8848-a82fe8880545.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bulb-syringe'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('bulb', 'syringe')
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

        path('outline',(6,28),[('A',(20,14),14,14,True),('C',(26,14),(24,14),(24,16)),('L',(34,6)),('C',(42,12),(37,6),(42,9)),('L',(32,22)),('C',(34,28),(30,24),(34,24)),('A',(20,42),14,14,True),('A',(6,28),14,14,True)],True)
