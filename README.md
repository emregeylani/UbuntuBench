# Laptop Performance Benchmark

This Python script benchmarks the performance of your laptop running Ubuntu (Budgie). It evaluates CPU, memory, and disk performance, and provides system information for reference.

## Features

- **CPU Benchmark**: Measures the computation time using parallel processes.
- **Memory Benchmark**: Tests memory allocation and performance.
- **Disk Benchmark**: Evaluates disk read/write speeds using temporary files.
- **System Information**: Displays details about your operating system, processor, memory, and more.

## Prerequisites

Ensure you have Python 3 installed on your system. The script also requires the `psutil` library, which can be installed using pip:

```bash
pip install psutil
```

## How to Use

1. Clone this repository or download the script.
2. Run the script using Python:

   ```bash
   python3 benchmark.py
   ```

3. View the benchmark results and system information in the terminal.

## Output

The script provides the following:

- **CPU Benchmark**: Time taken to execute parallel tasks across all cores.
- **Memory Benchmark**: Time taken to allocate memory blocks up to 1 GB.
- **Disk Benchmark**: Time taken to write and read a 10 MB temporary file.
- **System Information**: Details about the OS, processor, memory, and CPU cores.

## Example Output

```text
Gathering system information...
OS: Linux
OS Version: #22-Ubuntu SMP Wed Dec 20 12:34:56 UTC 2023
OS Release: 5.15.0-73-generic
Processor: Intel(R) Core(TM) i7-1165G7 @ 2.80GHz
CPU Cores: 8
Memory: 16.00 GB

Starting benchmarks...

Starting CPU benchmark...
CPU benchmark completed in 4.32 seconds.

Starting memory benchmark...
Memory benchmark completed in 3.45 seconds.

Starting disk benchmark...
Disk write completed in 0.12 seconds.
Disk read completed in 0.08 seconds.

Benchmark Results:
CPU Time: 4.32 seconds
Memory Time: 3.45 seconds
Disk Write Time: 0.12 seconds
Disk Read Time: 0.08 seconds
```

## Safety

This script is safe to use. It:

- Does not modify your system or files.
- Cleans up temporary files after disk benchmarking.
- Handles memory allocation errors gracefully.

However, ensure you:

- Save your work before running the script, as high resource usage might slow other tasks.
- Run the script on AC power to prevent rapid battery drain.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests with improvements or new features.

---

Happy benchmarking!
