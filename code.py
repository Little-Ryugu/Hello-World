from astropy.constants import M_sun, M_earth, M_jup
import astropy.units as u
class Body(): #parent class
    count=0
    def __init__(self,name,mass): #give celestial body a name and mass
        Body.count+=1

        if not isinstance(name, str) or not (isinstance(mass,float) or  isinstance(mass,int)): #encapsulation
            Body.count-=1
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self.name=name
        if isinstance(mass,int):
             mass=float(mass)
        if not isinstance(mass, float):
            raise ValueError('mass must be float or int') 
        self.mass= mass

    @classmethod
    def get_body_count(cls):     #count how many overal bodies there are
            print('There is',Body.count,'bodies.')

class Star(Body):                #child class of body       inheritance
        def is_body_shiny(self):
            print(self.name,'is shiny.')
        def what_is_the_mass(self):
            mass=round((self.mass/(M_sun.value)),2)*u.M_sun
            print('Mass of',self.name,'is',mass)
class Planet(Body):              #child class of body       inheritance
    def is_body_shiny(self):
        print(self.name,'is not shiny.')
    def what_is_the_mass(self):
        mass=round((self.mass/(M_earth.value)),2)*u.M_earth
        print('Mass of',self.name,'is',mass)
#setting up bodies
sun= Star('Sun',M_sun.value)
print(sun)
print(sun.name)
earth=Planet('Earth',M_earth.value)
jupiter=Planet('Jupiter',M_jup.value)
sirius=Star('Sirius',4.6e30)
#testing 
sun.what_is_the_mass()
sun.is_body_shiny()  
print('')
earth.what_is_the_mass()
earth.is_body_shiny() 
print('')
jupiter.what_is_the_mass()
jupiter.is_body_shiny()
print('')
sirius.what_is_the_mass()
sirius.is_body_shiny()
print('')
Body.get_body_count()
