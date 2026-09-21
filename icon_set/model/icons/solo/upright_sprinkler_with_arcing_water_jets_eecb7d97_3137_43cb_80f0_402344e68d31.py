'A sprinkler rises on a narrow upright stem above a low rounded base. A shallow nozzle bowl sits at the top, with four curved water jets spreading outward around a central upright stream.\nPlan: Sprinkler on base with five separate water jets; nozzle and stem as attached structure. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eecb7d97-3137-43cb-80f0-402344e68d31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/sprinkler_eecb7d97-3137-43cb-80f0-402344e68d31.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-sprinkler-with-arcing-water-jets'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('upright', 'sprinkler', 'with', 'arcing', 'water', 'jets')

    # Repair: Use one stem stroke and three water jets instead of five, preserving a recognizable spraying sprinkler with a clear nozzle.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        poly('base',(6,42),(24,42),(42,42));line('stem',(24,30),(24,42));join('base','stem')
        path('nozzle',(16,22),[('L',(32,22)),('A',(24,30),8,8,True),('A',(16,22),8,8,True)],True);join('stem','nozzle')
        line('center-jet',(24,6),(24,13))
        path('left-jet',(6,6),[('C',(14,13),(10,6),(14,9))]);path('right-jet',(42,6),[('C',(34,13),(38,6),(34,9))])
