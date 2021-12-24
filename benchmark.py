
import os, re, gc
from time import perf_counter_ns
from collections import defaultdict

from tabulate import tabulate

# Import these outside benchmark to avoid skewing result
import numpy

BENCHMARK_GLOBALS = { "print": lambda *args, **kwargs: None }
MILLISECOND = 10**6
FILENAME_RE = re.compile(r"(\d+)\_(\d)_?(\w+)?\.py")

def benchmark(filename, n=None):
    with open(filename) as file:
        source = file.read()
    
    code = compile(source, filename, "exec")

    # Warmup run / time estimation
    st = perf_counter_ns()
    exec(code, BENCHMARK_GLOBALS)
    et = perf_counter_ns()

    if n is None:
        target_time = 200*MILLISECOND
        n = max(1, target_time // (et - st))

    measurements = []
    for _ in range(n):
        gc.collect()
        st = perf_counter_ns()
        exec(code, BENCHMARK_GLOBALS)
        et = perf_counter_ns()
        measurements.append(et-st)

    return measurements

if __name__ == "__main__":

    import sys

    args = sys.argv
    if len(args) >= 2:
        path = args[1]
        n = int(args[2]) if len(args) > 2 else None
        measurements = benchmark(path, n)
        print(f"{path} :: {min(measurements)//10**3:>10,} µs")
        exit(0)

    paths = []
    for path in os.listdir("."):
        if (match := FILENAME_RE.match(path)):
            day, part, extra = match.groups()
            day, part = map(int, (day, part))
            paths.append((day, part, bool(extra), path))
    paths.sort()

    results = defaultdict(dict)
    for day, part, extra, path in paths:
        print(path, flush=False, end="\t")
        measurements = benchmark(path)
        time_str = f"{min(measurements)//10**3:>10,} µs"
        results[day][part + int(extra)] = time_str
        print(results[day][part + int(extra)])
        # print(f"Puzzle {day:2}.{part} {min(measurements)//10**3:>16,} µs")

    table = [(day, *parts.values()) for day, parts in results.items()]
    print(tabulate(table, headers=("Day", "Part 1", "Part 2", "Extra"), tablefmt="github"))