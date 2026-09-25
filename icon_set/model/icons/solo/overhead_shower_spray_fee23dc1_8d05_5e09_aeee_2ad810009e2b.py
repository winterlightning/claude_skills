"""Overhead Shower Spray.

Plan: Centered dome, vertical feed and mirrored three-stream spray. Bounds (8,4)-(40,44).
Construction: Lucide shower-head dome and pipe, source vertical rain-shower silhouette.
Reduction: Collar omitted, one long stroke for each of three water streams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'fee23dc1-8d05-5e09-aeee-2ad810009e2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom shower head_fee23dc1-8d05-5e09-aeee-2ad810009e2b.svg'
AUTHOR = 'gpt-6'


class IconOverheadShowerSpray(Solo48):
    icon_id = 'overhead-shower-spray'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('overhead', 'shower', 'spray')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('dome',(8,22),[('A',(24,12),16,10,True),('A',(40,22),16,10,True),('L',(8,22))],True)
        self.add_line('pipe',(24,4),(24,12));self.relate('connect','pipe','dome')
        for n,a,b in [('left',(14,32),(10,44)),('center',(24,32),(24,44)),('right',(34,32),(38,44))]:self.add_line('water-'+n,a,b)
