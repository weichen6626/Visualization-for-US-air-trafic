import json

airport_list = [
    "ATL", 
    "BOS", 
    "BWI", 
    "CLT", 
    "DCA", 
    "DEN", 
    "DFW", 
    "DTW", 
    "EWR", 
    "FLL", 
    "HNL", 
    "IAD", 
    "IAH", 
    "JFK", 
    "LAS", 
    "LAX", 
    "LGA", 
    "MCO", 
    "MDW", 
    "MIA", 
    "MSP", 
    "ORD", 
    "PDX", 
    "PHL", 
    "PHX", 
    "SAN", 
    "SEA", 
    "SFO", 
    "SLC", 
    "TPA"
]

if __name__ == "__main__":
    outputList = []
    for airport in airport_list:
        with open(airport + "_data.json") as json_file:
            data = json.load(json_file)
            for d in data:
                outputList.append(d)
    
    with open("Airports_data.json", 'w') as outfile:
	    json.dump(outputList, outfile)
