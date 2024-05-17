import pyxel

#LightAndFight par Johan et Lena

class FightUi:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.states = False
        self.enemyhealth = 5
        self.enemycolor = 0

        
    def update(self):
        global IsAttacking
        global attackingcmpt
        self.x = 0
        if IsAttacking:
            attackingcmpt = attackingcmpt + 1
        
        if attackingcmpt >= 150:
            IsAttacking =not IsAttacking
            attackingcmpt = 0
    def draw(self):
        global IsAttacking
        global FightPlayer
        global IsFighting
        global attackingcmpt
        pyxel.rectb(4,40,121,66,13) #Bord du cadre combat
        
        #pyxel.rectb(64,0,2,128,11) "le centre"
        
        #Dessiner l'ennemie (a voir avec lena)
        pyxel.circb(64,20,15,self.enemycolor)
        
        #Dessiner les boxs
        pyxel.rectb(6,109,36,11,13)
        pyxel.rectb(46,109,36,11,13)
        pyxel.rectb(87,109,36,11,13)
        
        #Ui
        pyxel.text(10,112,f"Atk:{150-attackingcmpt}",5)
        pyxel.text(48,112,f"Vie: {FightPlayer.health}",5)
        pyxel.text(96,112,"Fuite",5)
        
        if not IsAttacking:
            pyxel.text(30,64,"ESPACE POUR ATTAQUER",8)
            if pyxel.btn(pyxel.KEY_SPACE):
                self.enemyhealth -= 1
                pyxel.play(0,1)
                if self.enemyhealth <= 0 :
                    IsFighting = False
                IsAttacking = True
        
        pyxel.text(10,10,f"Vie : {self.enemyhealth}",8)
            
        
        
        
        
class Player:
    
    def __init__(self):
        self.x = 64
        self.y = 72
        self.vie = 100
        self.colorpatern = 0
        self.colorcooldown = 5
        self.showcoll = False
        self.health = 10
        
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x -5 > 5 :
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x+5 < 123 :
            self.x += 1
            
        if pyxel.btn(pyxel.KEY_UP) and self.y-9 > 41:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y+11 < 104:
            self.y += 1
        
    def draw(self):
        pyxel.tri(self.x-5,self.y,self.x+5,self.y,self.x,self.y+11,13) #Cone
            
        if self.colorpatern == 0:
            pyxel.tri(self.x-2,self.y-1,self.x+2,self.y-1,self.x,self.y-9,14) #Grande flamme
            pyxel.tri(self.x-5,self.y-1,self.x,self.y-1,self.x-2,self.y-5,9) #Flamme gauche
            pyxel.tri(self.x+5,self.y-1,self.x,self.y-1,self.x+2,self.y-5,10) #Flame Droite
            pyxel.tri(self.x+1,self.y-1,self.x-1,self.y-1,self.x,self.y-2,8) #Petite flamme
            
        if self.colorpatern == 1:
            pyxel.tri(self.x-2,self.y-1,self.x+2,self.y-1,self.x,self.y-9,19) #Grande flamme
            pyxel.tri(self.x-5,self.y-1,self.x,self.y-1,self.x-2,self.y-5,10) #Flamme gauche
            pyxel.tri(self.x+5,self.y-1,self.x,self.y-1,self.x+2,self.y-5,14) #Flame Droite
            pyxel.tri(self.x+1,self.y-1,self.x-1,self.y-1,self.x,self.y-2,2) #Petite flamme
            
        if self.colorpatern == 2:
            pyxel.tri(self.x-2,self.y-1,self.x+2,self.y-1,self.x,self.y-9,10) #Grande flamme
            pyxel.tri(self.x-5,self.y-1,self.x,self.y-1,self.x-2,self.y-5,14) #Flamme gauche
            pyxel.tri(self.x+5,self.y-1,self.x,self.y-1,self.x+2,self.y-5,9) #Flame Droite
            pyxel.tri(self.x+1,self.y-1,self.x-1,self.y-1,self.x,self.y-2,8) #Petite flamme
        
        if self.colorcooldown <= 0:
            self.colorpatern += 1
            self.colorcooldown = 5
        self.colorcooldown -= 1 
        if self.colorpatern >= 3:
            self.colorpatern = 0
            
        self.Coll()
        
    def Coll(self):
        global EnemyList
        global IsFighting
        global Vies
        #Les coins du player
        coin1 = [self.x-5,self.y-9]
        coin2 = [self.x+5,self.y-9]
        coin3 = [self.x+5,self.y+11]
        coin4 = [self.x-5,self.y+11]
        if self.showcoll:
            pyxel.rectb(coin1[0],coin1[1],1,1,11)
            pyxel.rectb(coin2[0],coin2[1],1,1,15)
            pyxel.rectb(coin3[0],coin3[1],1,1,2)
            pyxel.rectb(coin4[0],coin4[1],1,1,9)
        
        for i in EnemyList:
            toRemove = []
            icoin1 = [i.x-i.rayon,i.y-i.rayon]
            icoin2 = [i.x+i.rayon,i.y-i.rayon]
            icoin3 = [i.x+i.rayon,i.y+i.rayon]
            icoin4 = [i.x-i.rayon,i.y+i.rayon]
            if self.showcoll:
                pyxel.rectb(icoin1[0],icoin1[1],1,1,11)
                pyxel.rectb(icoin2[0],icoin2[1],1,1,15)
                pyxel.rectb(icoin3[0],icoin3[1],1,1,2)
                pyxel.rectb(icoin4[0],icoin4[1],1,1,9)
                
                
            if coin1[0] < icoin2[0] + 5 and coin4[0] + 10 > icoin1[0] and coin1[1] < icoin2[1] + 5 and coin4[1] + 10 > icoin1[1] : 
                toRemove.append(i)  
        

            for i in toRemove:
                EnemyList.remove(i)
                self.health -= 1
                pyxel.play(1,2)
                if self.health <= 0:
                    pyxel.play(2,3)
                    Vies -= 1
                    IsFighting = False
                    self.health = 10
                    EnemyList = []
                
            
        
        
class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rayon = 5
        
    def __del__(self):
        pass
        
    def update(self):
        if self.y < 100:
            self.y += 1
            
            
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.rayon,3)
        
    
class Player2 :
    def __init__(self):
        self.x=20
        self.y=20
        self.cpt=0
        self.cooldown=4
        self.colorpatern = 0
        self.colorcooldown = 5
        self.sprint=100
        self.cooldown_sprint=10
        
    def update(self):
        
        self.cooldown_sprint-=1
        self.cooldown-=1
        if self.cooldown==0:
            
            self.cpt+=1
            self.cooldown=4
        
        if self.sprint<100 and self.cooldown_sprint<=0:
            self.sprint+=1
            self.cooldown_sprint=10
            
        if pyxel.btn(pyxel.KEY_SHIFT)and self.sprint>0 :
            
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x+=2
                self.sprint-=1
                
            
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.x-=2
                self.sprint-=1
               
            
            elif pyxel.btn(pyxel.KEY_UP):
                self.y-=2
                self.sprint-=1
                
            
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.y+=2
            
                self.sprint-=1
            
            
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x+=1
          
            
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.x-=1
            self.cooldown-=1
            
        elif pyxel.btn(pyxel.KEY_UP):
            self.y-=1
            self.cooldown-=1
            
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y+=1
            self.cooldown-=1

            
    def draw(self):
        global FightPlayer
        global Vies
        #compteur
        pyxel.rectb(2,3,20,10,7)
        pyxel.text(4,5,str(self.cpt),7)
        
        #sprint
        pyxel.rectb(2,13,20,10,7)
        pyxel.text(4,16,str(self.sprint),7)
        
        #Vies
        pyxel.rectb(106,3,20,10,7)
        pyxel.text(108,6,f"V: {Vies}",7)
        
        #personnage
        pyxel.rect(self.x-1,self.y+2,3,7,8) #1 corps
        pyxel.circ(self.x,self.y,2,15) #tête
        pyxel.rect(self.x+1,self.y+4,4,1,15) #2 bras droit
        pyxel.rect(self.x-2,self.y+4,1,4,15) #2 bras gauche
        pyxel.rect(self.x-1,self.y+9,1,4,15) #2 jambe gauche
        pyxel.rect(self.x+1,self.y+9,1,4,15) #2 jambe droite
        pyxel.rect(self.x-1,self.y+9,1,2,5) #2 short gauche
        pyxel.rect(self.x+1,self.y+9,1,2,5) #2 short droite
        pyxel.rectb(self.x-1,self.y,1,1,4) #2 oeil gauche
        pyxel.rectb(self.x+1,self.y,1,1,4) #2 oeil droite
        
        #collisions perso
        coin1 = [self.x-2,self.y-2]
        coin2 = [self.x+10,self.y]
        coin3 = [self.x-2,self.y+12]
        coin4 = [self.x+10,self.y+12]
        
        if FightPlayer.showcoll:
            pyxel.rectb(coin1[0],coin1[1],1,1,2) #1
            pyxel.rectb(coin2[0],coin2[1],1,1,2) #2
            pyxel.rectb(coin3[0],coin3[1],1,1,2) #3
            pyxel.rectb(coin4[0],coin4[1],1,1,2) #4


        #Flamme
        pyxel.tri(self.x+3,self.y,self.x+9,self.y,self.x+6,self.y+5,13) #Cone
        
        if self.colorpatern == 0:
            pyxel.tri(self.x+3,self.y-1,self.x+9,self.y-1,self.x+6,self.y-5,14) #Grande flamme
            
            pyxel.tri(self.x+3,self.y-1,self.x+5,self.y-3,self.x+6,self.y-1,9) #Flamme gauche
            
            pyxel.tri(self.x+6,self.y-1,self.x+8,self.y-3,self.x+9,self.y-1,9) #Flame Droite
            pyxel.tri(self.x+5,self.y-1,self.x+7,self.y-1,self.x+6,self.y-2,8) #Petite flamme
            
        elif self.colorpatern == 1:
            pyxel.tri(self.x+3,self.y-1,self.x+9,self.y-1,self.x+6,self.y-5,19) #Grande flamme
            pyxel.tri(self.x+3,self.y-1,self.x+5,self.y-3,self.x+6,self.y-1,10) #Flamme gauche
            pyxel.tri(self.x+6,self.y-1,self.x+8,self.y-3,self.x+9,self.y-1,14) #Flame Droite
            pyxel.tri(self.x+5,self.y-1,self.x+7,self.y-1,self.x+6,self.y-2,2) #Petite flamme
            
        elif self.colorpatern == 2:
            pyxel.tri(self.x+3,self.y-1,self.x+9,self.y-1,self.x+6,self.y-5,19) #Grande flamme
            pyxel.tri(self.x+3,self.y-1,self.x+5,self.y-3,self.x+6,self.y-1,14) #Flamme gauche
            pyxel.tri(self.x+6,self.y-1,self.x+8,self.y-3,self.x+9,self.y-1,9) #Flame Droite
            pyxel.tri(self.x+5,self.y-1,self.x+7,self.y-1,self.x+6,self.y-2,8) #Petite flamme
        
        if self.colorcooldown <= 0:
            self.colorpatern += 1
            self.colorcooldown = 5
        self.colorcooldown -= 1 
        if self.colorpatern >= 3:
            self.colorpatern = 0
            
            

class Enemy2:
    def __init__(self):
        self.x=pyxel.rndi(1,128)
        self.y=130
        self.color=pyxel.rndi(1,15)
        self.cooldown=150
        self.depart()
    
    def __del__(self):
        pass
    
    def update(self):
        global joueur
        if self.cooldown>=0:
            if joueur.x <= self.x and joueur.y <= self.y :                
                self.x-=1
                self.y-=1
                self.cooldown-=1
            elif joueur.x <= self.x and joueur.y >= self.y :                
                self.x-=1
                self.y+=1
                self.cooldown-=1
            elif joueur.x >= self.x and joueur.y <= self.y :                
                self.x+=1
                self.y-=1
                self.cooldown-=1
            elif joueur.x >= self.x and joueur.y >= self.y :                
                self.x+=1
                self.y+=1
                self.cooldown-=1
        else:
            self.depart()
            
    def draw(self):
        global joueur
        global IsFighting
        global FightWindow
        global FightPlayer

        
        coin1 = [joueur.x-2,joueur.y-2]
        coin2 = [joueur.x+10,joueur.y]
        coin3 = [joueur.x-2,joueur.y+12]
        coin4 = [joueur.x+10,joueur.y+12]
        
        pyxel.circb(self.x,self.y,4,self.color)#enemy
        
        icoin1 = [self.x-4,self.y]
        icoin2 = [self.x+4,self.y-4]
        icoin3 = [self.x-4,self.y+4]
        icoin4 = [self.x+4,self.y+4]
        if FightPlayer.showcoll:
            pyxel.rect(icoin1[0],icoin1[1],1,1,10)#1
            pyxel.rect(icoin2[0],icoin2[1],1,1,10)#2
            pyxel.rect(icoin3[0],icoin3[1],1,1,10)#3
            pyxel.rect(icoin4[0],icoin4[1],1,1,10)#4
        
        if coin1[0] < icoin2[0] + 5 and coin4[0] + 10 > icoin1[0] and coin1[1] < icoin2[1] + 5 and coin4[1] + 10 > icoin1[1] : 
                IsFighting = True
                FightWindow.enemycolor = self.color
                FightWindow.enemyhealth = 5
                FightPlayer.health = 10
                pyxel.play(0,0)
                self.depart()
                
        
        

        
    def depart(self):
        self.x=pyxel.rndi(1,128)
        self.y=130
        couleur_non = [4,11,14,15]
        self.color=pyxel.rndi(1,15)
        if self.color in couleur_non:
            self.depart()
        self.cooldown=150
        
        
class Monde:
    def __init__(self):
        pass
    
    def draw(self):
        pyxel.rect(22,0,80,128,4)
        pyxel.rect(22,0,2,128,14)
        pyxel.rect(100,0,2,128,14)
        pyxel.rect(63,0,2,128,15)
        

        
        
def update():
    global Vies
    
    if Vies <= 0:
        pass
    if Vies > 0:
        global IsFighting
        if IsFighting:
            
            global EnemyList
            global FightPlayer
            global FightUi
            global IsAttacking
            FightWindow.update()
            toRemove = []
            
            FightPlayer.update()
            
            if IsAttacking:
                if pyxel.rndi(1,300) < 30:
                    EnemyList.append(Enemy(pyxel.rndi(10,119),40))
                    
                
                for i in EnemyList:
                    i.update()
                    if i.y >= 100:
                        toRemove.append(i)

                for i in toRemove:
                    EnemyList.remove(i)
                    
            if not IsAttacking:
                EnemyList = []
        
        if not IsFighting:
            joueur.update()
            adversaire.update()
            if pyxel.btn(pyxel.KEY_TAB):
                IsFighting = True
    
    
    
    
def draw():
    global joueur
    global Vies
    if Vies <= 0:
        pyxel.cls(0)
        pyxel.text(28,44,f"Vous avez perdu !",2)
        pyxel.text(28, 60,f"voici votre score: {joueur.cpt}",2)
    if Vies > 0:
        global IsFighting
        if IsFighting:
            
            global FightWindow
            global FightPlayer
            global EnemyList
            pyxel.cls(0)
            FightWindow.draw()
            FightPlayer.draw()
            for i in EnemyList:
                i.draw()
                
        if not IsFighting:
            pyxel.cls(11)
            monde.draw()
            joueur.draw()
            adversaire.draw()

        
    
    
    

pyxel.init(128,128,"nuit du code")
pyxel.load("res.pyxres")
joueur=Player2()
monde=Monde()
adversaire=Enemy2()
Vies = 3
FightWindow = FightUi()
FightPlayer = Player()
IsFighting = False
IsAttacking = True
attackingcmpt = 0

EnemyList = []

pyxel.run(update,draw)



