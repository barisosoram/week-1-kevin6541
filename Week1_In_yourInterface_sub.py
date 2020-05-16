class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

#Q1. Add Container protocol
  def __contains__(self,member):
      return member in self.__myTeam
#Q2. Add __iter__protocol
  def __iter__(self):
      return iter(self.__myTeam)
    
"""
Q3) Determine if the class classmates implements the __len__ method
class classmate can implement __Len__ method as informal interface to directly
use length function on Teams instance and check number of team membership.
Since __len__ method defined in the class Teams,Classmates is instance of
class Teams which can inherite all attributes and method of class Team. see size protocol
"""
 
def main():
     classmates = Teams(['John', 'Steve', 'Tim'])
     
     #size protocol
     print (len(classmates))#==> Return number of member of team

     #container protocol
     print("Tim" in classmates) #Return True because it is member of team.==>check for membership using the in operator
     print("Sam" in classmates)#Return False because it is not member of team.==>check for membership using the in operator
     # Iterate and print list of member of team
     for member in classmates: 
         print(member)
main()