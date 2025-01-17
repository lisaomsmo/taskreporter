import psutil
import datetime

class TaskReporter:
    def __init__(self):
        self.processes = []

    def gather_process_info(self):
        self.processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
            try:
                process_info = proc.info
                process_info['cpu_percent'] = proc.cpu_percent(interval=1)
                process_info['memory_percent'] = proc.memory_percent()
                self.processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def generate_report(self):
        report = f"System Activity Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += "=" * 60 + "\n"
        report += f"{'PID':<10}{'Name':<25}{'User':<15}{'CPU%':<10}{'Memory%':<10}\n"

        for proc in self.processes:
            report += f"{proc['pid']:<10}{proc['name']:<25}{proc['username']:<15}{proc['cpu_percent']:<10.2f}{proc['memory_percent']:<10.2f}\n"

        report += "=" * 60 + "\n"
        return report

    def save_report(self, filename="system_report.txt"):
        report = self.generate_report()
        with open(filename, 'w') as file:
            file.write(report)
        print(f"Report saved to {filename}")

if __name__ == "__main__":
    task_reporter = TaskReporter()
    task_reporter.gather_process_info()
    task_reporter.save_report()