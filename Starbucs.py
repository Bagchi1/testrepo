import shutil
import os
for i in range(5,25,5): #Range of CTs ranging from 5-20yrs 
    os.makedirs(r'C:\USER\Abhiroop\Python_Tests\STARBUCS\ ' + str(i) + ' years') #Creating folders for differnt CTs
    shutil.copy2(r'C:\USER\Abhiroop\Python_Tests\STARBUCS\TN40HT_W14STD_Reconfig-Array_CR_BU5_5yCT.inp', r'C:\USER\Abhiroop\Python_Tests\STARBUCS\ ' + str(i) + ' years\TN40HT_W14STD_Reconfig-Array_CR_BU5_' + str(i) + 'yCT.inp') #Creating a copy of base file with different CTs in the required folders
    for j in range(10,60,5): #Range of BUs ranging from 10-55 BU
      shutil.copy2(r'C:\USER\Abhiroop\Python_Tests\STARBUCS\ ' + str(i) + ' years\TN40HT_W14STD_Reconfig-Array_CR_BU5_' + str(i) + 'yCT.inp', r'C:\USER\Abhiroop\Python_Tests\STARBUCS\ ' + str(i) + ' years\TN40HT_W14STD_Reconfig-Array_CR_BU' + str(j) + '_' + str(i) + 'yCT.inp') #Inside a specific CT folder creating copies of the base file with varying BUs in the names of the inputs
      with open(r'C:\USER\Abhiroop\Python_Tests\STARBUCS\ ' + str(i) + ' years\TN40HT_W14STD_Reconfig-Array_CR_BU' + str(j) + '_' + str(i) + 'yCT.inp','r') as f: #Reading a file with specific CT and BU and determing number of lines
          get_all=f.readlines()
      with open(r'C:\USER\Abhiroop\Python_Tests\STARBUCS\ ' + str(i) + ' years\TN40HT_W14STD_Reconfig-Array_CR_BU' + str(j) + '_' + str(i) + 'yCT.inp','w') as f:
          for l,line in enumerate(get_all,1):             
              if l == 47:                              
                  f.writelines('  power=  40.00000 burn= ' + str('%.2f'%((j/120)*1000)) + ' nlib=6 down=      0.00 end\n') #editing the line specifying BU value (l represents line number of file where BU is specified)
              elif l == 48:
                  f.writelines('  power=  40.00000 burn= ' + str('%.2f'%((j/120)*1000)) + ' nlib=6 down=      0.00 end\n')
              elif l == 49:
                  f.writelines('  power=  40.00000 burn= ' + str('%.2f'%((j/120)*1000)) + ' nlib=6 down=   ' + str('%.2f'%(i*365.25)) + ' end\n')#editing the line specifying CT value (l represents line number of file where CT is specified)
              elif l == 37 and (18<=j<30):                                       #Editing Burnup dependent axial profiles
                  f.writelines('  axp=0.668 1.034 1.150 1.094 1.053 1.048 1.064 1.095 1.121\n')
              elif l == 38 and (18<=j<30):
                  f.writelines('      1.135 1.140 1.138 1.130 1.106 1.049 0.933 0.669 0.373 end\n')
              elif l == 37 and (30<=j<38): 
                  f.writelines('  axp=0.652 0.967 1.074 1.103 1.108 1.106 1.102 1.097 1.094\n')
              elif l == 38 and (30<=j<38):
                  f.writelines('      1.094 1.095 1.096 1.095 1.086 1.059 0.971 0.738 0.462 end\n')
              elif l == 37 and (j>=38): 
                  f.writelines('  axp=0.660 0.936 1.045 1.080 1.091 1.093 1.092 1.090 1.089\n')
              elif l == 38 and (j>=38):
                  f.writelines('      1.088 1.088 1.086 1.084 1.077 1.057 0.996 0.823 0.525 end\n')
              else:
                  f.writelines(line)                                             #Writing the rest of the lines
