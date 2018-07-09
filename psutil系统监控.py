#!/usr/bin/env python
#coding=utf-8


import psutil

# import re
# propertyList = dir(psutil)
# pList = []
# fList = []
# for x in propertyList:
# 	if(re.match(r'[a-zA-Z]{1,100}$',x)):
# 		pList.append(x)
# 	else:
# 		fList.append(x)
# print('pasutil属性：',pList)
# print('pasutil方法：',fList)

''' ['AIX', 'AccessDenied', 'BSD', 'Error', 'FREEBSD', 'LINUX', 'NETBSD', 
	 'NoSuchProcess', 'OPENBSD', 'OSX', 'POSIX', 'Popen', 'Process', 'SUNOS', 
	 'TimeoutExpired', 'WINDOWS', 'ZombieProcess', 'collections', 'contextlib', 
	 'datetime', 'errno', 'functools', 'long', 'os', 'pids', 'pwd', 'signal', 
	 'subprocess', 'sys', 'test', 'time', 'traceback', 'users']
	 '''


'''
	在Python中获取系统信息	psutil
	1.获取CPU信息
	'''

cpuCount = psutil.cpu_count()#cpu 逻辑数量
print('cpu 逻辑数量:',cpuCount)
cpulogical = psutil.cpu_count(logical=False)#CPU物理核心
print('CPU物理核心:',cpulogical) # 2说明是双核超线程, 4则是4核非超线程
	

'''
	2.统计CPU的用户／系统／空闲时间：
	'''
cpuTimes = psutil.cpu_times()
print('CPU的用户／系统／空闲时间:',cpuTimes)

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# for x in range(10):
# 	CPUUser =  psutil.cpu_percent(interval = 1,percpu = True)
# 	print('CPU使用率每秒刷新一次:',CPUUser)
	
'''
	3.获取内存信息
	'''
cpuMemory = psutil.virtual_memory()
cpuSwap = psutil.swap_memory()
print('cpuMemory内存信息：',cpuMemory)
print('cpu交换区信息：',cpuSwap)
'''
cpuMemory内存信息:
svmem(total=8589934592, #总内存大小是8589934592 = 8 GB
 	available=2579615744, 
 	percent=70.0, #使用了70%
    used=7015297024, #已用7015297024 = 7 GB
 	free=31858688, 
 	active=2672586752, 
 	inactive=2547757056, 
 	wired=1794953216)

cpu交换区信息:
sswap(total=1073741824, #而交换区大小是1073741824 = 1 GB。
	used=0, 
	free=1073741824, 
	percent=0.0, 
	sin=11635412992, 
	sout=87379968)
'''

'''
	4.获取磁盘信息
	可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
'''
 
cpuPart = psutil.disk_partitions()#磁盘分区信息
cpuUseage = psutil.disk_usage('/')#磁盘使用情况
cpuCounters =  psutil.disk_io_counters() #磁盘IO
print('cpu磁盘分区信息:',cpuPart)
print('cpu磁盘使用情况:',cpuUseage)
print('cpu磁盘IO:',cpuCounters)

'''

# cpu磁盘分区信息:
[sdiskpart(device='/dev/disk0s2', 
	mountpoint='/', 
	fstype='hfs', #文件格式是HFS
	opts='rw,local, #表示可读写
	rootfs,dovolfs,
	journaled,#表示支持日志
	multilabel')]

# cpu磁盘使用情况:
sdiskusage(total=999345127424, #总容量是999345127424 = 930 GB
	used=256843866112, 
	free=742239117312, 
	percent=25.7)#使用了25.7%

# cpu磁盘IO:
sdiskio(read_count=365015, 
	write_count=344144, 
	read_bytes=11479504384, 
	write_bytes=6250120704, 
	read_time=4374786, 
	write_time=2834698)
'''

'''
5.获取网络信息
psutil可以获取网络接口和网络连接信息：
'''

netCounters = psutil.net_io_counters() #获取网络读写字节/包的个数
print('获取网络读写字节/包的个数:',netCounters)
netAddress = psutil.net_if_addrs()#获取网络接口信息
# print('获取网络接口信息',netAddress)
netstatus = psutil.net_if_stats()#获取网络接口状态
# print('获取网络接口状态：',netstatus)


'''
# 获取网络读写字节/包的个数:
snetio(bytes_sent=366861312, 
	bytes_recv=540371968, 
	packets_sent=973691, 
	packets_recv=976662, 
	errin=0, 
	errout=0, 
	dropin=0, 
	ropout=0)

# 获取网络接口信息 很长省略...
{
  'lo0': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0'), ...],
  'en1': [snic(family=<AddressFamily.AF_INET: 2>, address='10.0.1.80', netmask='255.255.255.0'), ...],
  'en0': [...],
  'en2': [...],
  'bridge0': [...]
}

# 获取网络接口状态：很长省略...
{
  'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=16384),
  'en0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),
  'en1': snicstats(...),
  'en2': snicstats(...),
  'bridge0': snicstats(...)
}
'''


'''
	6.要获取当前网络连接信息，使用net_connections()：
	#warn 需要root权限
	sudo python ***.py
	'''
netConnection = psutil.net_connections()
# print('获取当前网络连接信息:',netConnection)#warn 需要root权限
# 你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：

'''
	7.获取进程信息
	通过psutil可以获取到所有进程的详细信息：
	'''  
netPids = psutil.pids()
# print('所有进程的详细信息：',netPids)
 
netProcess = psutil.Process(netPids[1]) # 获取指定进程 iD=3776其实就是当前 python 交互环境
# print('获取指定进程:',netProcess)

netName = netProcess.name()#进程名称
print('进程名称:',netName)

netpath = netProcess.exe()#进程exe路径
print('进程exe路径',netpath)
netcwd = netProcess.cwd() # 进程工作目录
print('进程工作目录:',netcwd)
netline = netProcess.cmdline()# 进程启动的命令行
print(' 进程启动的命令行:',netline)
netFa = netProcess.ppid()# 父进程ID
print('父进程ID:',netFa)
netparent = netProcess.parent()#父进程
print('父进程:',netparent) 
netparentChildren = netProcess.children()#子进程列表
print('子进程列表:',netparentChildren)
netstatus = netProcess.status()#进程状态
print('进程状态:',netstatus)
netName = netProcess.username() # 进程用户名
print('进程用户名:',netName)
netcreateTime = netProcess.create_time() # 进程创建时间
print('进程创建时间：',netcreateTime)   
netterminal = netProcess.terminal() # 进程终端
print('进程终端：',netterminal)
nettimes = netProcess.cpu_times()# 进程使用的CPU时间
print('进程使用的CPU时间:',nettimes)
netMemoryInfo = netProcess.memory_info()# 进程使用的内存
print('进程使用的内存:',netMemoryInfo)
netOpenFiles = netProcess.open_files()# 进程打开的文件
print('进程打开的文件:',netOpenFiles)
netConnc = netProcess.connections()# 进程相关网络连接
print('进程相关网络连接:',netConnc)

netthreads = netProcess.num_threads() # 进程的线程数量
print('进程的线程数量:',netthreads)

'''


通过psutil可以获取到所有进程的详细信息：
[3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]

获取指定进程 
pid=3221, name='sudo', started='18:07:19'

进程名称: sudo

进程exe路径 /usr/bin/sudo
进程工作目录: /Users/djnet/Desktop
进程启动的命令行: ['sudo', 'python3.7', 'pic.py']
父进程ID: 1158
父进程: psutil.Process(pid=1158, name='zsh', started='10:15:29')
子进程列表: [psutil.Process(pid=3333, name='Python', started='18:16:54')]
进程状态: running
进程用户名: root
进程创建时间： 1530785984.024908
进程终端： /dev/ttys000
进程使用的CPU时间: pcputimes(user=0.014507413, system=0.009406903, children_user=0.0, children_system=0.0)
进程使用的内存: pmem(rss=5378048, vms=4399153152, pfaults=1612, pageins=0)
进程打开的文件: [popenfile(path='/private/etc/security/audit_event', fd=5), popenfile(path='/private/etc/security/audit_class', fd=6)]
进程相关网络连接: []
进程的线程数量: 1


'''








