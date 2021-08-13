import datetime

class Note():
  def __init__(self, author, content):
    self.author = author
    self.content = content
    self.created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Notebook():
  def __init__(self):
    self.notes = []
  
  def add_new_note(self, author, content):
    self.notes.append(Note(author, content))
    print('Notatka została dodana')
  
  def add_note(self, note):
    if note.__class__.__name__ == 'Note':
      self.notes.append(note)
      print('Notatka została dodana')
    else: print('Zły format')

  def check_number_of_notes(self):
    print(f'W notatniku jest obecnie {len(self.notes)} notatek.')
  
  def print_all_notes(self):
    if self.notes:
      print('W notatniku znajdują się następujące pozycje: ')
      i = 1
      for note in self.notes:
        print(f'{i}. {note.author.capitalize()}: "{note.content}" dnia {note.created_date} ')
    else:
      print('Notatnik jest pusty')


def main():
  notebook1 = Notebook()
  notebook1.print_all_notes()
  notebook1.add_new_note('Justyna', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ')
  note1 = Note('Ola', 'Morbi a dolor tellus.')
  notebook1.add_note(note1)
  notebook1.check_number_of_notes()
  notebook1.print_all_notes()

if __name__ == '__main__':
  main()