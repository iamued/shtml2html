#coding=utf-8
'''
Created on Oct 19, 2011

@author: richie mail:richiefans@gmail.com website:http://www.iamued.com
'''
import os,re,sys
#遍历目录
def listyoudir(level, path):  
    for i in os.listdir(path): 
        if os.path.isdir(path + '' + i): 
            listyoudir(level+1, path + '' + i+"/")  
        #print '  '*(level+1) + i  
        #只对部分文件进行处理
        if os.path.splitext(i)[1] == ".shtml":
            #print path+i
            changelink(path,i)
#核心处理函数
def changelink(file,filename):
    print "正在处理...:"+file+filename
    page = open (file+filename).read()
    links = re.compile(r'<!--#include virtual="(.*?)"-->',re.I).findall(page)
    for link in links:
        print "正在替换include："+link
        page=page.replace("<!--#include virtual=\""+link+"\"-->",open (file+link).read())
    #重新写入文件
    #print os.path.splitext(filename)[0]
    open(file+os.path.splitext(filename)[0]+".html",'w').write(page)
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            print "目录递归处理"
            listyoudir(0,sys.argv[1])
        else:
            print "文件处理"
            if os.path.splitext(sys.argv[1])[1] == ".shtml":
                changelink(os.path.dirname(sys.argv[1])+"/",os.path.basename(sys.argv[1]))
        print "全部处理完成....."
    else:
        print "Usage: python "+sys.argv[0]+" path"   
        print "支持目录 和 文件"
        #listyoudir(0, "/Users/richie/wp/studypython/src/buildhtml/")