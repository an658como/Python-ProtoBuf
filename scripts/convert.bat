@ECHO OFF
SET arg1=%1
ECHO The .protofile name is: %arg1%
ECHO Creating the python-readable ProtoBuf structure: 
protoc -I=SRC_DIR\ --python_out=DST_DIR\ SRC_DIR\%arg1%.proto
