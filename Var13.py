import re
import time

counter = 0
System = dict()

_time = open('RegEx_time.txt', 'a')
_data = open(r'C:\Users\1\PycharmProjects\my_first_project\test.txt', 'r')
_analyze = open('RegEx_analyze.txt', 'w')
start_time = time.perf_counter()
for line in _data:
    match = re.search(r'^(\\\\)[A-Z][A-Z0-9]{,14}\\[A-Za-z][A-Za-z0-9]{,30}[A-Za-z0-9$]?\\'
                      r'([A-Za-z][A-Za-z0-9]{,31}\\)*([A-Za-z][A-Za-z0-9]{,31})?$', line)
    if match and len(line) <= 101:
        counter += 1
        _analyze.write('+ ' + line)
        server = line[2:line.find('\\', 2)]
        if server in System:
            System[server] += 1
        else:
            System[server] = 1
    else:
        _analyze.write('- ' + line)

_time.write('\nResult time: ' + str(time.perf_counter() - start_time))
_time.close()
_result = open('RegEx_servers.txt', 'w')
for i in System:
    _result.write(i + '\t' + str(System[i]) + '\n')
_analyze.close()
_data.close()
_result.close()