import base64
print "Pleas Enter Data For Encode";
data=raw_input();
encode=base64.b64encode(data);
print "encode value = "+encode;
print "Pleas Enter Date For Decode";
dataq=raw_input();
decode=base64.b64decode(dataq);
print "decode value = "+decode;
