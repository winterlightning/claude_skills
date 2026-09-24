"""Revision for bad-stroke feedback. Lucide wrench: open jaws and smoothly flowing tool shoulders.
Omissions: Handle thickness simplified to two open curved strokes; retains asymmetric curved forceps.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c9bcc56f-bc17-4b53-9088-582efa893f7d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dental-extraction-forceps-open-jaws/20260924T092136Z-thuan-mac/reference/instrument tooth_c9bcc56f-bc17-4b53-9088-582efa893f7d.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'dental-extraction-forceps-open-jaws'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('instrument', 'tooth')
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

        # Two tool arms cross at a shared mechanical pivot; asymmetric hooked jaws.
        path('arm-front',(18,42),[('C',(30,24),(25,36),(30,30)),('C',(36,6),(28,15),(32,9))])
        path('arm-back',(6,34),[('C',(30,24),(13,26),(23,25)),('C',(42,10),(38,22),(42,18))])
        join('arm-front','arm-back')
