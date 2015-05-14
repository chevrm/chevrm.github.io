#!/bin/env perl

use strict;
use warnings;

my $theme = undef;
my $com = "git commit -m 'autofired'";
$com =~ s/autofired/$ARGV[0]/ if(@ARGV[0]);
my @cmd = (
	"pelican -s pelicanconf.py -o ./ content",
	"git add .",
 	$com,
	"git push -u origin master" 
);
$cmd[0] .= " -t $theme" if($theme);
foreach (@cmd){
	system("$_");
}
