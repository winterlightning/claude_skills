"""Closed Eyes with Eyelashes.
Plan: Paired shallow eyelids with a lash attached at each lower midpoint; mirror about x24. Radial envelope22.
Reference construction: eye-closed; human_ref/user.svg.
Reduction: Keep one central lash per lid; the radial envelope preserves the shallow horizontal expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8f73b826-1326-4de9-8ddd-dc0a24d8eacc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/close two eyes_8f73b826-1326-4de9-8ddd-dc0a24d8eacc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'closed-eyes-with-eyelashes'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('closed', 'eyes', 'with', 'eyelashes')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for label,cx in [('left',12),('right',36)]:
            self.add_arc(label+'-lid-a',(cx-8,24),(cx,28),radius_x=8,radius_y=4,sweep=False)
            self.add_arc(label+'-lid-b',(cx,28),(cx+8,24),radius_x=8,radius_y=4,sweep=False)
            self.add_contour(label+'-lid',label+'-lid-a',label+'-lid-b')
            self.add_line(label+'-lash',(cx,28),(cx,34))
            self.relate('connect',label+'-lash',label+'-lid')
