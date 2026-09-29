"""cloud-connected-to-a-two-tier-terminal: Restored the two circular nodes, unequal leads and two terminal tiers; opened the cloud sides to separate its outline from the circuitry.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide cloud original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '825b8945-11e9-428c-b6e8-1d38a40f575a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cloud-connected-to-a-two-tier-terminal/20260928T164600Z-thuan-mac/reference/amazon web service direct connect_825b8945-11e9-428c-b6e8-1d38a40f575a.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'cloud-connected-to-a-two-tier-terminal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cloud', 'connected', 'to', 'a', 'two', 'tier', 'terminal')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for i,(kind,end,*args) in enumerate(steps):
                eid=f'{name}-{i}';members.append(eid)
                if kind=='L':self.add_line(eid,here,end)
                elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        def poly(name,*pts):self.add_polyline(name,*pts,closed=pts[0]==pts[-1])
        def join(a,b):self.relate('connect',a,b)

        path('cloud',(9,26),[('C',(4,17),(6,24),(4,21)),('C',(18,4),(4,9),(10,4)),('C',(31,12),(24,4),(29,7)),('C',(44,19),(38,7),(44,12)),('C',(42,25),(44,22),(43,24))])
        circle('node-left',18,18,3);circle('node-right',32,22,3)
        line('lead-left',(18,21),(18,32));join('lead-left','node-left')
        line('lead-right',(32,25),(32,32));join('lead-right','node-right')
        poly('upper-tier',(14,38),(14,32),(18,32),(32,32),(34,32),(34,38))
        for n in ('lead-left','lead-right'):join(n,'upper-tier')
        poly('lower-tier',(10,44),(10,38),(14,38),(34,38),(38,38),(38,44));join('upper-tier','lower-tier')


Revision.exception = {'reason': 'Preserve two circular network nodes, unequal leads and both terminal tiers beneath the cloud. Use the larger 2px-inset envelope on the 48px canvas, 2px open tier spacing and about 3px local cloud/node spacing. The rings and tiers remain distinct in both themes at native 48px.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': 'e48f72155bfc9a3e3f865366abe2f089f2cbc2cfca4f23b3d969468417955ddd'}
