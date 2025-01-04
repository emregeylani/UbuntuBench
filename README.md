# UbuntuBench

UbuntuBench is a Python-based benchmarking tool designed to evaluate CPU, memory, and disk performance on Linux systems. It also provides basic system information, including hardware specifications such as RAM and disk details.

## Features
- Benchmarks CPU performance using multiprocessing.
- Tests memory performance by allocating memory blocks.
- Evaluates disk read/write speed.
- Gathers system information, including OS details, processor specifications, RAM, and disk usage.

## Prerequisites
- Python 3.6+
- `psutil` library

### Install Dependencies
```bash
pip install psutil
```

### Additional Tools (Linux)
Ensure the following command is available:
- `lsblk`

On Ubuntu, install it with:
```bash
sudo apt update
sudo apt install util-linux
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/UbuntuBench.git
   cd UbuntuBench
   ```
2. Run the script:
   ```bash
   python3 benchmark.py
   ```

> **Note:** The script no longer requires `sudo` for basic functionality. However, detailed hardware information (e.g., RAM speed and manufacturer) is no longer included to avoid requiring elevated privileges.

## Sample Output
```plaintext
Gathering system information...
OS: Linux
OS Version: #14-Ubuntu SMP PREEMPT_DYNAMIC Sat Nov 30 23:51:51 UTC 2024
OS Release: 6.11.0-13-generic
Processor: x86_64
CPU Cores: 4
Memory: 8.20 GB
Disk Total: 512.00 GB
Disk Used: 120.00 GB
Disk Free: 392.00 GB

Disk Details:
NAME ROTA MODEL             SIZE
sda  0    Samsung SSD 970   512G

RAM Details:
Total Memory: 8.20 GB
Available Memory: 6.50 GB

Starting benchmarks...

Starting CPU benchmark...
CPU benchmark completed in 0.42 seconds.

Starting memory benchmark...
Memory benchmark completed in 1.32 seconds.

Starting disk benchmark...
Disk write completed in 0.10 seconds.
Disk read completed in 0.05 seconds.

Benchmark Results:
CPU: A+ (0.42 seconds)
Memory: A (1.32 seconds)
Disk Write: A (0.10 seconds)
Disk Read: A+ (0.05 seconds)
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Disclaimer
This tool is designed for benchmarking purposes. It does not require `sudo` privileges to run, making it safe for use without elevated permissions.


