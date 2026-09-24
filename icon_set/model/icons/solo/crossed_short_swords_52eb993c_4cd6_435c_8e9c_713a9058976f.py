"""Crossed short swords with equal blade widths, pointed tips, straight guards and rounded outlined grips. Back blade is occluded at the crossing.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: swords: scoped crossing and paired guards; pill: rounded grips
Omissions: Blade center ridges omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '52eb993c-4cd6-435c-8e9c-713a9058976f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antique swords_52eb993c-4cd6-435c-8e9c-713a9058976f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='crossed-short-swords'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('crossed', 'short', 'swords')
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

        path('front',(12,30),[('L',(34,8)),('L',(42,6)),('L',(40,14)),('L',(18,36)),('L',(12,42)),('C',(6,36),(8,42),(6,40)),('L',(12,30))],True)
        path('back-upper',(18,24),[('L',(8,14)),('L',(6,6)),('L',(14,8)),('L',(24,18))]);join('back-upper','front')
        path('back-grip',(24,30),[('L',(36,42)),('C',(42,36),(40,42),(42,40)),('L',(30,24))]);join('back-grip','front')
        line('guard-front',(8,26),(22,40));join('guard-front','front')
        line('guard-back',(26,40),(40,26));join('guard-back','back-grip')
