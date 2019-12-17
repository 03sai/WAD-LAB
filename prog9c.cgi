#!/usr/bin/perl
use CGI;
$cgi=new CGI;
print "Content-typr: text/html\n\n";
print "<html>\n<body>\n";
print "<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">\n";
print $cgi->h1('<center>Server Page visited Informations</center>');
print $cgi->hr;
$count_file="/home/rahul/Downloads/count.txt";
if(open(FILE,"<".$count_file))
{
$no_accesses=<FILE>;
close(FILE);
if(open (FILE,">".$count_file)){
$no_accesses++;
print FILE $no_accesses;
close(FILE);
}
else
{
print "Cannot write the file. No Visitors information in the server";
}
}
else
{
print "cannot read the counter database for visitors";
}
print "Welcome user";
print "<BR><BR>This page has been accessed <font color=red size=10>
$no_accesses </font> times from the creation";
print "\n</div>\n";
print "</body>\n</html>\n";
