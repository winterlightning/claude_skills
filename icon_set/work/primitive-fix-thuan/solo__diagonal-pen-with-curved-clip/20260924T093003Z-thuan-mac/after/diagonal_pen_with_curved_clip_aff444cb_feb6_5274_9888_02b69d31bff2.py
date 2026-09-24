"""Bad-stroke revision. Lucide pen: rounded cap, long diagonal barrel and separate triangular nib.
Omissions: Clip simplified to one smoothly attached curved stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aff444cb-feb6-5274-9888-02b69d31bff2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-pen-with-curved-clip/20260924T093003Z-thuan-mac/reference/pen_aff444cb-feb6-5274-9888-02b69d31bff2.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-pen-with-curved-clip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('pen',)
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

        # Barrel edges share the 45-degree axis; clip grows from the cap seam.
        path('pen',(34,6),[('A',(42,14),8,8,True),('C',(38,20),(42,17),(40,18)),('L',(20,38)),('L',(6,42)),('L',(10,28)),('L',(28,10)),('C',(34,6),(30,8),(31,6))],True)
        line('cap-seam',(28,10),(38,20));join('pen','cap-seam')
        line('nib-seam',(10,28),(20,38));join('pen','nib-seam')
        path('clip',(38,20),[('C',(42,30),(42,22),(42,26)),('C',(32,40),(42,33),(36,36))])
        join('clip','pen');join('clip','cap-seam')
