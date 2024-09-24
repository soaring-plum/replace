import binascii

def find_all_occurrences(text, pattern):
    occurrences = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        occurrences.append(index)
        start = index + 1
    return occurrences
def creat(hex_data,filename):
    # 将十六进制字符串转换为二进制数据
    binary_data = binascii.unhexlify(hex_data)
    # 将二进制数据写入文件
    with open(filename, 'wb') as file:
        file.write(binary_data)
    print("文件已成功创建")
def r(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    hex_data = binascii.hexlify(data)
    d=hex_data.decode('utf-8')
    return d
# 打开文件，以二进制模式读取


# 将文件内容转换为十六进制
f1='weapon.bank'#-----------------------------------
d=r(f1)
snd='534e4420'
fsb='465342350100'
l1=find_all_occurrences(d, snd)
l2=find_all_occurrences(d, fsb)
sndindex=[]
fsbindex=[]
for i in l1:
    if i%2==0:
        sndindex.append(i)
for i in l2:
    if i%2==0:
        fsbindex.append(i)
if len(sndindex) != len(fsbindex):
    print("有错误！！！")
l=len(d)
print(sndindex,fsbindex)
fsblist=[]
for i in range(len(sndindex)):
    if i==len(sndindex)-1:
        t=(l-fsbindex[i])/2
        fsblist.append(t)
        print('fsb{0}文件大小：{1}'.format(i+1,t))
    else:
        t = (sndindex[i+1]-fsbindex[i])/2
        fsblist.append(t)
        print('fsb{0}文件大小：{1}'.format(i+1,t))
f2='untitled.fsb'#自己制作的fsb文件
newfsb=r(f2)
n=len(newfsb)#新fsb文件的大小
print('新fsb文件大小：',n/2)
x=2#-----------------------选择要替换第2个fsb-----------------
if n/2>fsblist[x-1]:
    print('超过原本大小！')
else:
    newbank=d.replace(d[fsbindex[x-1]:fsbindex[x-1]+n],newfsb)
    # newbank = d.replace(d[fsbindex[x - 1]:], newfsb)
    f2='new.bank'#新文件名字
    creat(newbank,f2)




# 十六进制字符串
