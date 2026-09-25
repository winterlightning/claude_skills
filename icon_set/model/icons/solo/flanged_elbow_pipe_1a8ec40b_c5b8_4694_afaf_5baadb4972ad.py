'A right-angle pipe with broad end flanges, opening left and upward. SQUARE fits the two equal arms. One outline owns collars and concentric radii 8 and 16 about (22,22). Source supplies orientation and flange steps; internal flange seams omitted to keep openings clear. Lucide rectangle-vertical informs continuous outline joins.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a8ec40b-c5b8-4694-afaf-5baadb4972ad'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pipe section_1a8ec40b-c5b8-4694-afaf-5baadb4972ad.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'flanged-elbow-pipe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Curved Elbow Pipe Fitting']
    keywords = []
    def build(self):
        points=[(6,26),(14,26),(14,30),(22,30),(30,22),(30,14),(26,14),(26,6),(42,6),(42,14),(38,14),(38,22),(22,38),(14,38),(14,42),(6,42),(6,26)]
        names=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            name=f'pipe-{i}';names.append(name)
            if i==3: self.add_arc(name,a,b,radius_x=8,sweep=False)
            elif i==11: self.add_arc(name,a,b,radius_x=16,sweep=True)
            else: self.add_line(name,a,b)
        self.add_contour('pipe',*names,closed=True)
