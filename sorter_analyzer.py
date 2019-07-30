from sorter import sorter

from generic_text_parser import directory_parser

from time_gapper import time_gapper

time_counter = time_gapper(time_gap=1)


def analyze(words):
        
        if len(words) > 9  and  words[2] == "[CISZonesManager::ProcessISLoadData]" and words[10] == "Master" and (words[15][0] == "1" or words[15][0] == "2"):
                induct_line =  "1" +words[6]
                time_counter.increment_value_in_slot(words[0],induct_line)
                
directory_to_parse = '\\\\2.145.48.10\\D$\\LOGS\\Traces\\'
directory_parser(directory_to_parse).parse_directory([analyze])
#directory_to_parse = '\\\\2.145.48.10\\D$\\LOGS\\Traces\\'

print(time_counter.slots)

time_counter.plot(["131"])

