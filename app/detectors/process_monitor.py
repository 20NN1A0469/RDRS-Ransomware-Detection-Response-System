import psutil


def get_processes():

    processes = []

    for process in psutil.process_iter(
        [
            "pid",
            "name",
            "cpu_percent",
            "memory_percent",
            "exe",
            "ppid"
        ]
    ):

        try:

            info = process.info

            processes.append({
                "pid": info.get("pid"),
                "name": info.get("name"),
                "cpu_percent": info.get("cpu_percent"),
                "memory_percent": info.get("memory_percent"),
                "executable": info.get("exe"),
                "parent_pid": info.get("ppid")
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):

            continue

    return processes


if __name__ == "__main__":

    processes = get_processes()

    for process in processes[:10]:
        print(process)