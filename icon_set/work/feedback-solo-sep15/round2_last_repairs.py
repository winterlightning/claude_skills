from pathlib import Path
import json
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
W=Path(__file__).parent;R=json.loads((W/'revisions.json').read_text())
for n,pairs in {87:[('(x(18), 34)','(x(18), 40)')],123:[('(26, 24)','(24, 24)'),('(26, 16)','(24, 16)')],170:[("line('center-collar', (20, 30), (28, 30))",''),("join('center', 'center-collar')",'')]}.items():
 p=W/'snapshot'/R[str(n)]['file'];s=p.read_text()
 for a,b in pairs:
  assert a in s,(n,a);s=s.replace(a,b)
 p.write_text(s)
for p in (W/'snapshot').rglob('*.pyc'):p.unlink()
