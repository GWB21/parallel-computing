import multiprocessing as mp
import time
import math


def complex_calculation(x):
    # 계산 집약적인 작업을 시뮬레이션
    return sum(math.sin(math.sqrt(i * x)) for i in range(100000))


def parallel_process(arr, num_processes):
    pool = mp.Pool(processes=num_processes)
    results = pool.map(complex_calculation, arr)
    pool.close()
    pool.join()
    return sum(results)


def measure_performance(arr, max_cores):
    results = []
    for cores in range(1, max_cores + 1, 5):
        start_time = time.time()
        result = parallel_process(arr, cores)
        end_time = time.time()
        elapsed_time = end_time - start_time
        results.append((cores, elapsed_time))
    return results


if __name__ == '__main__':
    # 작업량을 늘리기 위해 더 큰 배열 사용
    arr = list(range(1000))

    max_cores = mp.cpu_count()

    print(f"시스템의 총 코어 수: {max_cores}")
    print("\n코어 수 | 실행 시간(초)")
    print("-" * 25)

    results = measure_performance(arr, max_cores)

    for cores, elapsed_time in results:
        print(f"{cores:7d} | {elapsed_time:13.4f}")

    # 속도 향상 계산
    single_core_time = results[0][1]
    max_speedup = single_core_time / min(time for _, time in results)

    print(f"\n최대 속도 향상: {max_speedup:.2f}배")