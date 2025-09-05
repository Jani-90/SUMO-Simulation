import pandas as pd # To read excel data
import helper.generate_xml as gen

def run_demand_file(input_file, output_file):

    #Read the traffic counts
    counts = pd.read_excel(input_file, "Sheet1")
    route = pd.read_excel(input_file, "Sheet2")
    vclass = pd.read_excel(input_file, "Sheet3")

    # Generate demand file
    gen.generate_demand_file(counts, route, vclass, output_file)


def main():
    run_demand_file(input_file='data/fifteenthAve-11112024-Monday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_11112024_Monday.rou.xml')
    run_demand_file(input_file='data/fifteenthAve-12112024-Tuesday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_12112024_Tuesday.rou.xml')
    run_demand_file(input_file='data/fifteenthAve-13112024-Wednesday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_13112024_Wednesday.rou.xml')
    run_demand_file(input_file='data/fifteenthAve-14112024-Thursday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_14112024_Thursday.rou.xml')
    run_demand_file(input_file='data/fifteenthAve-08112024-Friday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_08112024_Friday.rou.xml')
    run_demand_file(input_file='data/fifteenthAve-09112024-Saturday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_09112024_Saturday.rou.xml')
    run_demand_file(input_file='data/fifteenthAve-10112024-Sunday.xlsx',
                    output_file='demand/all_petrol/vehicle_demand_fifteenthAve_10112024_Sunday.rou.xml')

    #=============================================================================================================

    #run_demand_file(input_file='data/turretRoad - 21082023-Monday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_21082023_Monday.rou.xml')
    # run_demand_file(input_file='data/turretRoad - 22082023-Tuesday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_22082023_Tuesday.rou.xml')
    # run_demand_file(input_file='data/turretRoad - 23082023-Wednesday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_23082023_Wednesday.rou.xml')
    # run_demand_file(input_file='data/turretRoad - 24082023-Thursday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_24082023_Thursday.rou.xml')
    # run_demand_file(input_file='data/turretRoad - 18082023-Friday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_18082023_Friday.rou.xml')
    # run_demand_file(input_file='data/turretRoad - 19082023-Saturday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_19082023_Saturday.rou.xml')
    # run_demand_file(input_file='data/turretRoad - 20082023-Sunday.xlsx',
    #                output_file='demand/all_petrol/vehicle_demand_turretRoad_20082023_Sunday.rou.xml')

    #=================================================================================================================

    #run_demand_file(input_file='data/newtonStreet-29072024-Monday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_29072024_Monday.rou.xml')
    #run_demand_file(input_file='data/newtonStreet-30072024-Tuesday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_30072024_Tuesday.rou.xml')
    #run_demand_file(input_file='data/newtonStreet-31072024-Wednesday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_31072024_Wednesday.rou.xml')
    #run_demand_file(input_file='data/newtonStreet-01082024-Thursday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_01082024_Thursday.rou.xml')
    #run_demand_file(input_file='data/newtonStreet-02082024-Friday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_02082024_Friday.rou.xml')
    #run_demand_file(input_file='data/newtonStreet-03082024-Saturday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_03082024_Saturday.rou.xml')
    #run_demand_file(input_file='data/newtonStreet-28072024-Sunday.xlsx', output_file='demand/all_petrol/vehicle_demand_newtonStreet_28072024_Sunday.rou.xml')





if __name__ == "__main__":
    # calling main function
    main()





