import GenerateData.conveyor as conveyor
import GenerateData.load_data as load_data

patients = load_data.load_data('dbs_merged_lite.csv')

conveyor.run_deep(patients, './pictures/deep/')
conveyor.run_skin(patients, './pictures/skin/')
conveyor.run_all(patients, './pictures/all/')
