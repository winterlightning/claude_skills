"""closed-sectional-garage-door: Restored the outlined overhead casing and projecting ground line, with two evenly spaced seams defining three door panels.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide warehouse original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8cdf3f7f-a05b-585c-bc1b-60e8dd63c214'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-sectional-garage-door/20260928T164600Z-thuan-mac/reference/garage door closed_8cdf3f7f-a05b-585c-bc1b-60e8dd63c214.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'closed-sectional-garage-door'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('closed', 'sectional', 'garage', 'door')

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

        poly('casing',(6,6),(42,6),(42,14),(38,14),(10,14),(6,14),(6,6))
        for x in (10,38):
            poly(f'jamb-{x}',(x,14),(x,23),(x,32),(x,42));join(f'jamb-{x}','casing')
        for y in (23,32):
            line(f'seam-{y}',(10,y),(38,y))
            for x in (10,38): join(f'seam-{y}',f'jamb-{x}')
        poly('ground',(6,42),(10,42),(38,42),(42,42))
        for x in (10,38):join('ground',f'jamb-{x}')
