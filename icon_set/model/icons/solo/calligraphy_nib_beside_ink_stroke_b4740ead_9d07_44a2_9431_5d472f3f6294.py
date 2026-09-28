"""Diagonal calligraphy nib beside an elongated curled ink stroke; broad nib shoulders and one central slit.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: pen-tool: joined outline and nib slit; source governs separate ink curl
Omissions: Tiny vent omitted to keep slit clear.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4740ead-9d07-44a2-9431-5d472f3f6294'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crafts calligraphy_b4740ead-9d07-44a2-9431-5d472f3f6294.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='calligraphy-nib-beside-ink-stroke'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('calligraphy', 'nib', 'beside', 'ink', 'stroke')
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

        path('nib',(24,25),[('L',(30,8)),('L',(36,6)),('L',(42,12)),('L',(40,19)),('L',(24,25))],True)
        line('slit',(24,25),(33,16));join('slit','nib')
        path('ink',(16,20),[('C',(6,30),(8,23),(6,23)),('L',(6,36)),('A',(12,42),6,6,False),('A',(18,36),6,6,False)])
