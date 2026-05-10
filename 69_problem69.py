class Employee:
      company = "ITC"
      name = "Dia pal"

      def show(self):
          print(f" The name of the employee is {self.name} and the company is {self.company}")

class coder:
      language = "python"
      company = "ITC.NMC"
      def pythonprintAS(self):
          print(f" Out of all the laguages {self.language} is the best")


class Programmer(Employee,coder):
      language = "Python"
      company = "YAHOO"
      def getLanguage(self):
          print(f"The language is {self.language}")

a = Programmer
a.show(a)