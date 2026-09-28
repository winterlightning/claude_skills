"""Bad-stroke revision. Lucide skull: restrained eye socket detail; supplied side-view dinosaur reference owns silhouette.
Omissions: Nostril and detached neck/shoulder marks omitted to preserve the skull opening.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f8b2772e-1a7e-4a46-b432-a5aa1ea004a8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dinosaur-skull/20260924T093003Z-thuan-mac/reference/dinosaur skull fossil_f8b2772e-1a7e-4a46-b432-a5aa1ea004a8.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'dinosaur-skull'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dinosaur', 'skull', 'fossil')
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Long snout and a heavy lower jaw; rounded rear cranium, single eye socket.
        path('skull',(28,4),[('A',(40,16),12,12,True),('L',(40,32)),('A',(28,44),12,12,True),('L',(14,44)),('C',(8,36),(10,44),(8,40)),('L',(24,36)),('L',(28,28)),('L',(20,28)),('L',(8,26)),('L',(10,14)),('C',(18,7),(12,10),(15,8)),('L',(26,4)),('L',(28,4))],True)
        circle('eye',28,16,3)
