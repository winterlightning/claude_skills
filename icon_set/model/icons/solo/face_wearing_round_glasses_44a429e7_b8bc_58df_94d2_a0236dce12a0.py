'Circular face with mirrored round glasses and raised smile. Human reference icon_set/references/human_ref/user.svg supplies the round head vocabulary; no body or head-to-body gap applies. Lucide glasses informs paired lenses and bridge. Pupils and temple arms remain omitted. CIRCLE visible radius 22; SOLO48 stroke 4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44a429e7-b8bc-58df-94d2-a0236dce12a0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/glasses_44a429e7-b8bc-58df-94d2-a0236dce12a0.svg'
AUTHOR = 'gpt-6'

class FaceWearingRoundGlasses(Solo48):
    icon_id = 'face-wearing-round-glasses'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('face', 'glasses', 'spectacles', 'smile', 'avatar', 'person', 'eyewear', 'portrait')

    def build(self):
        # Large equal circular glasses meet at the bridge and join the round head at true shared nodes; Lucide glasses and circle construction.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('face',(4,24),[('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True)],True)
        ellipse('left',14,24,10,10);ellipse('right',34,24,10,10)
        join('left','right');join('face','left');join('face','right')
