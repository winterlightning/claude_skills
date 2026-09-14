from pathlib import Path
import json
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
rows={r['original']:Path(r['file']) for r in json.load(open('icon_set/work/too-short-repair/mapping.json'))}
p=rows['person-waving'];s=p.read_text().replace("self.add_polyline('wave', (23, 24), (32, 24), (40, 17), (40, 7))","self.add_line('wave-base', (23, 24), (32, 24))\n        self.add_polyline('wave', (32, 24), (40, 17), (40, 7))\n        self.relate('connect', 'wave-base', 'wave')\n        self.relate('connect', 'wave-base', 'torso')").replace("('left-arm', 'wave', 'legs')","('left-arm', 'wave-base', 'legs')").replace("self.relate('connect', 'left-arm', 'wave')","self.relate('connect', 'left-arm', 'wave-base')");p.write_text(s)
for n in ['tree-pose','standing-full-body-stretch']:
 p=rows[n];s=p.read_text();a=s.index("        self.add_line('arm-l'");b=s.index("        self.add_polyline(",a)
 s=s[:a]+'''        # Separate the rounded side arms from the flat shoulder span so the exact gap is certifiable.
        self.add_line('arm-l', (8, 4), (8, 16))
        self.add_arc('shoulder-l', (8, 16), (16, 24), radius_x=8, sweep=False)
        self.add_contour('left-arm', 'arm-l', 'shoulder-l')
        self.add_line('arms', (16, 24), (24, 24))
        self.add_line('arms-right', (24, 24), (32, 24))
        self.add_arc('shoulder-r', (32, 24), (40, 16), radius_x=8, sweep=False)
        self.add_line('arm-r', (40, 16), (40, 4))
        self.add_contour('right-arm', 'shoulder-r', 'arm-r')
        self.relate('connect', 'left-arm', 'arms')
        self.relate('connect', 'arms', 'arms-right')
        self.relate('connect', 'arms-right', 'right-arm')
'''+s[b:]
 s=s.replace("(24, 44), (24, 44)","(24, 44)")
 p.write_text(s)
