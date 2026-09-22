from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '89ad6115-4299-4633-9b15-29ffb24ba379'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/ac cool_89ad6115-4299-4633-9b15-29ffb24ba379.svg'
AUTHOR = 'gpt-6'

class AirConditionerCoolingMode(Solo48):
    """A wall-mounted air conditioner emits cool air around a snowflake."""
    icon_id = 'air-conditioner-cooling-mode'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/appliances'
    aliases = ('ac-cool',)
    keywords = ('air conditioning', 'cooling', 'snowflake', 'climate')

    def build(self):
        # Plan: rounded housing owns one grille; lower row owns a six-ray
        # snowflake and two instances of a smooth airflow wave. Housing and
        # snowflake mirror about x=24; waves keep the source's same-way flow.
        # SQUARE ink extremes (4,4)-(44,44); centerline (6,6)-(42,42).
        left, right, top, bottom, r = 6, 42, 6, 24, 4
        nodes = [(left+r,top),(right-r,top),(right,top+r),
                 (right,bottom-r),(right-r,bottom),(left+r,bottom),
                 (left,bottom-r),(left,top+r)]
        ids=[]
        for i,start in enumerate(nodes):
            end=nodes[(i+1)%8]; name=f'housing-{i}';ids.append(name)
            if i%2: self.add_arc(name,start,end,radius_x=r)
            else: self.add_line(name,start,end)
        self.add_contour('housing',*ids,closed=True)
        self.add_line('grille',(15,15),(33,15))
        center=(24,37)
        tips=[(24,32),(24,42),(18,34),(30,40),(18,40),(30,34)]
        for i,tip in enumerate(tips):
            self.add_line(f'crystal-ray-{i}',center,tip)
        for i in range(6):
            for j in range(i):
                self.relate('connect',f'crystal-ray-{i}',f'crystal-ray-{j}')
        for i,x in enumerate((8,40)):
            self.add_bezier(f'airflow-{i}',(x,32),
                ((x-4,35),(x+4,39),(x,42)))
