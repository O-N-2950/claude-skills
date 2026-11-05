"""Generate a reproducible inventory of the actual, versioned skill bundles."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inventory(root=ROOT):
    items = []
    for path in sorted(Path(root).glob('*/SKILL.md')):
        raw = path.read_bytes()
        content = raw.decode('utf8')
        if not content.strip():
            raise ValueError(f'empty skill: {path.parent.name}')
        items.append({'name': path.parent.name, 'path': path.relative_to(root).as_posix(),
                      'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
    if not items:
        raise ValueError('no skills found')
    return {'schema': 'neo.skill-catalog.v1', 'count': len(items), 'skills': items}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    generated = json.dumps(inventory(), ensure_ascii=False, indent=2) + '\n'
    path = ROOT / 'catalog.json'
    if args.check:
        if not path.is_file() or path.read_text(encoding='utf8') != generated:
            parser.exit(1, 'catalog.json is stale; run python scripts/catalog.py\n')
        print(f'Catalog verified: {inventory()["count"]} skills')
    else:
        path.write_text(generated, encoding='utf8')


if __name__ == '__main__':
    main()
