#!/perl/bin/perl.exe
use CGI;
$cgi=new CGI;
print $cgi->header;
print $cgi->start_html('Program 1a');
print $cgi->h1('Server Informations');
print $cgi->hr;
print "<table border=0 cellpadding=2>";
print "<tr><td>SERVER_NAME: </td><td>",
$ENV{'SERVER_NAME'}, "</td></tr>";
print "<tr><td>SERVER_PORT: </td><td>",
$ENV{'SERVER_PORT'}, "</td></tr>";
print "<tr><td>SERVER_SOFTWARE: </td><td>",
$ENV{'SERVER_SOFTWARE'}, "</td></tr>";
print "<tr><td>SERVER_PROTOCOL: </td><td>",
$ENV{'SERVER_PROTOCOL'}, "</td></tr>";
print "<tr><td>GATEWAY_INTERFACE:</td><td>",
$ENV{'GATEWAY_INTERFACE'}, "</td></tr>";
print "</table>";
print $cgi->end_html;