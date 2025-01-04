import time
import psutil
import os
import platform
import subprocess
from multiprocessing import Pool

# CPU Task Function
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i ** 0.5
    return total

# CPU Benchmark
def cpu_benchmark():
    num_processes = psutil.cpu_count(logical=True)
    n = 10**7  # Increased workload
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
    block_size = 10**8  # 100 MB blocks (increased size)
    start_time = time.time()
    try:
        for _ in range(50):  # Up to 5 GB
            data.append(bytearray(block_size))
    except MemoryError:
        pass
    elapsed_time = time.time() - start_time
    print(f"Memory benchmark completed in {elapsed_time:.2f} seconds.")
    return elapsed_time

# Disk Benchmark
def disk_benchmark():
    print("Starting disk benchmark...")
    file_size = 10**9  # 1 GB (increased size)
    filename = "disk_benchmark.tmp"
    data = bytearray(os.urandom(file_size))  # Create a 1 GB random data block

    # Measure write time
    start_time = time.time()
    with open(filename, "wb") as f:
        f.write(data)
    write_time = time.time() - start_time

    # Measure read time
    start_time = time.time()
    with open(filename, "rb") as f:
        f.read()
    read_time = time.time() - start_time

    # Clean up
    os.remove(filename)

    print(f"Disk write completed in {write_time:.2f} seconds.")
    print(f"Disk read completed in {read_time:.2f} seconds.")
    return write_time, read_time

# Grading Results
def grade_result(category, time, thresholds):
    for grade, threshold in thresholds.items():
        if time <= threshold:
            return f"{category}: {grade} ({time:.2f} seconds)"
    return f"{category}: F ({time:.2f} seconds)"

# Disk Details
def get_disk_details():
    try:
        result = subprocess.check_output(["lsblk", "-o", "NAME,ROTA,MODEL,SIZE"], text=True)
        print("\nDisk Details:")
        print(result)
    except Exception as e:
        print(f"Error retrieving disk details: {e}")

# RAM Details
def get_ram_details():
    memory = psutil.virtual_memory()
    print("\nRAM Details:")
    print(f"Total Memory: {memory.total / 1e9:.2f} GB")
    print(f"Available Memory: {memory.available / 1e9:.2f} GB")

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
        "Disk Total": f"{psutil.disk_usage('/').total / 1e9:.2f} GB",
        "Disk Used": f"{psutil.disk_usage('/').used / 1e9:.2f} GB",
        "Disk Free": f"{psutil.disk_usage('/').free / 1e9:.2f} GB",
    }
    for k, v in info.items():
        print(f"{k}: {v}")
    
    get_disk_details()
    get_ram_details()

# Main Function
def main():
    system_info()
    print("\nStarting benchmarks...\n")
    
    # Define grading thresholds
    cpu_thresholds = {"A+": 1.0, "A": 2.0, "B": 4.0, "C": 6.0, "D": 8.0}  # Stricter thresholds
    memory_thresholds = {"A+": 0.5, "A": 1.0, "B": 2.0, "C": 4.0, "D": 6.0}
    disk_thresholds = {"A+": 0.25, "A": 0.5, "B": 1.0, "C": 2.0, "D": 4.0}

    # Run benchmarks
    cpu_time = cpu_benchmark()
    memory_time = memory_benchmark()
    write_time, read_time = disk_benchmark()

    # Grade results
    print("\nBenchmark Results:")
    print(grade_result("CPU", cpu_time, cpu_thresholds))
    print(grade_result("Memory", memory_time, memory_thresholds))
    print(grade_result("Disk Write", write_time, disk_thresholds))
    print(grade_result("Disk Read", read_time, disk_thresholds))

if __name__ == "__main__":
    main()

