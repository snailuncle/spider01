import telnetlib

try:
    telnetlib.Telnet('127.0.0.1', port='80', timeout=20)
except:
    print 'connect failed'
else:
    print 'success'
