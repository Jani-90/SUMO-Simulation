# importing the required modules
import helper.generate_xml as gen

def process_emission_data(locationD, dateD, dayD, input_file, output_csv, contextD):

	# parse xml file
	simData = gen.parseXML(locationD, dateD, dayD, input_file, contextD)

	# store emission data in a csv file
	gen.savetoCSV(simData, output_csv)

	#insert emission data to the database
	gen.DBinsert(locationD, dateD, dayD, simData, contextD)

def main():
	# process_emission_data('FIFTEENTH AVE', '11112024', 'Monday', 'output/all_petrol/emission_fifteenthAve_11112024_monday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_11112024_monday.csv', 'all_petrol')
	# process_emission_data('FIFTEENTH AVE', '12112024', 'Tuesday', 'output/all_petrol/emission_fifteenthAve_12112024_tuesday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_12112024_tuesday.csv', 'all_petrol')
	# process_emission_data('FIFTEENTH AVE', '13112024', 'Wednesday', 'output/all_petrol/emission_fifteenthAve_13112024_wednesday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_13112024_wednesday.csv', 'all_petrol')
	# process_emission_data('FIFTEENTH AVE', '14112024', 'Thursday', 'output/all_petrol/emission_fifteenthAve_14112024_thursday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_14112024_thursday.csv', 'all_petrol')
	# process_emission_data('FIFTEENTH AVE', '08112024', 'Friday', 'output/all_petrol/emission_fifteenthAve_08112024_friday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_08112024_friday.csv', 'all_petrol')
	# process_emission_data('FIFTEENTH AVE', '09112024', 'Saturday', 'output/all_petrol/emission_fifteenthAve_09112024_saturday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_09112024_Saturday.csv', 'all_petrol')
	# process_emission_data('FIFTEENTH AVE', '10112024', 'Sunday', 'output/all_petrol/emission_fifteenthAve_10112024_sunday.xml',
	# 					  'output/all_petrol/emissionData_fifteenthAve_10112024_Sunday.csv', 'all_petrol')

	# process_emission_data('NEWTON STREET', '29072024', 'Monday', 'output/all_petrol/emission_newtonStreet_29072024_monday.xml',
	# 					  'output/all_petrol/emissionData_newtonStreet_29072024_monday.csv', 'all_petrol')
	# process_emission_data('NEWTON STREET', '30072024', 'Tuesday', 'output/all_petrol/emission_newtonStreet_30072024_tuesday.xml',
	# 					  'output/all_petrol/emissionData_newtonStreet_30072024_tuesday.csv', 'all_petrol')
	# process_emission_data('NEWTON STREET', '31072024', 'Wednesday', 'output/all_petrol/emission_newtonStreet_31072024_wednesday.xml',
	# 					  'output/all_petrol/emissionData_newtonStreet_31072024_wednesday.csv', 'all_petrol')
	# process_emission_data('NEWTON STREET', '01082024', 'Thursday','output/all_petrol/emission_newtonStreet_01082024_thursday.xml',
	# 					  'output/all_petrol/emissionData_newtonStreet_01082024_thursday.csv', 'all_petrol')
	# process_emission_data('NEWTON STREET', '02082024', 'Friday', 'output/all_petrol/emission_newtonStreet_02082024_friday.xml',
	# 					  'output/all_petrol/emissionData_newtonStreet_02082024_friday.csv', 'all_petrol')
	# process_emission_data('NEWTON STREET', '03082024', 'Saturday', 'output/all_petrol/emission_newtonStreet_03082024_saturday.xml',
	# 					  'output/all_petrol/emissionData_newtonStreet_03082024_saturday.csv', 'all_petrol')
	#process_emission_data('NEWTON STREET', '28072024', 'Sunday', 'output/all_petrol/emission_newtonStreet_28072024_sunday.xml',
	#					  'output/all_petrol/emissionData_newtonStreet_28072024_sunday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '21082023', 'Monday', 'output/all_petrol/emission_turretRoad_21082023_monday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_21082023_monday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '22082023', 'Tuesday', 'output/all_petrol/emission_turretRoad_22082023_tuesday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_22082023_tuesday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '23082023', 'Wednesday', 'output/all_petrol/emission_turretRoad_23082023_wednesday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_23082023_wednesday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '24082023', 'Thursday', 'output/all_petrol/emission_turretRoad_24082023_thursday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_24082023_thursday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '18082023', 'Friday', 'output/all_petrol/emission_turretRoad_18082023_friday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_18082023_friday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '19082023', 'Saturday', 'output/all_petrol/emission_turretRoad_19082023_saturday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_19082023_saturday.csv', 'all_petrol')
	# process_emission_data('TURRET ROAD', '20082023', 'Sunday', 'output/all_petrol/emission_turretRoad_20082023_sunday.xml',
	# 					  'output/all_petrol/emissionData_turretRoad_20082023_sunday.csv', 'all_petrol')

	# process_emission_data('FIFTEENTH AVE', '11112024', 'Monday', 'output/electricCar_4.8/emission_fifteenthAve_11112024_monday_E4.8.xml',
	# 					  'output/electricCar_4.8/emission_fifteenthAve_11112024_monday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('FIFTEENTH AVE', '12112024', 'Tuesday', 'output/electricCar_4.8/emission_fifteenthAve_12112024_tuesday_E4.8.xml',
	# 					  'output/electricCar_4.8/emission_fifteenthAve_12112024_tuesday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('FIFTEENTH AVE', '13112024', 'Wednesday', 'output/electricCar_4.8/emission_fifteenthAve_13112024_wednesday_E4.8.xml',
	# 					  'output/electricCar_4.8/emission_fifteenthAve_13112024_wednesday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('FIFTEENTH AVE', '14112024', 'Thursday', 'output/electricCar_4.8/emission_fifteenthAve_14112024_thursday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_fifteenthAve_14112024_thursday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('FIFTEENTH AVE', '08112024', 'Friday', 'output/electricCar_4.8/emission_fifteenthAve_08112024_friday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_fifteenthAve_08112024_friday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('FIFTEENTH AVE', '09112024', 'Saturday', 'output/electricCar_4.8/emission_fifteenthAve_09112024_saturday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_fifteenthAve_09112024_saturday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('FIFTEENTH AVE', '10112024', 'Sunday', 'output/electricCar_4.8/emission_fifteenthAve_10112024_sunday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_fifteenthAve_10112024_sunday_E4.8.csv', 'electricCar_4.8')

	#======================================================================================================================
	# process_emission_data('TURRET ROAD', '21082023', 'Monday', 'output/electricCar_4.8/emission_turretRoad_21082023_monday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_21082023_monday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('TURRET ROAD', '22082023', 'Tuesday', 'output/electricCar_4.8/emission_turretRoad_22082023_tuesday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_22082023_tuesday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('TURRET ROAD', '23082023', 'Wednesday', 'output/electricCar_4.8/emission_turretRoad_23082023_wednesday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_23082023_wednesday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('TURRET ROAD', '24082023', 'Thursday', 'output/electricCar_4.8/emission_turretRoad_24082023_thursday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_24082023_thursday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('TURRET ROAD', '18082023', 'Friday', 'output/electricCar_4.8/emission_turretRoad_18082023_friday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_18082023_friday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('TURRET ROAD', '19082023', 'Saturday', 'output/electricCar_4.8/emission_turretRoad_19082023_saturday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_19082023_saturday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('TURRET ROAD', '20082023', 'Sunday', 'output/electricCar_4.8/emission_turretRoad_20082023_sunday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_turretRoad_20082023_sunday_E4.8.csv', 'electricCar_4.8')

	#======================================================================================================================
	# process_emission_data('NEWTON STREET', '29072024', 'Monday', 'output/electricCar_4.8/emission_newtonStreet_29072024_monday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_newtonStreet_29072024_monday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('NEWTON STREET', '30072024', 'Tuesday', 'output/electricCar_4.8/emission_newtonStreet_30072024_tuesday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_newtonStreet_30072024_tuesday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('NEWTON STREET', '31072024', 'Wednesday', 'output/electricCar_4.8/emission_newtonStreet_31072024_wednesday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_newtonStreet_31072024_wednesday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('NEWTON STREET', '01082024', 'Thursday', 'output/electricCar_4.8/emission_newtonStreet_01082024_thursday_E4.8.xml',

	#  					  'output/electricCar_4.8/emission_newtonStreet_01082024_thursday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('NEWTON STREET', '02082024', 'Friday', 'output/electricCar_4.8/emission_newtonStreet_02082024_friday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_newtonStreet_02082024_friday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('NEWTON STREET', '03082024', 'Saturday', 'output/electricCar_4.8/emission_newtonStreet_03082024_saturday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_newtonStreet_03082024_saturday_E4.8.csv', 'electricCar_4.8')
	# process_emission_data('NEWTON STREET', '28072024', 'Sunday', 'output/electricCar_4.8/emission_newtonStreet_28072024_sunday_E4.8.xml',
	#  					  'output/electricCar_4.8/emission_newtonStreet_28072024_sunday_E4.8.csv', 'electricCar_4.8')

	#==================================================================================================================

	# process_emission_data('FIFTEENTH AVE', '11112024', 'Monday', 'output/electricCar_10/emission_fifteenthAve_11112024_monday_E10.xml',
	# 					  'output/electricCar_10/emission_fifteenthAve_11112024_monday_E10.csv', 'electricCar_10')


	# process_emission_data('FIFTEENTH AVE', '13112024', 'Wednesday',
	# 					  'output/tracklessTram/emission_fifteenthAve_13112024_wednesday_ttram.xml',
	# 					  'output/tracklessTram/emission_fifteenthAve_13112024_wednesday_ttram.csv', 'trackless_tram')

	# process_emission_data('FIFTEENTH AVE', '13112024', 'Wednesday',
	# 					  'output/carpooling/emission_fifteenthAve_13112024_wednesday_carpooling.xml',
	# 					  'output/carpooling/emission_fifteenthAve_13112024_wednesday_carpooling.csv', 'carpooling')

	process_emission_data('FIFTEENTH AVE', '13112024', 'Wednesday', 'output/electricCar_20/emission_fifteenthAve_13112024_wednesday_E20.xml',
						  'output/electricCar_20/emission_fifteenthAve_13112024_wednesday_E20.csv', 'electricCar_20')


if __name__ == "__main__":

	# calling main function 
	main() 
