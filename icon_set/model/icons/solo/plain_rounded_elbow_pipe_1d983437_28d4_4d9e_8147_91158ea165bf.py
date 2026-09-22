'A broad plain elbow pipe bending from below toward the right. SQUARE preserves equal arm extent. One contour with concentric elbow radii 18 and 6 around (24,24); matching terminal corners radius 4. Source supplies the broad smooth bend and rounded ends; no omitted identity features. Lucide rectangle-vertical informs tangent line/quarter-circle transitions.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d983437-28d4-4d9e-8147-91158ea165bf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pipe_1d983437-28d4-4d9e-8147-91158ea165bf.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'plain-rounded-elbow-pipe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ['Curved Plumbing Elbow Pipe']
    keywords = []
    def build(self):
        points=[(6,38),(6,24),(24,6),(38,6),(42,10),(42,14),(38,18),(24,18),(18,24),(18,38),(14,42),(10,42),(6,38)]
        arcs={1:(18,True),3:(4,True),5:(4,True),7:(6,False),9:(4,True),11:(4,True)}
        names=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            name=f'pipe-{i}';names.append(name)
            if i in arcs:
                r,sweep=arcs[i];self.add_arc(name,a,b,radius_x=r,sweep=sweep)
            else: self.add_line(name,a,b)
        self.add_contour('pipe',*names,closed=True)
