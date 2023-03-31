#!/usr/bin/perl
use strict;
use warnings;

opendir(DIR,"Exercise_2") || die("cannot open dir!");
while(my $file = readdir(DIR)){
	if ( $file !~ /.fastq.gz$/ ){ next; }
	open(FILE,"Exercise_2/" . $file) || die ("cannot open file!");
	open(OUTFILE,">","Exercise_3/" . $file) || die("cannot open file!");
	my $counter=0;
	while(<FILE>){
		if ( $counter == 4 ){ last; }
		my $line = $_;
		chomp($line);
		print OUTFILE "$line\n";
		$counter++;
	}
	close(OUTFILE);
}
closedir(DIR);
