import subprocess,sys,time
from pathlib import Path
paths=['icon_set/model/icons/solo/litter_tray_with_slotted_scoop_e6e7ff28_6ade_4296_95f7_4a6c7bd1ce2a.py','icon_set/model/icons/solo/open_front_hooded_cloak_a31f3f41_e636_492d_ad83_a82ed5593583.py','icon_set/model/icons/solo/pick_entering_open_padlock_7f4d0d07_e981_4efd_ae8c_b673077a9b75.py']
cmd=[sys.executable,'-m','icon_set','build','--no-png','--no-report']
for p in paths:cmd+=['--icon',p]
for attempt in range(40):
 result=subprocess.run(cmd,capture_output=True,text=True)
 output=result.stdout+result.stderr
 if 'Build output is busy' not in output:
  Path(__file__).with_name('build-result.txt').write_text(output)
  print(output,flush=True);sys.exit(result.returncode)
 print('Shared output busy; waiting for active build.',flush=True);time.sleep(15)
print('Shared output remained busy; no build completed.',flush=True);sys.exit(2)
