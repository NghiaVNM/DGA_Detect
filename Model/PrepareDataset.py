import importlib.util

# Process DNS Traffic
module1_path = "../Module/Process_DNSTraffic.py"
module1_name = "Process_DNSTraffic"

spec = importlib.util.spec_from_file_location(module1_name, module1_path)
module1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module1)

module1.process_dns_traffic("../Dataset/Raw/DNSTraffic.csv", "../Dataset/Processed/DNSTraffic_Processed.txt")


# Process Domain dataset
module2_path = "../Module/Process_Domain.py"
module2_name = "Process_Domain.py"

spec = importlib.util.spec_from_file_location(module2_name, module2_path)
module2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module2)

module2.Process_Domain("../Dataset/Raw/Short", "../Dataset/Processed/Short")
