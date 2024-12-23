# UbuntuBench

UbuntuBench is a Python-based benchmarking tool designed to evaluate CPU, memory, and disk performance on Linux systems. It also provides detailed system information, including hardware specifications such as RAM and disk details.

## Features
- Benchmarks CPU performance using multiprocessing.
- Tests memory performance by allocating memory blocks.
- Evaluates disk read/write speed.
- Gathers system information, including OS details, processor specifications, RAM, and disk type (HDD/SSD).

## Prerequisites
- Python 3.6+
- `psutil` library
- Root privileges for detailed hardware information (required for `dmidecode` command).

### Install Dependencies
```bash
pip install psutil
```

### Additional Tools (Linux)
Ensure the following commands are available:
- `lsblk`
- `dmidecode`

On Ubuntu, install these with:
```bash
sudo apt update
sudo apt install util-linux dmidecode
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/UbuntuBench.git
   cd UbuntuBench
   ```
2. Run the script:
   ```bash
   sudo python3 benchmark.py
   ```

> **Note:** Running as root (`sudo`) is required to retrieve detailed RAM and disk information using `dmidecode`.

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
Speed: 3200 MT/s
Manufacturer: Corsair
Part Number: CMK16GX4M2B3200C16

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
This tool is designed for benchmarking purposes. Running the script with `sudo` may pose security risks. Use at your own discretion.


