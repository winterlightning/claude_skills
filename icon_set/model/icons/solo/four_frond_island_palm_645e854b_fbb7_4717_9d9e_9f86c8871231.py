'A palm tree rises from a low semicircular island on a curved slender trunk. Four broad pointed fronds spread outward from a single junction at its crown.\nPlan: Leaning palm trunk and four curved frond strokes above low island.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '645e854b-fbb7-4717-9d9e-9f86c8871231'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beach palm_645e854b-fbb7-4717-9d9e-9f86c8871231.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-frond-island-palm'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('four', 'frond', 'island', 'palm')

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

        path('trunk',(20,34),[('C',(26,16),(20,26),(24,20))])
        path('upper-left',(26,16),[('C',(6,6),(20,6),(14,6))]);path('upper-right',(26,16),[('C',(42,6),(30,6),(36,6))])
        path('lower-left',(26,16),[('C',(6,24),(18,12),(8,18))]);path('lower-right',(26,16),[('C',(42,24),(34,12),(40,18))])
        for a in ('upper-left','upper-right','lower-left','lower-right'):
         join('trunk',a)
         for b in ('upper-left','upper-right','lower-left','lower-right'):
          if a<b:join(a,b)
        path('island',(6,42),[('C',(20,34),(10,36),(14,34)),('C',(42,42),(30,34),(38,36)),('L',(6,42))],True);join('island','trunk')
