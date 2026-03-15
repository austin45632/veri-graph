from pathlib import Path
import os
import re

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = Path(os.environ.get('TRACEABILITY_ROOT', str(DEFAULT_ROOT)))
AUTOMOTIVE_DIR = DATA_ROOT / 'docs/automotive'
AUTOMOTIVE_MATRIX = Path(
    os.environ.get('AUTOMOTIVE_MATRIX', str(DATA_ROOT / 'docs/automotive/automotive-matrix.md'))
)
ID_PATTERNS = {
    'FEAT': re.compile(r'FEAT-\d{3}'),
    'VSTATE': re.compile(r'VSTATE-\d{3}'),
    'SIG': re.compile(r'SIG-\d{3}'),
    'FAULT': re.compile(r'FAULT-\d{3}'),
    'DIAG': re.compile(r'DIAG-\d{3}'),
    'VAR': re.compile(r'VAR-\d{3}'),
    'SG': re.compile(r'SG-\d{3}'),
}
AUTOMOTIVE_SOURCE_RELATIONS = {
    'FEAT': 'belongs_to_feature',
    'VSTATE': 'applies_in_state',
    'SIG': 'depends_on_signal',
    'FAULT': 'covers_fault_reaction',
    'DIAG': 'covers_diagnostic_event',
    'VAR': 'applies_to_variant',
    'SG': 'satisfies_safety_goal',
}
AUTOMOTIVE_PREFIXES = ['FEAT', 'VSTATE', 'SIG', 'FAULT', 'DIAG', 'VAR', 'SG']


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith('|')]
    if len(lines) < 3:
        return []

    headers = [cell.strip() for cell in lines[0].strip('|').split('|')]
    rows = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def collect_ids(directory: Path, prefix: str) -> list[str]:
    if not directory.exists():
        return []
    pattern = ID_PATTERNS[prefix]
    ids = []
    for path in sorted(directory.glob(f'{prefix}-*.md')):
        match = pattern.search(path.read_text(encoding='utf-8'))
        if match:
            ids.append(match.group(0))
    return ids


def collect_automotive_ids(directory: Path) -> dict[str, list[str]]:
    return {prefix: collect_ids(directory, prefix) for prefix in AUTOMOTIVE_PREFIXES}


def build_automotive_report(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    report = {
        'FEAT missing matrix link': [],
        'VSTATE missing matrix link': [],
        'SIG missing matrix link': [],
        'FAULT missing matrix link': [],
        'DIAG missing matrix link': [],
        'VAR missing matrix link': [],
        'SG missing matrix link': [],
        'Automotive unreferenced files': [],
    }
    automotive_ids = collect_automotive_ids(AUTOMOTIVE_DIR)
    referenced_targets = {row.get('target_id') for row in rows}

    for prefix, ids in automotive_ids.items():
        expected_relation = AUTOMOTIVE_SOURCE_RELATIONS[prefix]
        missing_key = f'{prefix} missing matrix link'
        for item_id in ids:
            if not any(
                row.get('source_id') == item_id and row.get('relation') == expected_relation
                for row in rows
            ):
                report[missing_key].append(item_id)
            if item_id not in referenced_targets and not any(row.get('source_id') == item_id for row in rows):
                report['Automotive unreferenced files'].append(item_id)

    return report


def format_report(report: dict[str, list[str]]) -> str:
    lines = []
    for title, items in report.items():
        lines.append(f'[{title}]')
        if items:
            lines.extend(items)
        else:
            lines.append('none')
    return '\n'.join(lines)


def main() -> int:
    if not (AUTOMOTIVE_DIR.exists() and AUTOMOTIVE_MATRIX.exists()):
        print('missing required files or directories')
        return 1

    rows = parse_markdown_table(AUTOMOTIVE_MATRIX.read_text(encoding='utf-8'))
    report = build_automotive_report(rows)
    has_failures = any(report.values())
    automotive_ids = collect_automotive_ids(AUTOMOTIVE_DIR)
    automotive_count = sum(len(ids) for ids in automotive_ids.values())

    if not has_failures:
        print(f'automotive semantics check passed ({automotive_count} automotive nodes)')
        print(format_report(report))
        return 0

    print('automotive semantics check failed')
    print(format_report(report))
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
