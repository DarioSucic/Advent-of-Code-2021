
import os, re, gc
from time import perf_counter_ns
from collections import defaultdict

from tabulate import tabulate

BENCHMARK_GLOBALS = { "print": lambda *args, **kwargs: None }
MILLISECOND = 10**6
FILENAME_RE = re.compile(r"(\d+)\_(\d)\.py")

def benchmark(filename):
    with open(filename) as file:
        source = file.read()
    
    code = compile(source, filename, "exec")

    # Warmup run / time estimation
    st = perf_counter_ns()
    exec(code, BENCHMARK_GLOBALS)
    et = perf_counter_ns()

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
    tmp = [path for path in os.listdir(".") if FILENAME_RE.match(path)]

    pairs = [(*match.groups(), path) for path in os.listdir(".") if (match := FILENAME_RE.match(path))]
    pairs.sort()


    paths = []
    for path in os.listdir("."):
        if (match := FILENAME_RE.match(path)):
            day, part = map(int, match.groups())
            paths.append((day, part, path))
    paths.sort()

    results = defaultdict(dict)
    for day, part, path in paths:
        print(path, flush=False, end="\t")
        measurements = benchmark(path)
        results[day][part] = f"{min(measurements)//10**3:>10,} µs"
        print(results[day][part])
        # print(f"Puzzle {day:2}.{part} {min(measurements)//10**3:>16,} µs")

    table = [(day, *parts.values()) for day, parts in results.items()]
    print(tabulate(table, headers=("Day", "Part 1", "Part 2"), tablefmt="github"))