# Compiler of C/C++ files on termux 
<br> This script helps to run C/C++ files on termux


 # usage:
  To have access to the shared storage you need to write  
  
  + termux-setup-storage
  
  <br>After that you will be able to open the shared storage  
  
  + cd storage/downloads
  
 <br>Don't forget to install the dependencies once you open the folder by typing
 + git clone git clone https://github.com/RuslanFF/C-CPP-file-compiler-on-termux.git
 + cd C-CPP-file-compiler-on-termux
 + pip install -r requirements 
 
 <br>You must also install the clang by typing
 + pkg install clang
 
 <br> Then drop the main.py file into the folder with the C/C++ file and write
 + python main.py

# TODO:
- [ ] Support for header files
