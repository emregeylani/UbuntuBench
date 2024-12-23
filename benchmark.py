import time
import psutil
import os
import platform
from multiprocessing import Pool

# CPU task for benchmarking
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i ** 0.5
    return total

# CPU Benchmark
def cpu_benchmark():
    num_processes = psutil.cpu_count(logical=True)
    n = 10**6
    print("Starting CPU benchmark...")
    start_time = time.time()
    with Pool(num_processes) as pool:
        pool.map(cpu_task, [n] * num_processes)
    elapsed_time = time.time() - start_time
    print(f"CPU benchmark completed in {elapsed_time:.2f} seconds.")
    return elapsed_time

# Memory Benchmark
def memory_benchmark():
    print("Starting memory benchmark...")
    data = []
    block_size = 10**7  # 10 MB blocks
    start_time = time.time()
    try:
        for _ in range(100):  # Up to 1 GB
            data.append(bytearray(block_size))
    except MemoryError:
        pass
    elapsed_time = time.time() - start_time
    print(f"Memory benchmark completed in {elapsed_time:.2f} seconds.")
    return elapsed_time

# Disk Benchmark
def disk_benchmark():
    print("Starting disk benchmark...")
    file_size = 10**7  # 10 MB
    filename = "disk_benchmark.tmp"
    data = bytearray(os.urandom(file_size))

    start_time = time.time()
    with open(filename, "wb") as f:
        f.write(data)
    write_time = time.time() - start_time

    start_time = time.time()
    with open(filename, "rb") as f:
        f.read()
    read_time = time.time() - start_time

    os.remove(filename)
    print(f"Disk write completed in {write_time:.2f} seconds.")
    print(f"Disk read completed in {read_time:.2f} seconds.")
    return write_time, read_time

# System Info
def system_info():
    print("Gathering system information...")
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "Memory": f"{psutil.virtual_memory().total / 1e9:.2f} GB",
    }
    for k, v in info.items():
        print(f"{k}: {v}")

# Main Function
def main():
    system_info()
    print("\nStarting benchmarks...\n")
    cpu_time = cpu_benchmark()
    memory_time = memory_benchmark()
    write_time, read_time = disk_benchmark()

    print("\nBenchmark Results:")
    print(f"CPU Time: {cpu_time:.2f} seconds")
    print(f"Memory Time: {memory_time:.2f} seconds")
    print(f"Disk Write Time: {write_time:.2f} seconds")
    print(f"Disk Read Time: {read_time:.2f} seconds")

if __name__ == "__main__":
    main()

