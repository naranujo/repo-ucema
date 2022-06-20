
class Contacto():
   def __init__(self):
       self.mail = "mail"
       self.direccion = "direccion"
       self.telefono = "telefono"

   def serialize(self):
       return {
                'mail': self.mail,
                'direccion': self.direccion,
                "telefono": self.telefono
            }