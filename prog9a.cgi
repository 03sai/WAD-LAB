#!/usr/bin/perl
use CGI;
$cgi=new CGI;
print "Content-type: text/html\n\n";
print "<html>\n<body>\n";
print "<div style=\"width:100%; font-size:40px; font-weight:bold; text-align:center;\">\n";
print "<table border=0 cellpadding=2>";
print "<tr><td>SERVER_NAME:</td><td>", $ENV{'SERVER_NAME'},"</td></tr>";
print "<tr><td>SERVER_PORT:</td><td>", $ENV{'SERVER_PORT'},"</td></tr>";
print "<tr><td>SERVER_PROTOCOL:</td><td>", $ENV{'SERVER_PROTOCOL'},"</td></tr>";
print "<tr><td>SERVER_SOFTWARE:</td><td>", $ENV{'SERVER_SOFTWARE'},"</td></tr>";
print "<tr><td>CONTENT_LENGTH:</td><td>", $ENV{'CONTENT_LENGTH'},"</td></tr>";
print "<tr><td>GATEWAY_INTERFACE:</td><td>", $ENV{'GATEWAY_INTERFACE'},"</td></tr>";
print "<tr><td>PATH_INFO:</td><td>", $ENV{'PATH_INFO'},"</td></tr>";
print "<tr><td>PATH_TRANSLATED:</td><td>", $ENV{'PATH_TRANSLATED'},"</td></tr>";
print "<tr><td>QUERY_STRING:</td><td>", $ENV{'QUERY_STRING'},"</td></tr>";
print "<tr><td>REMOTE_ADDR:</td><td>", $ENV{'REMOTE_ADDR'},"</td></tr>";
print "<tr><td>REMOTE_HOST:</td><td>", $ENV{'REMOTE_HOST'},"</td></tr>";
print "<tr><td>REMOTE_USER:</td><td>",$ENV{'REMOTE_USER'},"</td></tr>";
print "<tr><td>REQUEST_METHOD:</td><td>",$ENV{'REQUEST_METHOD'},"</td></tr>";
print "<tr><td>DOCUMENT_NAME:</td><td>",$ENV{'DOCUMENT_NAME'},"</td></tr>";
print "<tr><td>DOCUMENT_URI:</td><td>",$ENV{'DOCUMENT_URI'},"</td></tr>";
print "<tr><td>SCRIPT_NAME:</td><td>",$ENV{'SCRIPT_NAME'},"</td></tr>";
print "<tr><td>SCRIPT_FILENAME:</td><td>",$ENV{'SCRIPT_FILENAME'},"</td></tr>";
print "</table>";
print "\n</div>\n";
print "</body>\n</html>\n"

