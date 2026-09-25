'Two tall champagne flutes tilt inward until their rims nearly touch. Each has a liquid line across its narrow bowl above a slender stem and short flat foot.\nPlan: Two inward-tilted flute bowls, narrow stems and angled feet; omit liquid seam.\nConstruction reference: Lucide wine original and atomic-debug: bowl, slender stem and foot; paired tilted construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8af7ae40-ea5a-48d3-bfc6-209e3b88e405'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/champagne cheers_8af7ae40-ea5a-48d3-bfc6-209e3b88e405.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'touching-champagne-flutes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('touching', 'champagne', 'flutes')

    # Repair: Use smooth bowl curves with real stem attachment at the bottom extrema.
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

        path('left',(10,6),[('L',(24,10)),('L',(18,26)),('C',(12,30),(17,30),(14,30)),('C',(6,22),(8,30),(6,26)),('L',(10,6))],True)
        path('right',(24,10),[('L',(38,6)),('L',(42,22)),('C',(36,30),(42,26),(40,30)),('C',(30,26),(34,30),(31,30)),('L',(24,10))],True);join('left','right')
        line('stem-left',(12,30),(8,42));line('stem-right',(36,30),(40,42));join('left','stem-left');join('right','stem-right')
        poly('foot-left',(6,42),(8,42),(16,42));poly('foot-right',(32,42),(40,42),(42,42));join('stem-left','foot-left');join('stem-right','foot-right')
