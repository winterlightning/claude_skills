'A barn has a high angular gambrel roof and straight outer walls. A small square loft window sits above a wide doorway, whose two diagonal braces cross across the lower opening.\nPlan: Gambrel barn contour; large cross-braced doorway without tiny loft detail.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab6f847e-97f6-4764-91e7-6c7ab7f8aacf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/ranch_ab6f847e-97f6-4764-91e7-6c7ab7f8aacf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'barn-with-cross-braced-doors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('barn', 'with', 'cross', 'braced', 'doors')

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

        poly('barn',(6,42),(6,22),(14,12),(24,6),(34,12),(42,22),(42,42),(34,42),(14,42),(6,42))
        poly('door',(14,42),(14,26),(34,26),(34,42));join('door','barn')
        poly('brace',(14,26),(24,34),(34,42));poly('brace2',(34,26),(24,34),(14,42));join('brace','brace2');join('brace','door');join('brace','barn');join('brace2','door');join('brace2','barn')
