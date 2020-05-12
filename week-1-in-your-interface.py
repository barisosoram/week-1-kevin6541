class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.__max = len(self.__myTeam)

    def __contains__(self,name):
        if name in self.__myTeam:
            return True
        else:
            return False

    def __iter__(self):
        self.__iter = 0
        return self
    def __next__(self):
        if self.__iter < self.__max:
            member = self.__myTeam[self.__iter]
            self.__iter += 1
            return member
        else:
            raise StopIteration
        
    def __len__(self):
        return len(self.__myTeam)
    

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print('Is Tim a part of our team? ' + str('Tim' in classmates))
  print('Is Sara a part of our team? ' + str('Sara' in classmates))
  print('Are both Tim and Sara a part of our team? ' + str('Tim' and 'Sara' in classmates))
  print('Iterating through the member names:')
  for name in classmates:
      print('    ' + name)
  print ('Total number of memebers on our team: ' + str(len(classmates)))

main()


#1) Add the __contains__ protocol and show whether or not  'Tim' and 'Sam' are part of our team.  
#
#2) Add the __iter__ protocol and show how you can print each member of the classmates object.
#
#3) Determine if the class classmates implements the __len__ method.
#
#4) Explain the difference between interfaces and implementation. 
#
#5) Using both visual and written descriptions, think through the interface-implementation of a large
#scale storage system.   In many systems today, we have the ability to store information from a single
#application to a variety of storage devices - local storage (hard drive, usb), the cloud and/or some
#new medium in the future.   How would you design an interface structure such that all of the possible
#implementations could store data effectively.