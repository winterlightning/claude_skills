"""Broad crescent curls around the lower-left of a separate upright five-point star. Directional crescent follows the source.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: moon and star: coherent crescent curves and five-point contour
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b261f656-d077-46a8-afd0-2ebb46927dab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/star and crescent_b261f656-d077-46a8-afd0-2ebb46927dab.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='crescent-moon-beside-five-point-star'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('crescent', 'moon', 'beside', 'five', 'point', 'star')
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

        path('moon',(24,6),[('C',(6,24),(14,6),(6,14)),('C',(24,42),(6,34),(14,42)),('C',(42,34),(32,42),(38,39)),('C',(15,24),(27,42),(15,34)),('C',(24,6),(15,16),(18,10))],True)
        poly('star',(33,9),(36,16),(42,16),(37,21),(39,26),(33,23),(27,26),(29,21),(26,16),(31,16),closed=True)
