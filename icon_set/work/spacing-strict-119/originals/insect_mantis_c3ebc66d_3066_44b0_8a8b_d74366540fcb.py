"""Connected mantis head: arched antennae join the brow, and hooked forelegs join the eyes. Mirrored on x=24; SQUARE extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3ebc66d-3066-44b0-8a8b-d74366540fcb'
SOURCE_PATH = 'pictographic-primitives/animals/insect mantis_c3ebc66d-3066-44b0-8a8b-d74366540fcb.svg'
AUTHOR = 'gpt-6'


class PrayingMantisHead(Solo48):
    icon_id = 'praying-mantis-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('mantis', 'praying mantis', 'insect', 'head', 'claws', 'antennae', 'bug', 'predator')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('eye-left-0',(11, 15),(14, 18),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-left-1',(14, 18),(11, 21),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-left-2',(11, 21),(8, 18),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-left-3',(8, 18),(11, 15),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-right-0',(37, 15),(40, 18),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-right-1',(40, 18),(37, 21),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-right-2',(37, 21),(34, 18),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_arc('eye-right-3',(34, 18),(37, 15),radius_x=3,radius_y=3,large_arc=False,sweep=True)
        self.add_line('brow-left',(11, 15),(20, 15))
        self.add_line('brow-center',(20, 15),(28, 15))
        self.add_line('brow-right',(28, 15),(37, 15))
        self.add_line('face-1',(11, 21),(24, 29))
        self.add_line('face-2',(24, 29),(37, 21))
        self.add_bezier('antenna-left',(20, 8),*(((18.29132138, 6.59041206), (15.71849104, 6), (13.0, 6)), ((10.28150896, 6), (7.70867862, 6.59041206), (6, 8))))
        self.add_bezier('claw-upper-left',(11, 21),*(((7.61252992, 23.20847304), (6, 27.99838774), (6, 33)),))
        self.add_bezier('claw-lower-left',(6, 33),*(((6, 36.21886761), (6.24806195, 39.4273707), (7, 42)),))
        self.add_line('claw-tip-left',(7, 42),(15, 34))
        self.add_bezier('antenna-right',(28, 8),*(((29.70867862, 6.59041206), (32.28150896, 6), (35.0, 6)), ((37.71849104, 6), (40.29132138, 6.59041206), (42, 8))))
        self.add_bezier('claw-upper-right',(37, 21),*(((40.38747008, 23.20847304), (42, 27.99838774), (42, 33)),))
        self.add_bezier('claw-lower-right',(42, 33),*(((42, 36.21886761), (41.75193805, 39.4273707), (41, 42)),))
        self.add_line('claw-tip-right',(41, 42),(33, 34))
        self.add_line('antenna-stem-left',(20, 15),(20, 8))
        self.add_line('antenna-stem-right',(28, 15),(28, 8))
        self.add_contour('eye-left',*('eye-left-0', 'eye-left-1', 'eye-left-2', 'eye-left-3'),closed=True)
        self.add_contour('eye-right',*('eye-right-0', 'eye-right-1', 'eye-right-2', 'eye-right-3'),closed=True)
        self.add_contour('brow',*('brow-left', 'brow-center', 'brow-right'),closed=False)
        self.add_contour('face',*('face-1', 'face-2'),closed=False)
        self.add_contour('claw-left',*('claw-upper-left', 'claw-lower-left'),closed=False)
        self.add_contour('claw-right',*('claw-upper-right', 'claw-lower-right'),closed=False)
        self.relate('connect',*('brow', 'eye-left'))
        self.relate('connect',*('brow', 'eye-right'))
        self.relate('connect',*('face', 'eye-left'))
        self.relate('connect',*('face', 'eye-right'))
        self.relate('connect',*('claw-left', 'eye-left'))
        self.relate('connect',*('claw-left', 'face'))
        self.relate('connect',*('claw-left', 'claw-tip-left'))
        self.relate('connect',*('claw-right', 'eye-right'))
        self.relate('connect',*('claw-right', 'face'))
        self.relate('connect',*('claw-right', 'claw-tip-right'))
        self.relate('connect',*('antenna-stem-left', 'brow'))
        self.relate('connect',*('antenna-stem-left', 'antenna-left'))
        self.relate('connect',*('antenna-stem-right', 'brow'))
        self.relate('connect',*('antenna-stem-right', 'antenna-right'))
