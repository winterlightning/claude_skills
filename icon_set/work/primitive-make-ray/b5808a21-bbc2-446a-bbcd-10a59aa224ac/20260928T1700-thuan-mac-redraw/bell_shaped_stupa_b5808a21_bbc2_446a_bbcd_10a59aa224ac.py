"""bell-shaped-stupa: Restored the tapering pointed spire, broad bell dome and projecting plinth with symmetric curved shoulders.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide bell original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b5808a21-bbc2-446a-bbcd-10a59aa224ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bell-shaped-stupa/20260928T164600Z-thuan-mac/reference/wat phra kaew_b5808a21-bbc2-446a-bbcd-10a59aa224ac.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'bell-shaped-stupa'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bell', 'shaped', 'stupa')

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

        path('dome',(10,36),[('C',(18,20),(10,28),(13,23)),('A',(30,20),10,6,True),('C',(38,36),(35,23),(38,28))])
        poly('spire',(18,20),(24,4),(30,20));join('spire','dome')
        poly('plinth',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),(8,36));join('plinth','dome')
