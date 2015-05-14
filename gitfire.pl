#!/bin/env perl

use strict;
use warnings;

my $com = "git commit -m 'autofired'";
$com =~ s/autofired/$ARGV[0]/ if(@ARGV[0]);
my @cmd = (
	"pelican -s pelicanconf.py -o ./ content -t mct",
	"git add .",
 	$com,
	"git push -u origin master" 
);
foreach (@cmd){
	system("$_");
}
