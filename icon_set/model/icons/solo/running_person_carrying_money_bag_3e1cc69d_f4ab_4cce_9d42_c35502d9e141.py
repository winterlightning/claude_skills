"""Person Running with Money Bag.

Symbol plan: Running stick figure carries sack to the left, bent stride to the right. Head (28,13),r5; torso starts(28,26), exact detached ink gap4. Visible (2,6)-(46,42). Omit dollar mark, fingers and doubled limb outlines.
Construction references: human_ref/full_body_ref.png: circular outlined head and coherent round-ended limbs; human_ref/user.svg: circular head vocabulary.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e1cc69d-f4ab-4cce-9d42-c35502d9e141'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/robber_3e1cc69d-f4ab-4cce-9d42-c35502d9e141.svg'
AUTHOR = 'gpt-6'


class RunningPersonCarryingMoneyBag(Solo48):
    icon_id = 'running-person-carrying-money-bag'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('running', 'person', 'carrying', 'money', 'bag')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        path('head',(23,13), [((33,13),5,5,True),((23,13),5,5,True)],True)
        self.add_line('torso',(28,26),(28,30))
        self.add_line('hip',(28,30),(30,32))
        path('arm-left',(28,26),[(20,26),(14,20)])
        path('arm-right',(28,26),[(36,26),(40,22)])
        path('leg-left',(30,32),[(24,40),(20,40)])
        path('leg-right',(30,32),[(36,40),(44,40)])
        self.add_bezier('sack-left',(14,20),((8,20),(4,26),(4,30)))
        self.add_arc('sack-bottom-0',(4,30),(10,36),radius_x=6,sweep=False)
        self.add_arc('sack-bottom-1',(10,36),(14,32),radius_x=4,sweep=False)
        self.add_line('sack-bottom-2',(14,32),(14,20))
        self.add_contour('sack','sack-left','sack-bottom-0','sack-bottom-1','sack-bottom-2',closed=True)
        for a,b in [('torso','hip'),('torso','arm-left'),('torso','arm-right'),('arm-left','arm-right'),('hip','leg-left'),('hip','leg-right'),('leg-left','leg-right'),('arm-left','sack')]:self.relate('connect',a,b)
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
