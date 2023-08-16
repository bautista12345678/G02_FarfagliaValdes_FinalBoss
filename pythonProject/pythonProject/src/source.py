import csv
class Ship:
    ship_count=0  #contador static de ships
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        Ship.ship_count +=1  #incremento el contador estatico
    def is_worth_it(self):
        d = int(self.draft) #aca y en el resto del programa casteo las entradas del csv por si acaso.
        c = int(self.crew)
        Value = 0
        Value = d - c*1.5
        print(Value)
        if Value > 20:
             print("¡A saquear!")
             return True
        else :
             print("¡Dejenlo pasar!")
             return False
    def get_ship_count(cls):
        return cls.ship_count
class Cargo(Ship):
    def __init__(self, draft, crew, extra, quality):
        Ship.__init__(self, draft, crew)
        self.extra = extra
        self.quality = quality
    def is_worth_it(self):
        d = int(self.draft)
        c = int(self.crew)
        e = int(self.extra)
        q = float(self.quality)
        Value = 0
        if q==1:
            Value = d - c * 1.5 - (e * 3.5)
        elif q == 0.5:
            Value = d - c * 1.5 - (e * 2)
        elif q == 0.25:
            Value = d - c * 1.5 - (e * 0.5)
        elif q == 0:
            Value = 0
        print(Value)
        if Value > 20:
            print("¡A saquear!")
            return True
        elif Value<20 and Value!=0:
            print("¡Dejenlo pasar!")
            return False
        elif Value==0:
            print("Mercancia sin calidad... dejenlo pasar.")
            return False

class Cruise(Ship):
     def __init__(self, draft, crew, extra):
         Ship.__init__(self, draft, crew)
         self.extra = extra
     def is_worth_it(self):
         d = int(self.draft)
         c = int(self.crew)
         e = int(self.extra)
         Value = 0
         Value = d - c*(1.5) - e * (2.25)
         print(Value)
         if Value > 20:
             print("¡A saquear!")
             return True
         else:
             print("¡Dejenlo pasar!")
             return False

def tipo_de_barco():
    barcos=[]
    with open("../pythonProject/ships.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader) #me salteo la primera fila para no cargar el encabezado, mucho mas facil que salvar una excepcion
        for row in reader:
            draft, crew, extra, quality = row  # "formateo row"
            if (quality != '' and extra != ''):
                barcos.append(Cargo(draft, crew, extra, quality))
            elif (quality == '' and extra != ''):
                barcos.append(Cruise(draft, crew, extra))
            elif (quality == '' and extra == ''):
                barcos.append(Ship(draft, crew))
            try: #lo que hago en este try es terrible, busco levantar la excepcion como sea, debe corregirse con raise.
                if (quality != '' and extra == ''):
                    print("a")
            except NameError:
                print("Excepcion, el barco que veo es imposible, no lo cargaré")
    return barcos


def main():
    barco = tipo_de_barco()
    for x in barco:
        state = x.is_worth_it() #state no sirve, solo es necesaria la variable

