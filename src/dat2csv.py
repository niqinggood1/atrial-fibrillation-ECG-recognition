from os import listdir, mkdir, system
from os.path import isfile, isdir, join, exists

dir = '../afpdb/'#'mitdb/'
#Create folder
dir_out = '../afpdbCSV/'
if not exists(dir_out):
	mkdir(dir_out)

records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.dat') != -1)]

#  isfile(path)   如果 path 是一个文件或一个文件的符号链接，则返回 True
#  os.path.exists(path) 方法，如果 path 是一个文件、目录或文件的符号链接，则返回 True
#  listdir 是遍历目录下的文件和文件夹
#  isdir

for i in records:
    print('###:',i )
import wfdb
import  pandas as pd
for r in records:
    print( r )
	# --> Create Csv files
    ##rdsamp :  rdrecord()和rdsamp,前者读取一个完整的信号记录，后者读取一个记录中指定的通道(channel)或者指定的部分(section).
    ##rdsamp -r record [options ... ]
    ##随意读指定记录文件，并以十进制标准输出。无参，则rdsamp默认开始为0时刻，输出所有样品。默认情况下，每一行输出包含样品数量和每个导联的样品。起始为0导联起点

    # command = 'rdsamp -r ' + dir + r[:-4] + ' -c -H -f 0 -t 10 -v > ' + dir_out + r[:-4] + '.csv'
    # print( 'command:',command  )
    # system(command)
    record = wfdb.rdrecord('../afpdb/'+r[:-4],  # 文件所在路径
                               sampfrom=0,  # 读取这个记录的起点，从第0个点开始读
                               sampto=1280,  # 读取记录的终点，到1000个点结束
                               physical=False,  # 若为True则读取原始信号p_signal，如果为False则读取数字信号d_signal，默认为False
                              )  #  channels=[0, 1] # 读取那个通道，也可以用channel_names指定某个通道;如channel_names=['MLII']
    signal = record.d_signal[0:1280]
    df = pd.DataFrame( signal )
    df.to_csv( dir_out + r[:-4]+'.csv' )
    #  --> Create annotation files
	# command_annotations = 'rdann -r ' + dir + r[:-4] +' -f 0 -a atr -v >' + dir_out + r[:-4] + 'annotations.txt'
	# print(command_annotations)
	# system(command_annotations)
# system(command_annotations)
records.sort()
print(records)
print(len(records))
