#!/usr/bin/env python3
"""Package the committed Vultuk plugin without marketplace/repository wrappers."""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile


def main():
    root = Path(__file__).resolve().parents[1]
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    # git archive includes only committed files and excludes unrelated local data.
    payload = subprocess.check_output(
        ['git', 'archive', '--format=tar.gz', f'{revision}:plugins/vultuk'], cwd=root
    )
    with tarfile.open(fileobj=io.BytesIO(payload), mode='r:gz') as archive:
        members = archive.getmembers()
        for member in members:
            path = Path(member.name)
            if path.is_absolute() or '..' in path.parts or not (member.isfile() or member.isdir()):
                raise ValueError(f'Unsafe archive member: {member.name}')
        manifest = json.load(archive.extractfile('plugin.json'))
        if manifest['name'] != 'vultuk' or manifest['$schema'] != 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':
            raise ValueError('Unexpected plugin manifest')
        names = {m.name for m in members}
        skills = [n for n in names if n.startswith('skills/') and n.endswith('/SKILL.md')]
        if not skills:
            raise ValueError('Plugin has no skills')
        for skill in skills:
            if str(Path(skill).parent / 'LICENSE') not in names:
                raise ValueError(f'Missing imported skill license: {skill}')
    output = root / 'dist'
    output.mkdir(exist_ok=True)
    asset = output / 'vultuk.tar.gz'
    asset.write_bytes(payload)
    (output / 'vultuk.tar.gz.sha256').write_text(
        f'{hashlib.sha256(payload).hexdigest()}  {asset.name}\n'
    )
    print(f'Packaged Vultuk {manifest["version"]} at {revision}: {len(skills)} skills')


if __name__ == '__main__':
    main()
