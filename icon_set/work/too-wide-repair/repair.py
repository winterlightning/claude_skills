from pathlib import Path
import json,re,ast
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-wide-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'mapping.json').read_text())
for row in rows:
 n=row['original'];p=Path(row['file']);s=(W/'starting'/p.name).read_text()
 s=re.sub(r"AUTHOR = .*", "AUTHOR = 'gpt-6'",s).replace('Keyshape.VRECT_XL','Keyshape.VRECT_L')
 # Move only the owning outer contour coordinates, retaining interior spacing.
 s=re.sub(r'\((2|46), (\d+)\)',lambda m:'('+{'2':'4','46':'44'}[m[1]]+', '+m[2]+')',s)
 if n in ['construction-hard-hat','external-hard-drive','simple-computer-keyboard','stone-bridge','desktop-hard-drive-enclosure']:
  s=re.sub(r'\((6|42), (\d+)\)',lambda m:'('+{'6':'8','42':'40'}[m[1]]+', '+m[2]+')',s)
 if n=='baseball-cap':
  s=s.replace("radius_x=17, radius_y=17, sweep=False)","radius_x=15, radius_y=17, sweep=False)",1).replace('radius_x=14, radius_y=4','radius_x=12, radius_y=4').replace('radius_x=15, radius_y=6','radius_x=13, radius_y=6')
 if n=='bowler-hat':s=s.replace('(4, 33), (9, 40), 7','(4, 35), (9, 40), 5').replace('(39, 40), (44, 33), 7','(39, 40), (44, 35), 5')
 if n=='bucket-hat':s=s.replace('radius_x=22','radius_x=20')
 if n=='capricorn-zodiac-symbol':
  s=s.replace('(10, 16)','(12, 16)').replace("(30, 30), (44, 30), radius_x=8","(30, 30), (44, 30), radius_x=7").replace("(44, 30), (30, 30), radius_x=8","(44, 30), (30, 30), radius_x=7")
 if n=='construction-hard-hat':s=s.replace('radius_x=12, radius_y=18','radius_x=10, radius_y=18')
 if n in ['cowboy-hat','cowboy-hat-with-band']:s=s.replace('radius_x=22','radius_x=20')
 if n=='curled-centipede':s=s.replace('radius_x=7, radius_y=7','radius_x=6, radius_y=7')
 if n=='genie-oil-lamp':s=s.replace('radius_x=10, radius_y=6','radius_x=8, radius_y=6')
 if n=='ladies-hat-with-bow':s=s.replace('radius_x=22','radius_x=20').replace('(45,','(44,')
 if n in ['laptop-with-flat-base-lip','laptop-with-rounded-base']:
  lines=s.splitlines();s='\n'.join(l.replace('radius_x=8','radius_x=6, radius_y=8') if ('add_arc' in l and ('(44, 32)' in l or '(4, 32)' in l)) else l for l in lines)+'\n'
 if n.startswith('round-bud-vase'):
  s=s.replace('(24, 42)','(24, 44)').replace('radius_x=10, radius_y=10','radius_x=8, radius_y=14').replace("('left', 8, 12)","('left', 11, 15)").replace("('top', 22, 5)","('top', 24, 7)").replace("('right', 40, 9)","('right', 37, 15)").replace("('side', 40, 23)","('side', 37, 29)")
 if n=='simple-computer-keyboard':
  s=s[:s.index("        self.add_dot('key")]+"        for x in (14, 24, 34):\n            self.add_dot(f'key-{x}', (x, 18))\n        self.add_line('spacebar', (14, 30), (34, 30))\n"
 if n=='sombrero':s=s.replace('radius_x=12, radius_y=10','radius_x=10, radius_y=10')
 if n=='squid':s=s.replace('p(22, 38), radius_x=12','p(18, 38), radius_x=8')
 if n=='standing-deer':s=s.replace('radius_x=10, radius_y=7','radius_x=6, radius_y=7')
 if n=='swan-couple-heart':s=s.replace('p(22,','p(20,').replace('p(20, 30), radius_x=10','p(20, 30), radius_x=8, radius_y=10').replace("        self.relate('connect', 'left-swan', 'right-swan')",'')
 if n=='desktop-hard-drive-enclosure':
  s=re.sub(r'\((\d+), (21|31|35)\)',lambda m:'('+m[1]+', '+{'21':'19','31':'33','35':'37'}[m[2]]+')',s).replace("'indicator', (12, 28)","'indicator', (14, 28)")
 if n=='power-supply-unit':
  s=s.replace('(4, 8)','(6, 8)').replace('(44, 8)','(42, 8)').replace('(44, 40)','(42, 40)').replace('(4, 40)','(6, 40)')
  s=s[:s.index("        self.add_arc('fan0'")]+"        self.add_arc('fan-top', (14, 24), (26, 24), radius_x=6)\n        self.add_arc('fan-bottom', (26, 24), (14, 24), radius_x=6)\n        self.add_contour('fan', 'fan-top', 'fan-bottom', closed=True)\n        self.add_line('power-port', (35, 19), (35, 29))\n"
 p.write_text(s)
