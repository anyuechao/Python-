


"""
    
    命令行运行文件
    python hello.py
    """

"""
    
    直接运行py文件
    1.文件中增加如下
    #!/usr/bin/env python
    2.命令行
    chmod a+x hello.py
    3.命令行
    ./文件名
    
    """

"""
    ASCII编码互转
    >>> ord('A')
    65
    >>> chr(65)
    'A'
    
    Unicode编码互转
    >>> print u'中文'
    中文
    >>> u'中'
    u'\u4e2d'
    
     u'中文'.encode('utf-8')
    """

"""
    len()函数可以返回字符串的长度
    >>> len(u'ABC')
    3
    >>> len('ABC')
    3
    >>> len(u'中文')
    2
    >>> len('\xe4\xb8\xad\xe6\x96\x87')
    6
    
    """

