from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c39f3f9-2463-5d7d-b812-76671198a134'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/grid ruler_5c39f3f9-2463-5d7d-b812-76671198a134.svg'
AUTHOR = 'gpt-6'


class DraftingGridWithLShapedRuler(Solo48):
    icon_id = 'drafting-grid-with-l-shaped-ruler'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('grid', 'ruler', 'drafting', 'measure', 'corner', 'geometry', 'layout', 'tool')

    def build(self) -> None:
        # Repeated 9-unit drafting mesh; separate 8-unit L ruler with full band ticks.
        for axis in ('x','y'):
            for p in (6,15,24):
                a,b=((p,6),(p,24)) if axis=='x' else ((6,p),(24,p))
                self.add_line(f'{axis}-{p}',a,b)
        for x in (6,15,24):
            for y in (6,15,24):self.relate('connect',f'x-{x}',f'y-{y}')
        self.add_line('ruler-top-1',(34,6),(42,6))
        self.add_line('ruler-top-2',(42,6),(42,38))
        self.add_arc('ruler-corner',(42,38),(38,42),radius_x=4)
        points=[(38,42),(6,42),(6,34),(34,34),(34,6)]
        for n,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'ruler-bottom-{n}',a,b)
        self.add_contour('ruler','ruler-top-1','ruler-top-2','ruler-corner',*[f'ruler-bottom-{n}' for n in range(1,5)],closed=True)
        for p in (14,22):
            for axis,a,b in [('x',(34,p),(42,p)),('y',(p,34),(p,42))]:
                name=f'tick-{axis}-{p}';self.add_line(name,a,b);self.relate('connect',name,'ruler')
