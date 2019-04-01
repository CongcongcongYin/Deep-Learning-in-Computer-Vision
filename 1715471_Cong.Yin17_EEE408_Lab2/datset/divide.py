import os
import os.path
import fnmatch
import shutil

def open_save(file,savepath):
    # read .seq file, and save the images into the savepath

    f = open(file,'rb')
    string = str(f.read())
    splitstring = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"
    # split .seq file into segment with the image prefix
    strlist=string.split(splitstring)
    f.close()
    count = 0
    filecount=0
    # delete the image folder path if it exists
    if os.path.exists(savepath):
        for root, di, files in os.walk(savepath):
            filecount+=len(files)
    # create the image folder path
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    # deal with file segment, every segment is an image except the first one
    for img in strlist:
	zero=''
	count_len=len(str(count+filecount))
	count_zero=6-count_len
	while count_zero > 0:
	    zero=zero+'0'
	    count_zero -= 1
	filename = zero+str(count+filecount)+'.jpg'
	filenamewithpath=os.path.join(savepath, filename)
        # abandon the first one, which is filled with .seq header
        if count > 0:
            i=open(filenamewithpath,'wb+')
            i.write(splitstring)
            i.write(img)
            i.close()
        count += 1

if __name__=="__main__":
    rootdir = "data"
    # walk in the rootdir, take down the .seq filename and filepath
    for parent, dirnames, filenames in os.walk(rootdir):
	dirnames.sort()
	filenames.sort()
	for filename in filenames:
            # check .seq file with suffix
            if fnmatch.fnmatch(filename,'*.seq'):
                # take down the filename with path of .seq file
                thefilename = os.path.join(parent, filename)
                # create the image folder by combining .seq file path with .seq filename
                thesavepath = '/home/deeplearning_2/congyin.2017/lab2/py-faster-rcnn/data/calimage'
                print "Filename=" + thefilename
                print "Savepath=" + thesavepath
                open_save(thefilename,thesavepath)
