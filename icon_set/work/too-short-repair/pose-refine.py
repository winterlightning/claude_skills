from pathlib import Path
import json
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
rs={r['original']:Path(r['file']) for r in json.load(open('icon_set/work/too-short-repair/mapping.json'))}
p=rs['chair-pose'];s=p.read_text();s=s[:s.index('    def build')]+'''    def build(self):
        # Human reference: circular head, raised arm, bent hips/knees; exact side gap 8.
        self.add_arc('head-top', (8, 14), (14, 14), radius_x=3)
        self.add_arc('head-bottom', (14, 14), (8, 14), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arm', (22, 4), (22, 22))
        self.add_polyline('body', (22, 22), (30, 30), (17, 30), (24, 44))
        self.add_line('feet', (24, 44), (40, 44))
        self.relate('connect', 'arm', 'body')
        self.relate('connect', 'body', 'feet')
''';p.write_text(s)
p=rs['mountain-pose-raised-arms'];s=p.read_text();ref=rs['standing-full-body-stretch'].read_text();a=ref.index("        # Separate");b=ref.index("        self.add_polyline('torso'",a)
x=s.index("        self.add_polyline('arms'");y=s.index("        self.add_line('body'",x);s=s[:x]+ref[a:b]+s[y:];s=s.replace('(21, 10)','(21, 13)').replace('(27, 10)','(27, 13)');p.write_text(s)
p=rs['security-officer'];s=p.read_text().replace("(20, 44), (20, 30), (24, 30), (28, 36), (32, 30), (34, 30)","(20, 44), (20, 29), (34, 29)").replace("(34, 30), (40, 36)","(34, 29), (40, 35)").replace('(40, 36)','(40, 35)').replace('(20, 30)','(20, 29)');p.write_text(s)
p=rs['woman-figure'];s=p.read_text().replace('(20, 31)','(20, 30)').replace('(28, 31)','(28, 30)');p.write_text(s)
