import os
from colorama import Fore
import sys

def main():
 try:
  if len(sys.argv) > 2:
   extension = sys.argv[1].split('.')
   match extension[1]:
    case 'cpp':
     compilerCPP(sys.argv[1], sys.argv[2])
    case 'c':
     compilerC(sys.argv[1], sys.argv[2])
  else:
   run()
 except IndexError:
  print(Fore.RED + 'Error! python main.py [filename.cpp] [namefile]\nExample: python main.py mycppcode.cpp main')

def run():
 for cppfilesearch in os.listdir():
  try:
   if os.path.isfile(cppfilesearch):
    extension = cppfilesearch.split('.')
    match extension[1]:
     case 'cpp':
      print('You can use a faster way to compile the code. Example python main.py mycppcode.cpp main')
      filename = str(input(f'The name of your {Fore.GREEN}{cppfilesearch}{Fore.WHITE} file is correct. Yes/No: '))
      match filename.upper():
       case 'YES':
        slnfilename = str(input(f'The name of the finished file will be {Fore.GREEN}{extension[0]}{Fore.WHITE}. Yes/No: '))
        match slnfilename.upper():
         case 'YES':
          compilerCPP(cppfilesearch, extension[0])     
          break 
         case 'NO':
          slnfilename = str(input(f'Enter another name for the finished file: '))
          compilerCPP(cppfilesearch, slnfilename)
          break 
       case 'NO':
        filename = str(input('Enter the name of the C/C++ file with the extension:  '))
        slnfilename = str(input(f'Enter the name of the finished file: ')) 
        compilerCPP(filename, slnfilename)
        break
      
     case 'c':
      print('You can use a faster way to compile the code. Example python main.py mycppcode.c main')
      filename = str(input(f'The name of your {Fore.GREEN}{cppfilesearch}{Fore.WHITE} file is correct. Yes/No: '))
      match filename.upper():
       case 'YES':
        slnfilename = str(input(f'The name of the finished file will be {Fore.GREEN}{extension[0]}{Fore.WHITE}. Yes/No: '))
        match slnfilename.upper():
         case 'YES':
          compilerC(cppfilesearch, extension[0])     
          break 
         case 'NO':
          slnfilename = str(input(f'Enter another name for the finished file: '))
          compilerC(cppfilesearch, slnfilename)
          break 
       case 'NO':
        filename = str(input('Enter the name of the C/C++ file with the extension: '))
        slnfilename = str(input(f'Enter the name of the finished file: ')) 
        compilerC(filename, slnfilename)
        break
     case _:
      pass
  except IndexError:
   return
  except KeyboardInterrupt:
   os._exit(0)

def compilerCPP(filename, slnfilename):
 clang = os.system(f'clang++ {filename} -o {slnfilename}')
 if clang == 0:
  if os.path.isdir(os.path.expanduser('~/CPPFolder')):
   os.system(f'mv {slnfilename} ~/CPPFolder')
   os.system(f'chmod +x $HOME/CPPFolder/{slnfilename}')
   print(f'All done\nnow type cd $HOME/CPPFolder followed by ./{slnfilename}')
  else:
   os.system('mkdir $HOME/CPPFolder')
   compilerCPP(filename, slnfilename)
 else:
  print('There was an error')

def compilerC(filename, slnfilename):
 clang = os.system(f'clang {filename} -o {slnfilename}')
 if clang == 0:
  if os.path.isdir(os.path.expanduser('~/CFolder')):
   os.system(f'mv {slnfilename} ~/CFolder')
   os.system(f'chmod +x $HOME/CFolder/{slnfilename}')
   print(f'All done\nnow type cd $HOME/CFolder followed by ./{slnfilename}')
  else:
   os.system('mkdir $HOME/CFolder')
   compilerC(filename, slnfilename)
 else:
  print('There was an error')
	
if __name__ == '__main__':
 main()
