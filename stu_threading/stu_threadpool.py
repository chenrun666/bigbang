"""
安装threadpool： pip install threadpool
pool = ThreadPool(poolsize)
requests = makeRequests(some_callable, list_of_args, callback)
[pool.putRequest(req) for req in requests]
pool.wait()
"""
import time

import threadpool


def call_back(list_of_args):
    print(list_of_args)
    time.sleep(2)


def hello(m, n, o):
    print("m = %s, n = %s, o = %s" % (m, n, o))


name_list = ["xiaozi", "aa", "bb", "cc"]

# 传入列表和字典
lst_vars_1 = ["1", "2", "3"]
lst_vars_2 = ["4", "5", "6"]
func_var = [(lst_vars_1, None), (lst_vars_2, None)]

# 传入字典
dict_vars_1 = {"m": "1", "n": "2", "o": "3"}
dict_vars_2 = {"m": "4", "n": "5", "o": "6"}
func_var2 = [(None, dict_vars_1), (None, dict_vars_2)]

if __name__ == '__main__':
    pool = threadpool.ThreadPool(2)
    requests = threadpool.makeRequests(hello, func_var2)
    [pool.putRequest(req) for req in requests]
    pool.wait()
