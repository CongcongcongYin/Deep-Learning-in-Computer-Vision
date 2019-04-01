import os
import random

def folder_struct(level, path):
    global allFileNum

    dirList = []
    fileList = []
    files = os.listdir(path)
    dirList.append(str(level))

    for f in files:
        if(os.path.isdir(path + '/' + f)):
            if f[0] != '.':
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            fileList.append(f)


    i_dl = 0
    for dl in dirList:
        if i_dl == 0:
            i_dl = i_dl + 1
        else:
            #print '-' * (int(dirList[0])), dl
            folder_struct((int(dirList[0]) + 1), path+'/'+dl)

    print fileList
    # print dirList

    file_info = 'Caltech'
    print file_info
    generate_txt(file_info)


def generate_txt(xml_folder):
    trainval_percent = 0.66
    train_percent = 0.5
    folder_root = '/home/deeplearning_3/CYPLab2/
    xmlfilepath = folder_root +'cal_txt/'+ xml_folder
    txtsavepath = folder_root + 'ImageSets/Main/'

    try:
        total_xml = os.listdir(xmlfilepath)
        #print total_xml

        num = len(total_xml)

        #print num
        list = range(num)
        tv = int(num * trainval_percent)
        tr = int(tv * train_percent)
        trainval = random.sample(list, tv)
        train = random.sample(trainval, tr)

        ftrainval = open(folder_root + 'ImageSets/Main/trainval.txt', 'aw')
        ftest     = open(folder_root + 'ImageSets/Main/test.txt'    , 'aw')
        ftrain    = open(folder_root + 'ImageSets/Main/train.txt'   , 'aw')
        fval      = open(folder_root + 'ImageSets/Main/val.txt'     , 'aw')

        folder_name = xmlfilepath[-10:] + '/'
 	#print trainval
	#print train

	total_xml.sort()
        print total_xml

	print folder_name
        for i in list:
            name = total_xml[i][:-4] + '\n'
            print name
	    if i in trainval:
                ftrainval.write(name)
                if i in train:
                    ftrain.write(name)
                else:
                    fval.write(name)
            else:
                ftest.write(name)

        ftrainval.close()
        ftrain.close()
        fval.close()
        ftest.close()
    except Exception:
        pass

folder_struct(1, "/home/deeplearning_2/congyin.2017/lab2/data_old")
