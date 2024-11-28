import time as t
from random import randint

class Auto:
    
    
    
    def __init__(self, typ, laenge, wun_vel, wun_ab, checks, spawn_time):
        
        #self.name=name
        
        self.typ = typ
        
        
        
        self.laenge = laenge
        self.km_zae = 0
        self.meter = 0
        self.back = 0
        
        self.spawn_time = spawn_time
        
        self.g_or_b_zu = True
        self.gas_pedal = 1
        self.gas_counter = 0
        
        self.brems_pedal = 0
        
        
        
        self.wun_vel = wun_vel #in m/s
        
        self.acc = 1.5
        
        self.max_acc = 4.0
        self.min_acc = 0
        self.min_acc = -10
        
        
        self.vel = 1 #in m/s
        
        
        self.vordermann=0
        self.abstand = 0
        self.vel_diff = 0
        self.diff = 0
        #self.geschwindigkeit_angepasst = False
        
        
        self.wun_ab = wun_ab
        self.m_rein = False
        self.m_raus = False
        
        self.checks = checks
        
        self.hab_vordermann = False
        
    def gas_oder_bremsen(gas, bremsen):
        return gas, bremsen
        
        
    def create_auto(art, time):
        if art == "mini":
            laenge = 3
            max_vel = 12
            
            pass
        elif art == "pkw":
            laenge = randint(3, 5)
            max_vel = randint(22, 40)
            pass
        elif art == "van":
            laenge = randint(4, 7)
            max_vel = randint(20, 35)
            pass
        elif art == "lkw":
            laenge = randint(10, 18)
            max_vel = randint(20, 30)
            pass
        elif art == "renn":
            laenge = randint(3, 5)
            max_vel = randint(30, 45)
            pass
        elif art == "bus":
            laenge = randint(8, 12)
            max_vel = randint(20, 30)
            pass
        elif art == "caprio":
            laenge = randint(3, 4)
            max_vel = randint(22, 40)
            pass
        else:
            print("No tpye named " + art+ "! Making PKW")
            laenge = randint(3, 5)
            max_vel = randint(22, 40)
            
        
        if laenge > 10:
            abstand = (max_vel * 3.6)
        else:
            abstand = (max_vel * 3.6) / 2
            
        return Auto(art, laenge, max_vel, abstand, False, time)
        
          
        
        
        
    def fahren(self, time, vorman, vordermann_ges):
         
        self.vordermann=vorman 
        
        self.hab_vordermann = self.vordermann != 0 and self.back < self.vordermann and self.meter != 0
        
        if self.hab_vordermann:
            self.abstand = self.vordermann - self.meter
            
            self.diff = vordermann_ges - self.vel
            
            if self.diff < -10:
                self.vel_diff = 3
            elif self.diff < -5:
                self.vel_diff = 2
            elif self.diff < -1:
                self.vel_diff = 1
            elif self.diff < 1:
                self.vel_diff = 0
            elif self.diff < 5:
                self.vel_diff = -1
            elif self.diff > 5:
                self.vel_diff = -2
            
            
            
           
            
        
        #wenn wunschgeschwindigkeit überschritten
        if self.vel >= self.wun_vel:
            #denn bremsen
            self.g_or_b_zu = Auto.gas_oder_bremsen(0, 1)
            if self.checks:
                print("WTF!")
                t.sleep(1)
            #if self.vel >= self. wun_vel+5:
                #print("ZU SCHNELL")
                #t.sleep(1)
            #wenn zu nah am vordermann
        elif self.abstand <= self.wun_ab / 2 and self.hab_vordermann: 
            if self.vel_diff >= 2:
                    #dann bremsen
                    self.g_or_b_zu = Auto.gas_oder_bremsen(0, 3)
                    
                    #self.geschwindigkeit_angepasst=True
                    
                    #self.vel -= self.acc *time
                    if self.checks:
                        print("SLOWER")
            elif self.vel_diff > 0:
                #dann bremsen
                self.g_or_b_zu = Auto.gas_oder_bremsen(0, 2)
                
                #self.geschwindigkeit_angepasst=True
                
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            elif self.vel_diff == 0:
                #dann bremsen
                self.g_or_b_zu = Auto.gas_oder_bremsen(0, 0)
                
                #self.geschwindigkeit_angepasst=True
                
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
        
            elif self.vel_diff < 0:
                #dann bremsen
                self.g_or_b_zu = Auto.gas_oder_bremsen(1, 0)
                
                #self.geschwindigkeit_angepasst=True
                
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
        
        elif self.abstand <= self.wun_ab  and self.hab_vordermann:
            if self.vel_diff >= 2:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(0, 1)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            elif self.vel_diff == 1:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(0, 0)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            #wenn doppelter wunschabstand zum vordermann       
            elif self.vel_diff == 0:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(1, 0)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            elif self.vel_diff < 0:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(2, 0)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            #wenn doppelter wunschabstand zum vordermann       
            
            
        elif self.abstand <= self.wun_ab * 2  and self.hab_vordermann:
            if self.vel_diff == 3:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(0, 1)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            elif self.vel_diff >= 1:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(0, 0)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
            #wenn doppelter wunschabstand zum vordermann       
            else:
                #dann fuß vom gas
                self.g_or_b_zu = Auto.gas_oder_bremsen(1, 0)
                #self.vel -= self.acc *time
                if self.checks:
                    print("SLOWER")
        
        #wenn man wunschgeschwindigkeit annähert  
        elif self.vel + self. wun_vel/4 >= self.wun_vel:
            #dann fuß vom gas
            self.g_or_b_zu = Auto.gas_oder_bremsen(1, 0)   
        #wenn nicht zu nah am vordermann und noch nicht wunscvhgeschwindigkeit
        elif self.vel < self.wun_vel:
            #dann gas
            self.g_or_b_zu = Auto.gas_oder_bremsen(3, 0)
            
        elif self.vel == self. wun_vel:
            pass

        
        
        # Beschläunigung korregieren
        
        self.gas_pedal, self.brems_pedal = self.g_or_b_zu
        
        #wenn gas und bremse
        if self.gas_pedal != 0 and self.brems_pedal != 0:
            #dann boom
            print("!! BREAK " + self.name + " !!")
            self.vel = 0
        
        #wenn gas
        if self.gas_pedal == 3:
            if self.acc < 0:
                self.acc = 0
            if self.acc <= self.max_acc:
                self.acc+=time*3 
        elif self.gas_pedal == 2:
            if self.acc < 0:
                self.acc = 0
            if self.acc <= self.max_acc:
                self.acc+=time  
        elif self.gas_pedal==1:
            if self.acc < 0:
                self.acc = 0
            if self.acc >= 0 + time:
                self.acc-=time
            else:
                self.acc+=time
    
        elif self.brems_pedal == 1:
            if self.acc > 0:
                self.acc = 0
            if self.acc >= self.min_acc:
                self.acc -= time 
            #if self.checks:
                #print("Ma gucken")
                #t.sleep(1)
        elif self.brems_pedal == 2:  
            self.acc = self.min_acc
            #if self.checks:
                #print("Ma gucken")
                #t.sleep(1)
        elif self.brems_pedal == 3:  
            self.acc = self.min_acc
            if self.vel > time:
                self.vel -= time
            #if self.checks:
                #print("Ma gucken")
                #t.sleep(1)
        else:
            if self.acc >= self.min_acc + time:
                self.acc-=time
            
        
        
        
        
        #calc vel   
        
        
        if self.vel + self.acc*time > 0:
            self.vel += self.acc*time
        else:
            self.vel = 0
        
        #calc meter
        self.km_zae  += self.vel*time
        self.meter += self.vel*time
        #calc hinten
        self.back = self.meter-self.laenge
        
        
