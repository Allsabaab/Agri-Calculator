data = {
    "Rice":{"seed rate":40,"row spacing":20,"plant spacing":15,"water depth":5,
            "pesticide":{"Chlorantraniliprole":0.85, "Imidacloprid":0.4, "Tricyclazole":1.25,},"yield":0.7,},
    "Wheat":{"seed rate":120,"row spacing":22.5,"plant spacing":5,"water depth":4,
             "pesticide":{"Imidacloprid":0.4, "Propiconazole":1, "Chlorpyrifos":2.75,},"yield":0.5,},
    "Maize":{"seed rate":20,"row spacing":75,"plant spacing":25,"water depth":5,
             "pesticide":{"Emamectin-Benzoate":0.45, "Carbofuran (granules)":0, "Metalaxyl+Mancozeb":2.5,},"yield":0.7,},
    "Potato":{"seed rate":1000,"row spacing":60,"plant spacing":20,"water depth":35,
              "pesticide":{"Mancozeb":2.75, "Dimethoate":1.5, "Chlorpyrifos":2.75,},"yield":0.8},
}
crop_list = list(data.keys())

def seed_calc(s,a):
    seed_rate = data[s]["seed rate"]
    result = float (a*seed_rate)
    dec_formate = f"{result:.2f}".rstrip("0").rstrip(".")
    print(f"Total Seed for {a:.2f} acre Land = {dec_formate} KG.")

def fertilizer_calc(d,a):
    result = float(a*d)
    dec_formate = f"{result:.2f}".rstrip("0").rstrip(".")
    print(f"Total Fertilizer for {a:.2f} acre Land = {dec_formate} KG.")

def plant_pop(p,a,r=False):
    row = float((data[p]["row spacing"])/100)
    plant = float((data[p]["plant spacing"])/100)
    ar1 = float(row*plant)
    ar2 = float(a*4046.86)
    result = round(ar2/ar1)
    if r == True:
        return result
    else:
        print(f"Total plants for {a:.2f} acre land = {result} Plants.")

def water_calc(w,a):
    depth = float((data[w]["water depth"])/100)
    result = float(a*4046.86*depth*1000)
    dec_formate = f"{result:.2f}".rstrip("0").rstrip(".")
    print(f"Total Water needed for {a:.2f} acre Land = {dec_formate} Litre.")

def pest_calc(v,n,c,p):
    pesticide = float(data[c]["pesticide"][p])
    per_tank = float(v*pesticide)
    dec_formate1 = f"{per_tank:.3f}".rstrip("0").rstrip(".")
    total = float(per_tank*n)
    dec_formate2 = f"{total:.3f}".rstrip("0").rstrip(".")
    print(f"Chemical needed per Tank = {dec_formate1} Millilitre.")
    print(f"Total Chemical needed = {dec_formate2} Millilitre.")

def yield_calc(y,a,h):
    population = plant_pop(y,a,r=True)
    result = float(population*h)
    dec_formate = f"{result:.2f}".rstrip("0").rstrip(".")
    print(f"Total Yield for {a:.2f} acre Land = {dec_formate} KG.")

def area_conv():
    while True:
                con = int(input("""1.Acre   2.Bigha   3.Shatak
Enter Area in - """))
                if con == 1:
                    area = float(input("Enter Area: "))
                elif con == 2:
                    area = float(float(input("Enter Area: "))*0.62)
                elif con == 3:
                    area = float(float(input("Enter Area: "))*0.01)
                else:
                    print("INVALID NUMBER!!!")
                    print("")
                    continue
                return area

while True:
    print("""
Welcome to Agri Calculator""")
    print("""1.Rice  2.Wheat  3.Maize  4.Potato""")

    name = int(input("""
Which crop do you want to calculate: """))-1
    if name < len(crop_list):
       crop = crop_list[name]
       harvest = data[crop]["yield"]
    
    while True:
        calc = int(input("""
1.Total Seed Calculation   2.Total Fertilizer Calculation   3.Plant Population Calculation   4.Total Water Calculation
 5.Pesticide Calculation      6.Total YIeld Estimation           7.All Calculation                 8.Exit

What do you want to calculate: """))
        
        print("")
        
        if calc == 1:
            area = area_conv()
            seed_calc(crop,area)
        elif calc == 2:
            area = area_conv()
            dose = float(input("Recommended Fertilizer Dose in KG per Acre: "))
            fertilizer_calc(dose,area)
        elif calc == 3:
            area = area_conv()
            plant_pop(crop,area)
        elif calc == 4:
            area = area_conv()
            water_calc(crop,area)
        elif calc == 5:
            tank_num = int(input("How many Tanks do you have: "))
            tank = float(input("Tank Capacity in Litres: "))
            pest_list = list(data[f"{crop}"]["pesticide"].keys())
            print(f"1.{pest_list[0]}  2.{pest_list[1]}  3.{pest_list[2]}")
            pest = int(input("Which Pesticide: "))-1
            if pest < len(pest_list):
                pesticide = pest_list[pest]
            pest_calc(tank,tank_num,crop,pesticide)
        elif calc == 6:
            area = area_conv()
            yield_calc(crop,area,harvest)

        elif calc == 7:
            area = area_conv()
            dose = float(input("Recommended Fertilizer Dose in KG per Acre: "))
            tank_num = int(input("How many Tanks do you have: "))
            tank = float(input("Tank Capacity in Litres: "))
            pest_list = list(data[f"{crop}"]["pesticide"].keys())
            print(f"1.{pest_list[0]}  2.{pest_list[1]}  3.{pest_list[2]}")
            pest = int(input("Which Pesticide: "))-1
            if pest < len(pest_list):
                pesticide = pest_list[pest]

            seed_calc(crop,area)
            fertilizer_calc(dose,area)
            plant_pop(crop,area)
            water_calc(crop,area)
            pest_calc(tank,tank_num,crop,pesticide)
            yield_calc(crop,area,harvest)

        elif calc == 8:
            break
        else:
            print("INVALID NUMBER!!!")
    
    restart=int(input("""You want to continue?
Press 1 if YES and press 2 if NO :"""))
    if restart==1:
        continue
    else:
        print("Thank You for using Agri Calculator.")
        break
