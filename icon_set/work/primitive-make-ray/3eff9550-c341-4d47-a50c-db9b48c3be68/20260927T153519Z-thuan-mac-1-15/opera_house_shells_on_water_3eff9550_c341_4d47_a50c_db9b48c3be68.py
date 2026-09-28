'opera-house-shells-on-water: Restore overlapping curved sail roofs over a low waterfront base, with a separate water ripple. Repaired original in place.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3eff9550-c341-4d47-a50c-db9b48c3be68'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__opera-house-shells-on-water/20260927T153322Z-thuan-mac-1/reference/sydney opera house_3eff9550-c341-4d47-a50c-db9b48c3be68.svg'
AUTHOR = "gpt-6"

class OperaHouseShellsOnWater(Solo48):
    icon_id = 'opera-house-shells-on-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('sydney opera house', 'australia', 'shells', 'sails', 'harbour', 'water', 'landmark', 'cloud')

    def build(self):
        # Three overlapping sail roofs, a low waterfront, and the reference cloud.
        def path(name, start, commands, closed=False):
            ids=[];here=start
            for n,(kind,end,*args) in enumerate(commands):
                eid=f'{name}-{n}'
                if kind=='L': self.add_line(eid,here,end)
                else: self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        path('roofs',(6,31),[
            ('C',(18,31),(9,22),(14,23)),
            ('L',(22,18)),
            ('C',(34,31),(28,19),(31,26)),
            ('L',(42,31))])
        cloud_points=((37,6),(42,10),(37,14),(32,10))
        for n,start in enumerate(cloud_points):
            self.add_arc(f'cloud-{n}',start,cloud_points[(n+1)%4],radius_x=5,radius_y=4,sweep=True)
        self.add_contour('cloud',*(f'cloud-{n}' for n in range(4)),closed=True)
        self.add_bezier('water-left',(6,42),((12,39),(18,39),(24,42)))
        self.add_bezier('water-right',(24,42),((30,39),(36,39),(42,42)))
        self.add_contour('water','water-left','water-right')
