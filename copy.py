import threading
import sys
class MemoryEaterThread(threading.Thread):
 def run(self):
 while True:
 a = [0] * (1024 * 1024 * 1024)
number_of_threads = 100
if len(sys.argv) > 1:
 try:
 number_of_threads = int(sys.argv[1])
 except ValueError:
 pass
for i in range(number_of_threads):
 t = MemoryEaterThread()
 t.start()
