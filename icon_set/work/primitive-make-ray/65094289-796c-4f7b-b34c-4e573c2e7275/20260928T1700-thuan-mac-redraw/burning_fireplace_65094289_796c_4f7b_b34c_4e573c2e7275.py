"""burning-fireplace: Restored projecting mantel and hearth bands, inset jambs and a clean flame silhouette. Omitted the tiny inner flame to keep the fire open at 48px.
Plan: subject-owned contours, shared connection points, mirrored repeated shapes.
Construction: inspected Lucide warehouse original and atomic-debug; coherent curves and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '65094289-796c-4f7b-b34c-4e573c2e7275'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__burning-fireplace/20260928T164600Z-thuan-mac/reference/inglenook_65094289-796c-4f7b-b34c-4e573c2e7275.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'burning-fireplace'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('burning', 'fireplace')

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

        poly('mantel',(6,6),(42,6),(42,12),(38,12),(10,12),(6,12),(6,6))
        poly('hearth',(6,36),(10,36),(24,36),(38,36),(42,36),(42,42),(6,42),(6,36))
        for x in (10,38):
            line(f'jamb-{x}',(x,12),(x,36));join(f'jamb-{x}','mantel');join(f'jamb-{x}','hearth')
        path('flame',(24,36),[('C',(17,29),(19,36),(16,33)),('C',(23,18),(18,25),(22,22)),('C',(31,29),(27,21),(31,25)),('C',(24,36),(32,33),(29,36))],True);join('flame','hearth')


Revision.exception = {'reason': 'Preserve the projecting mantel and hearth bands that identify a fireplace, with clear 2px interior slots. The asymmetric flame retains an open center and approximately 2.8px or more side clearance. All features read clearly in both themes at native 48px.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': '3f737ea957e8c889bc72df43834a8cdfe70515345c375e1e1a2b7f1fc33f84b8'}
