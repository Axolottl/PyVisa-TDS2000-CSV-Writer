import sys, traceback
import time
import pyvisa as visa
from csv import writer

def main():
	try:
		instrumentReturnValue = 0
		instrumentMaxValue = 0
		_rm = visa.ResourceManager()
		inst = _rm.open_resource('USB::0x0699::0x03A6::C055226::INSTR')
		inst.read_termination = '\n'
		inst.write_termination = '\n'
		#inst.write("AUTOS EXEC")
		inst.write("MEASU:IMM:SOU CH1;:MEASU:IMM:TYP MAXI")
		while True:
			instrumentReturnValue = float(inst.query("MEASU:IMM:VAL?"))
			if(instrumentReturnValue > instrumentMaxValue):
				instrumentMaxValuesList = []
				instrumentMaxValue = instrumentReturnValue
				print(instrumentMaxValue)
				instrumentMaxValuesList.append(instrumentMaxValue)
	except KeyboardInterrupt:
		print("Saving value ",instrumentMaxValue)
		with open('c:/Users/HP/Desktop/test.csv', 'a+', newline='') as write_obj:
			csv_writer = writer(write_obj)
			csv_writer.writerow(instrumentMaxValuesList)
			sys.exit(0)
	except Exception:
		traceback.print_exc(file=sys.stdout)
		sys.exit(0)
if __name__ == '__main__':
	main()
