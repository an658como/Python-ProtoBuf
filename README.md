# Application of ProtoBuf in Python
In this simple project, we are showcasing how to implement ProtBuf in a simple python code. Then, this project can be used for further expanding the implementation of ProtoBuf in larger projects. The instructions on the [www.freecodecamp.org](https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/) website is very useful to have better idea about ProtoBuf.

## Installing the ProtoBuf complier (`protoc`)
For installing `protoc`, please refer to the google developer team's [instructions](https://github.com/protocolbuffers/protobuf#protocol-compiler-installation). The easiet way for Windows installation is downloading the binary files and adding them to the `path` variable. 

## Creating the ProtoBuf python class
### Windows
To create the ProtBuf python class for your application, put your `.proto` file in the `SRC_DIR` and run the following command to create the required python class in the `DST_DIR`:

    scripts\convert.bat <name-of-your-.porto-file without the extension>

There is a file already provided in the `SRC_DIR` called `todolist.proto`. As an exmple you could run the following command to create the `todolist_pb2.py` in `DST_DIR`:

    scripts\convert.bat todolist

### Linux/Mac
This section will be added in next revision. 

## Running the python codes
There three python codes for different testing. `todolist.py` demostrate how to create a data object using `ProtoBuf` and write/read data using this object. `write.py` has the same application as `todolist.py`, and additioanlly, it writes the serialized data string into file. `read.py` is a python code that creates a `ProtoBuf` object and reads in the serialized file that was created by `write.py`. The serialized data file can transferred via networks or be used for data storage. 

For running the codes, you can open a cmd window, type in the following command, and press enter:

    python <name-of-the-python-code>