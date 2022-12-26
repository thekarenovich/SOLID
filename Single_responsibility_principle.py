class TelephoneDirectory:
  def __init__(self):
    self.telephonedirectory = {}

  def add_entry(self, name, number):
    self.telephonedirectory[name] = number

  def delete_entry(self, name):
    self.telephonedirectory.pop(name)

  def update_entry(self, name, number):
    self.telephonedirectory[name] = number

  def lookup_number(self, name):
    return self.telephonedirectory[name]
 
#   def save_to_file(self, file_name, location):
#     pass

#   def persist_to_database(self, database_details):
#     pass

  def __str__(self):
    ret_dct = ""
    for key, value in self.telephonedirectory.items():
      ret_dct += f'{key} : {value}\n'
    return ret_dct
  
class persist_to_database:
  def __init__(self, object_to_persist):
    pass

class save_to_file:
  def __init__(self, object_to_save):
    pass
  
  
# Принцип единой ответственности гласит, что у каждого класса должна быть только одна «ответственность» и он не должен брать на себя другие обязанности. 
# Мы сделали телефонный справочник, класс TelephoneDirectory, где можно добавлять новую запись, удалять существующую запись, изменять номер телефона и предоставлять поиск.




