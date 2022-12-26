# Принцип единственной ответственности 

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
  
# myTelephoneDirectory = TelephoneDirectory()
# myTelephoneDirectory.add_entry("Ravi", 123456)
# myTelephoneDirectory.add_entry("Vikas", 678452)
# print(myTelephoneDirectory)

# myTelephoneDirectory.delete_entry("Ravi")
# myTelephoneDirectory.add_entry("Ravi", 123456)
# myTelephoneDirectory.update_entry("Vikas", 776589)
# print(myTelephoneDirectory.lookup_number("Vikas"))
# print(myTelephoneDirectory)

# Принцип единой ответственности гласит, что у каждого класса должна быть только одна «ответственность» и он не должен брать на себя другие обязанности. 
# Мы сделали телефонный справочник, класс TelephoneDirectory, где можно добавлять новую запись, удалять существующую запись, 
# изменять номер телефона и предоставлять поиск.

# Добавив функции сохранения в базу данных и сохранения в файл, мы дали классу дополнительные обязанности, которые не входят в его основную зону ответственности. 
# Теперь в классе есть дополнительные функции, которые могут привести к его изменению. 
# В будущем, если появятся какие-то требования, связанные с сохранением данных, это может привести к изменениям в классе TelephoneDirectory. 
# Получается, что класс TelephoneDirectory подвержен изменениям по причинам, которые не являются его основной ответственностью.

# Принцип единственной ответственности требует от нас не добавлять дополнительные обязанности к классу, чтобы нам не приходилось менять класс, 
# когда нам нужно изменить функционал сохранения справочника в базу данных или в файл. 
# Мы можем передать экземпляр класса TelephoneDirectory экземплярам этих классов и записать любые дополнительные функции в них.
# Так мы гарантируем, что у класса TelephoneDirectory есть лишь одна причина для изменения – это изменения в его основной «ответственности».
