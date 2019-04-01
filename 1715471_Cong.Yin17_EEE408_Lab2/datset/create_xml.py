#from xml.etree.ElementTree import Element, SubElement, tostring
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import os

def mkdir(path):
    import os

    path = path.strip()
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print path + 'ok'
        return True
    else:
        print path + 'failed!'
        return False

def generate_xml(file_info, obj):
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = file_info[0]

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = file_info[1]

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = '640'

    node_height = SubElement(node_size, 'height')
    node_height.text = '480'

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    for obj_i in obj:
        print obj_i
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        #node_name.text = 'mouse'
        node_name.text = 'person'

        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        #node_xmin.text = '99'
        node_xmin.text = obj_i['xmin']

        node_ymin = SubElement(node_bndbox, 'ymin')
        #node_ymin.text = '358'
        node_ymin.text = obj_i['ymin']

        node_xmax = SubElement(node_bndbox, 'xmax')
        #node_xmax.text = '135'
        node_xmax.text = obj_i['xmax']

        node_ymax = SubElement(node_bndbox, 'ymax')
        #node_ymax.text = '375'
        node_ymax.text = obj_i['ymax']

    xml = tostring(node_root, pretty_print=True)
    dom = parseString(xml)
    file_root = '/home/deeplearning_3/CYPLab2/cal_datatest'

    file_name = file_root + file_info[0];
    mkdir (file_name)
    fw = open(file_name+"/"+file_info[1].split('.')[0]+".xml", 'a+')

    fw.write(xml)
    print "xml _ ok"
    fw.close()

    #for debug
    #print xml

def printPath(level, path):
    global allFileNum

    dirList = []

    fileList = []

    files = os.listdir(path)

    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):

            if(f[0] == '.'):
                pass
            else:

                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):

            fileList.append(f)

    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:

            print '-' * (int(dirList[0])), dl

            printPath((int(dirList[0]) + 1), path + '/' + dl)
    print fileList
    for fl in fileList:

        print fl[12:17],fl[17:21]
        file_info = []
	file_info.append('Caltech')

        print file_info
        print path
        file_name = path+"/"+fl
        fw = open(file_name, 'r');
        line_content = fw.readlines()
        fw.close()


        tmp = []
        obj = []
        con_len = len(line_content)

        try:
            string = line_content[0].split(" ")
            tmp = string[0]
        except Exception:
            continue
        file_info.append(tmp + '.jpg')
	xmin_=int(float(string[1]))
	if xmin_<0:
	    xmin_=0
        xmin = str(xmin_)
	ymin_=int(float(string[2]))

    if ymin_<0:
	    ymin_=0
	ymin = str(ymin_)
	xmax = str(int(float(string[1]) + float(string[3])))
        ymax = str(int(float(string[2]) + float(string[4])))
        dict1 = {}
        dict1["xmin"] = xmin
        dict1["ymin"] = ymin
        dict1["xmax"] = xmax
        dict1["ymax"] = ymax
        obj.append(dict1)

        for con_i in xrange(1, con_len):
            string = line_content[con_i].split(" ")
            tmp1 = string[0]
            if tmp == tmp1:
		xmin_=int(float(string[1]))
    	    if xmin_<0:
                 xmin_=0
        	xmin = str(xmin_)
        	ymin_=int(float(string[2]))
        	if ymin_<0:
                    ymin_=0
             	ymin = str(ymin_)
                xmax = str(int(float(string[1]) + float(string[3])))
                ymax = str(int(float(string[2]) + float(string[4])))

		dict1 = {}
                dict1["xmin"] = xmin
                dict1["ymin"] = ymin
                dict1["xmax"] = xmax
                dict1["ymax"] = ymax
                obj.append(dict1)
            elif int(tmp1) > 0:
                generate_xml(file_info, obj)
                obj = []
                tmp = tmp1
                file_info[1] = tmp1 + ".jpg"
                xmin_=int(float(string[1]))
	        if xmin_<0:
        	    xmin_=0
        	xmin = str(xmin_)
        	ymin_=int(float(string[2]))
        	if ymin_<0:
        	    ymin_=0
        	ymin = str(ymin_)
                xmax = str(int(float(string[1]) + float(string[3])))
                ymax = str(int(float(string[2]) + float(string[4])))
                dict1 = {}
                dict1["xmin"] = xmin
                dict1["ymin"] = ymin
                dict1["xmax"] = xmax
                dict1["ymax"] = ymax
                obj.append(dict1)
        continue

def read_annotations_generate_fileinfo_obj(file_path):
    pass

if __name__=="__main__":

    #
    # file_info = ['set00/V000', '1.jpg']
    #
    # obj = []
    # obj1 = {"xmin":"1", "ymin":"1", "xmax":"5", "ymax":"5"}
    # obj2 = {"xmin":"2", "ymin":"2", "xmax":"6", "ymax":"6"}
    # obj.append(obj1)
    # obj.append(obj2)
    #
    # generate_xml(file_info, obj)
    #

    printPath(1, "/home/deeplearning_2/congyin.2017/lab2/cal_txt")
