class Member:
  def __init__(self, full_name):
    self.full_name = full_name
  
  def introduce(self):
    print(f'Hello, my name is {self.full_name}')

class Student(Member):
  def __init__(self, full_name, reason):
    super().__init__(full_name)
    self.reason = reason
  def show_reason(self):
    print(self.reason)

class Instructor(Member):
  def __init__(self, full_name, bio, skills):
    super().__init__(full_name)
    self.bio = bio
    self.skills = skills
  def show_bio(self):
    print(self.bio)
  def add_skill(self, new_skill):
    self.skills = f'{self.skills}, {new_skill}'
    print(self.skills)

class Workshop:

  def __init__(self, date, subject, group_of_instroctures,  roster_of_students):
    self.date = date
    self.subject = subject
    self.roster_of_students = roster_of_students
    self.group_of_instroctures = group_of_instroctures

  def add_participant(self, member):
    
    if member.__class__.__name__ == 'Student':
      self.roster_of_students.append(member)
      print('cos tam')
    if member.__class__.__name__ == 'Instructor':
      self.group_of_instroctures.append(member)
  
  def print_details(self):
    print(f'Data utworzenia grupy: {self.date}, teamt grupy: {self.subject}. ')
    for student in self.roster_of_students:
      print(f'Imię: {student.full_name}, powód: {student.reason}') 
    for instrocture in self.group_of_instroctures:
      print(f'Imię: {instrocture.full_name}, bio: {instrocture.bio}, umiejętności: {instrocture.skills}')




def main():
  java_course = Workshop('15-07-2022', 'Java', [],  [])
  student1 = Student('Justyna K', 'chcę być mądra')
  student2 = Student('Ania M', 'bede programistą')


  mentor = Instructor('Kasia', 'Lubię placki', 'dzierganie' )
  mentor.add_skill('pieczenie ciast')
  mentor2 = Instructor('Łukasz', 'Kiedyś dorosnę', 'las, kwas, owoce, masło')
  print(mentor.__class__)

  java_course.add_participant(student1)
  java_course.add_participant(student2)
  java_course.add_participant(mentor)
  java_course.add_participant(mentor2)
  java_course.print_details()






if __name__ == '__main__':
  main()