"""End-to-end CLI check for legal thresholds beyond Python's default digit cap."""

import json
import subprocess
import sys
from pathlib import Path


ALGORITHM = Path(__file__).resolve().parents[2] / "algorithm.py"
sys.set_int_max_str_digits(0)


def call(payload, extract=False):
    run = subprocess.run(
        [sys.executable, str(ALGORITHM)] + (["--extract"] if extract else []),
        input=json.dumps(payload), text=True, capture_output=True, check=True,
    )
    return json.loads(run.stdout)


def main():
    graph = {"n": 2, "vertices": [0, 1], "edges": [[0, 1]]}
    yes_source = graph | {"k": int("9" * 4300)}
    target = call(yes_source)
    assert target == {"n": 3, "vertices": [0, 1, 2],
                      "edges": [[0, 1], [0, 2], [1, 2]], "K": yes_source["k"] + 3}
    witness = {"parent": [-1, 0, 1]}
    assert 4 <= target["K"]
    recovered = call({"source": yes_source, "target_solution": witness}, True)
    assert sorted(recovered["order"]) == [0, 1]

    no_source = graph | {"k": -int("9" * 4301)}
    assert call(no_source) == {"n": 3, "vertices": [0, 1, 2],
                               "edges": [[0, 1], [0, 2], [1, 2]], "K": 1}
    assert call({"source": no_source, "target_solution": "NO-SOLUTION"}, True) == "NO-SOLUTION"
    print("Large-threshold forward and recovery checks passed")


if __name__ == "__main__":
    main()
