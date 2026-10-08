import subprocess
import sys
import time

BOTS = [
    "bot.py",
    "forwarder.py",
]

processes = {}


def start_process(name):
    print(f"🚀 Запуск: {name}", flush=True)

    return subprocess.Popen(
        [sys.executable, "-u", name]
    )


# Запускаем процессы
for name in BOTS:
    processes[name] = start_process(name)
    time.sleep(3)

print(f"✅ Все {len(BOTS)} процесса запущены", flush=True)


while True:
    for name, process in list(processes.items()):

        if process.poll() is None:
            continue

        code = process.returncode

        print(
            f"❌ {name} остановился. Код: {code}",
            flush=True
        )

        # Если процесс завершился нормально — не перезапускаем
        if code == 0:
            print(
                f"ℹ️ {name} завершился без ошибки.",
                flush=True
            )
            continue

        # Небольшая задержка перед перезапуском
        print(
            f"⏳ Ожидание 10 секунд перед перезапуском {name}...",
            flush=True
        )

        time.sleep(10)

        print(
            f"🔄 Перезапуск: {name}",
            flush=True
        )

        processes[name] = start_process(name)

    time.sleep(5)
```
