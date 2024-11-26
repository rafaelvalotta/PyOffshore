
# import europe
import geojson

path = "sites/europe/alpha_ventus.geojson"



def read_sites(name):
    base_dir = "sites/europe"
    file_path = f"{base_dir}/{name}.geojson"
    
    with open(file_path, "r") as file:
       site = geojson.load(file)

    return site 
    
test = read_sites("alpha_ventus") 
    
coordinates = test["features"][0]["geometry"]["coordinates"]

    
sites = {
    "Alpha_Ventus": read_sites("alpha_ventus")
    
}

for key in sites:
    print(key)

test = sites["Alpha_Ventus"].get("geometry")


print(sites["Alpha_Ventus"])
print('done')