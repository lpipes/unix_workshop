#!/Users/lpipes/anaconda2/bin/python
import glob
path = "Exercise_2"
dir_list = glob.glob(path + '/*fastq.gz/')
for file in dir_list:
	spl = file.split("/")
	file_out = open("Exercise_3/" + spl[1],"w")
	file_in = open(file,"r")
	file_out.write(file_in.readline())
	file_out.write(file_in.readline())
	file_out.write(file_in.readline())
	file_out.write(file_in.readline())
	file_out.close()
	file_in.close()
