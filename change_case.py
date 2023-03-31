#!/Users/lpipes/anaconda2/bin/python
import glob
path = "Exercise_1c"
dir_list = glob.glob(path + '/*fastq')
file_out = open("Exercise_1e.txte","w")
for x in dir_list:
	spl = x.split("/")
	file_out.write(spl[1] + "\t")
	spl = spl[1].split(".fastq")
	spl = spl[0].split("16S_")
	lowercase_file = spl[1].lower()
	file_out.write(lowercase_file + "\n")
file_out.close()
