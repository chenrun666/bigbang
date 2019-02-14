"""
StringIO经常被用来作字符串的缓存，因为StringIO的一些接口和文件操作是一致的，也就是说同样的代码，可以同时当成文件操作或者StringIO操作。
"""
import io

output = io.StringIO()
output.write("First line.\n")

contents = output.getvalue()

print(contents)
output.close()