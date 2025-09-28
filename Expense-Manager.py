import random
class Character:
    def __init__(self, name , health , strength , defense , level ,intelligience ):
        self._name=name
        self._health=health
        self._strength=strength
        self._defense=defense
        self._level=level





































        
        self._intelligience=intelligience
    def attack (self,target ):
        damage=self._strength-target ._defense
        if damage<0 :
            damage=0
        target._health=target._health - damage
        if target._health < 0:
            target._health=0
            print(f"{target._name} Died ")
            self._level=self._level+1
        print(f"{self._name} attacks {target._name} for {damage} damage!")
    def take_damage(self , amount  ):
        self._health=self._health-amount
        if self._health < 0:
            self._health=0
            print(f"{self._name} Died ")
       
    def level_up (self):
        self._level=self._level+1
        self._health=self._health+self._health*0.10
        self._strength=self._strength+self._stringth*0.10
        self._defense=self._defense+self._defense*0.10
        self._intelligience=self._intelligience+self._intelligience*0.10
    def alive(self):
        if self._health>0:
            return True
        return False
class Warrior (Character ):
    def __init__(self, name , health , strength , defense , level ,intelligience ):
        super().__init__(name , health , strength , defense , level ,  intelligience )
        self._rage=0
    def take_damage ( self , amount , attacker):
        super().take_damage(amount )
        self._rage+=attacker._strength*0.2
    def power_attack(self , target):
        target.take_damage(self._rage+self._strength , self)
    def attack (self,target ):
        damage=2*(self._strength-target._defense)
        if damage<0 :
            damage=0
        target.take_damage(damage ,self )
        print(f"{self._name} attacks {target._name} for {damage} damage!")
        if target._health<0:
            print(f"{target._name} Died ")
            self._level=self._level+1
class Mage (Character ):
    def __init__(self, name , health , strength , defense , level ,intelligience ):
        super().__init__(name , health , strength , defense , level ,  intelligience )
        self._mana=0.80*self._intelligience
    def take_damage(self , amount , attacker):
        self._health=self._health-amount+int (self._intelligience*0.5)
        if self._health < 0:
            self._health=0
            print(f"{self._name} Died ")
            attacker._level=attacker._level+1
        print(f"{self._name} takes {amount} damage! Health = {self._health}")
    def cast_spell(self , spell, target):
        if spell=="fireball":
            cost=20
            if self._mana >= cost:
                self._mana-=cost
                target.take_damage(self._intelligience , self)
                print(f"{self._name} casts Fireball on {target._name} for {self._intelligience} damage! Mana = {self._mana}")
            else:
                print(f"{self._name} does not have enough mana for Fireball!")
        if spell=="heal":
            cost=10
            if self._mana>=cost:
                self._mana-=cost
                self._health+=int(self._intelligience*0.5)
                print(f"{self._name} casts Heal Healed SuccessFully ")
            else :
                print(f"{self._name} does not have enough mana to Heal!")
               

def playercreation():
    print("Welcome TO create the Character ")
    name = input("Enter yout  Character Name ")
    while True:
        typ=input("Choose character Warrior or Mage ")
        if typ == "Warrior"  or typ=="Mage":
            break
        print("Invalid Choice ")
    total_points=1000
    while True :
        print(f"You have  {total_points} to distribute among the Attributes ")
        try : 
            health=int(input("Enter the Health "))
            defense=int (input("Enter the Defense Points "))
            intelligience=int (input("Enter the Intelligience Points "))
            strength=int (input("Enter the Strength Points "))
            if (health+ defense + intelligience + strength) <= total_points:
                break
            else:
                print("Limit Exceded ")
        except ValueError :
            print("Invalid Data  Try Again ")
    if typ == "Warrior":
        character = Warrior(name, health,strength, 1 , defense, intelligience)
    else:
        character = Mage(name, health, strength, 1,defense, intelligience)
    return character
        
def battle_simulation(characters):
    print("\n Battle Begins \n")

    while sum(1 for c in characters if c.alive()) > 1:
        attacker = random.choice([c for c in characters if c.alive()])
        target = random.choice([c for c in characters if c.alive() and c != attacker])
        move = random.choice(["attack", "spell"])

        print(f"\n {attacker._name}'s turn!")

        if isinstance(attacker, Mage) and move == "spell":
            spell = random.choice(["fireball", "heal"])
            attacker.cast_spell(spell, target)
        else:
            attacker.attack(target)

    winner = [c for c in characters if c.alive()][0]
    print(f"\n Game Over! The winner is {winner._name}!")


c1 = playercreation()
c2 = playercreation()
c3 = playercreation()

characters = [c1, c2, c3]
battle_simulation(characters)