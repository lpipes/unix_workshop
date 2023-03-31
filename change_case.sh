#!/usr/bin/perl
use strict;
use warnings;

opendir(DIR,"Exercise_1c") || die("cannot open dir!");
while(my $file = readdir(DIR)){
	if ( $file !~ /.fastq$/ ){ next; }
	my $lowercase_file = lc $file;
	my @spl = split(/\.fastq/,$lowercase_file);
	@spl = split("16s_",$spl[0]);
	$lowercase_file = $spl[1];
	print "$file\t$lowercase_file\n";
}
closedir(DIR);
