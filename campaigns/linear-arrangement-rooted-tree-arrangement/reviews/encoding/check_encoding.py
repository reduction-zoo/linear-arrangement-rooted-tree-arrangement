"""Independent CLI checks for the explicit graph encoding."""

import json
import subprocess
import sys
from pathlib import Path


ALGORITHM = Path(__file__).resolve().parents[2] / "work" / "algorithm.py"
sys.set_int_max_str_digits(0)


def forward(raw_source):
    return subprocess.run(
        [sys.executable, str(ALGORITHM)],
        input=raw_source,
        text=True,
        capture_output=True,
    )


def main():
    for n, edges, k, expected_n in (
        (0, [], -1, 3),
        (0, [], 0, 1),
        (20, [], 0, 20),
        (20, [[0, 19]], 19, 21),
    ):
        source = {"n": n, "vertices": list(range(n)), "edges": edges, "k": k}
        result = forward(json.dumps(source))
        assert result.returncode == 0, result.stderr
        target = json.loads(result.stdout)
        assert target["n"] == expected_n
        assert target["vertices"] == list(range(expected_n))
        assert all(0 <= u < v < expected_n for u, v in target["edges"])

    prefix = '{"n":2,"vertices":[0,1],"edges":[],"k":'
    failures = []
    for digits in ("9" * 4300, "1" + "0" * 4300):
        result = forward(prefix + digits + "}")
        if result.returncode:
            failures.append((len(digits), result.stderr.strip().splitlines()[-1]))
        else:
            target = json.loads(result.stdout)
            assert target["vertices"] == [0, 1]
            assert target["K"] == int(digits) + 1
    assert not failures, failures


if __name__ == "__main__":
    main()
