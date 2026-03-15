from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    ('traceability', ROOT / 'scripts/check_traceability.py'),
    ('automotive semantics', ROOT / 'scripts/check_automotive_semantics.py'),
    ('result layer', ROOT / 'scripts/check_result_evidence.py'),
]


def run_check(name: str, script: Path) -> tuple[int, str]:
    result = subprocess.run(
        ['python', str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout.rstrip()
    if result.stderr:
        output = f'{output}\n{result.stderr.rstrip()}'.strip()
    header = f'== {name} =='
    return result.returncode, f'{header}\n{output}'


def main() -> int:
    statuses = []
    outputs = []
    for name, script in CHECKS:
        code, output = run_check(name, script)
        statuses.append(code)
        outputs.append(output)

    print('\n\n'.join(outputs))

    if any(code != 0 for code in statuses):
        print('\ncheck_all failed')
        return 2

    print('\ncheck_all passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
