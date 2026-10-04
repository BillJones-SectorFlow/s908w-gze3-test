#!/usr/bin/env python3
"""Prepare a GitHub upload folder; performs no network calls or phone operations."""
import argparse, hashlib, json, re, shutil
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('github_username')
p.add_argument('repository',nargs='?',default='s908w-gze3-test')
a=p.parse_args()
if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*',a.github_username):p.error('invalid GitHub username')
if not re.fullmatch(r'[A-Za-z0-9_.-]+',a.repository):p.error('invalid repository name')
base=Path(__file__).resolve().parent
m=json.loads((base/'support/targets-v3.json').read_text())
for target in m['payloads']:
 for kind in ('exploit','kernelsu'):
  artifact=target[kind]
  filename=artifact['url'].rsplit('/',1)[1]
  file=base/'artifacts'/filename
  if file.stat().st_size != artifact['size'] or hashlib.sha256(file.read_bytes()).hexdigest()!=artifact['sha256']:
   raise SystemExit(f'Artifact failed verification: {filename}')
  artifact['url']=f'https://raw.githubusercontent.com/{a.github_username}/{a.repository}/main/artifacts/{filename}'
out=base/'upload-to-github'
(out/'support').mkdir(parents=True,exist_ok=True)
shutil.copytree(base/'artifacts',out/'artifacts',dirs_exist_ok=True)
(out/'support/targets-v3.json').write_text(json.dumps(m,indent=2)+'\n')
print(f'Upload the artifacts and support folders inside: {out}')
print(f'GitHub repository: https://github.com/{a.github_username}/{a.repository}')
print(f'Next Payload Sources repository: {a.github_username}/{a.repository}; branch: main')
