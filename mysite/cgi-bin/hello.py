#encoding=utf-8
#!/usr/bin/python
import cgi

# 获取 GET 参数
form = cgi.FieldStorage()
name = form['name'].value

print "HTTP/1.0 200 OK"
print "Content-Type:text/html"
print ""
print ""
print "Hello, 世界, %s " % name
print ""
