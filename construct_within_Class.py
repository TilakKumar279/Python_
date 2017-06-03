class Bird:
  def __init__(self):
    self.hungry = True
    self.value = 1
  def eat(self):
    self.value +=1
    if self.hungry:
      print ('Aaaah...')
      self.hungry = False
    else:
      print ('No, thanks!')
      
class SongBird(Bird):
  def __init__(self):
    Bird.__init__(self)
    self.sound = 'Squawk!'
  def sing(self):
    print (self.sound)